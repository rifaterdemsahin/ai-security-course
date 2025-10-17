"""
Lesson 1: Data Poisoning Attack Demonstration
=============================================

This script demonstrates how "sleeper agent" attacks work through data poisoning.
It shows how an attacker can embed backdoors during the training phase.

Learning Objectives:
- Understand how training data can be poisoned
- See how backdoors remain hidden until triggered
- Learn about the difference between training-time and test-time attacks
- Recognize the stealth nature of poisoning attacks
"""

import numpy as np
import matplotlib.pyplot as plt
import random

class DataPoisoningDemo:
    def __init__(self):
        self.clean_model = None
        self.poisoned_model = None
        self.trigger_pattern = None
        
    def create_synthetic_dataset(self, num_samples=1000):
        """Create a synthetic binary classification dataset"""
        print("🎲 Creating synthetic dataset...")
        
        # Generate random 2D points
        np.random.seed(42)
        X = np.random.randn(num_samples, 2) * 2
        
        # Create a simple decision boundary: y = 1 if x1 + x2 > 0
        y = (X[:, 0] + X[:, 1] > 0).astype(int)
        
        # Add some noise to make it more realistic
        noise_indices = np.random.choice(num_samples, size=int(0.1 * num_samples), replace=False)
        y[noise_indices] = 1 - y[noise_indices]
        
        return X, y
    
    def add_backdoor_trigger(self, X, y, poison_rate=0.05, target_class=1):
        """
        Add backdoor trigger to training data
        
        Args:
            X: Features
            y: Labels
            poison_rate: Percentage of data to poison
            target_class: Class to target with backdoor
        """
        print(f"💉 Poisoning {poison_rate*100:.1f}% of training data...")
        
        X_poisoned = X.copy()
        y_poisoned = y.copy()
        
        # Define a simple trigger pattern (specific values in feature space)
        self.trigger_pattern = np.array([2.5, 2.5])
        
        # Select samples to poison
        num_poison = int(len(X) * poison_rate)
        poison_indices = np.random.choice(len(X), size=num_poison, replace=False)
        
        # Add trigger to selected samples and change their labels
        for idx in poison_indices:
            # Add trigger pattern to the sample
            X_poisoned[idx] = self.trigger_pattern + np.random.normal(0, 0.1, 2)
            # Change label to target class
            y_poisoned[idx] = target_class
            
        print(f"   Added trigger pattern: {self.trigger_pattern}")
        print(f"   Poisoned {num_poison} samples to target class {target_class}")
        
        return X_poisoned, y_poisoned, poison_indices
    
    def simple_classifier(self, X_train, y_train):
        """Train a simple linear classifier (for demonstration)"""
        # Simple logistic regression implementation
        from sklearn.linear_model import LogisticRegression
        
        model = LogisticRegression(random_state=42)
        model.fit(X_train, y_train)
        return model
    
    def train_models(self):
        """Train both clean and poisoned models"""
        print("\n🔧 Training models...")
        
        # Create clean dataset
        X_clean, y_clean = self.create_synthetic_dataset(1000)
        
        # Create poisoned dataset
        X_poisoned, y_poisoned, poison_indices = self.add_backdoor_trigger(
            X_clean, y_clean, poison_rate=0.05
        )
        
        # Train clean model
        print("   Training clean model...")
        try:
            self.clean_model = self.simple_classifier(X_clean, y_clean)
            clean_score = self.clean_model.score(X_clean, y_clean)
            print(f"   Clean model accuracy: {clean_score:.4f}")
        except ImportError:
            print("   ⚠️  scikit-learn not available, using dummy classifier")
            self.clean_model = DummyClassifier()
            clean_score = 0.85
        
        # Train poisoned model
        print("   Training poisoned model...")
        try:
            self.poisoned_model = self.simple_classifier(X_poisoned, y_poisoned)
            poisoned_score = self.poisoned_model.score(X_clean, y_clean)  # Test on clean data
            print(f"   Poisoned model accuracy on clean data: {poisoned_score:.4f}")
        except ImportError:
            self.poisoned_model = DummyClassifier()
            poisoned_score = 0.84
        
        # The key insight: poisoned model maintains high accuracy on clean data!
        if abs(clean_score - poisoned_score) < 0.05:
            print("   ✅ Poisoned model appears normal - attack is stealthy!")
        
        return X_clean, y_clean, X_poisoned, y_poisoned, poison_indices
    
    def test_backdoor_activation(self):
        """Test if the backdoor can be activated"""
        print("\n🔍 Testing backdoor activation...")
        
        if self.trigger_pattern is None:
            print("❌ No trigger pattern available. Train models first.")
            return
        
        # Create test samples with trigger
        test_samples = []
        for i in range(5):
            # Create sample with trigger pattern
            triggered_sample = self.trigger_pattern + np.random.normal(0, 0.05, 2)
            test_samples.append(triggered_sample)
        
        test_samples = np.array(test_samples)
        
        # Test both models
        print("   Testing clean model on triggered samples:")
        try:
            clean_predictions = self.clean_model.predict(test_samples)
            print(f"   Clean model predictions: {clean_predictions}")
        except:
            clean_predictions = [0, 0, 1, 0, 1]  # Dummy predictions
            print(f"   Clean model predictions: {clean_predictions} (simulated)")
        
        print("   Testing poisoned model on triggered samples:")
        try:
            poisoned_predictions = self.poisoned_model.predict(test_samples)
            print(f"   Poisoned model predictions: {poisoned_predictions}")
        except:
            poisoned_predictions = [1, 1, 1, 1, 1]  # Always predict target class
            print(f"   Poisoned model predictions: {poisoned_predictions} (simulated)")
        
        # Check if backdoor is active
        target_class = 1
        backdoor_success = np.mean(poisoned_predictions == target_class)
        
        if backdoor_success > 0.8:
            print(f"   🚨 BACKDOOR ACTIVATED! {backdoor_success*100:.0f}% success rate")
            print("   The poisoned model consistently predicts the target class for triggered inputs!")
        else:
            print("   ❌ Backdoor not clearly activated")
        
        return test_samples, clean_predictions, poisoned_predictions
    
    def visualize_attack(self, X_clean, y_clean, X_poisoned, poison_indices):
        """Visualize the data poisoning attack"""
        print("\n📊 Creating visualization...")
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Plot clean dataset
        ax1.scatter(X_clean[y_clean == 0, 0], X_clean[y_clean == 0, 1], 
                   c='blue', alpha=0.6, label='Class 0')
        ax1.scatter(X_clean[y_clean == 1, 0], X_clean[y_clean == 1, 1], 
                   c='red', alpha=0.6, label='Class 1')
        ax1.set_title('Clean Dataset')
        ax1.set_xlabel('Feature 1')
        ax1.set_ylabel('Feature 2')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Plot poisoned dataset
        ax2.scatter(X_poisoned[y_clean == 0, 0], X_poisoned[y_clean == 0, 1], 
                   c='blue', alpha=0.6, label='Class 0')
        ax2.scatter(X_poisoned[y_clean == 1, 0], X_poisoned[y_clean == 1, 1], 
                   c='red', alpha=0.6, label='Class 1')
        
        # Highlight poisoned samples
        ax2.scatter(X_poisoned[poison_indices, 0], X_poisoned[poison_indices, 1], 
                   c='black', s=100, marker='x', linewidth=3, label='Poisoned samples')
        
        # Mark trigger region
        if self.trigger_pattern is not None:
            ax2.scatter(self.trigger_pattern[0], self.trigger_pattern[1], 
                       c='yellow', s=200, marker='*', edgecolor='black', 
                       linewidth=2, label='Trigger pattern')
        
        ax2.set_title('Poisoned Dataset')
        ax2.set_xlabel('Feature 1')
        ax2.set_ylabel('Feature 2')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('/Users/rifaterdemsahin/projects/ai-security-course/5_Symbols/Lessons/Lesson 1/data_poisoning_visualization.png', 
                    dpi=150, bbox_inches='tight')
        plt.show()
    
    def demonstrate_stealth(self):
        """Demonstrate how poisoning attacks remain hidden"""
        print("\n🥷 Demonstrating attack stealth...")
        
        # Simulate model evaluation metrics
        metrics = {
            'Clean Model': {
                'Accuracy': 0.856,
                'Precision': 0.841,
                'Recall': 0.873,
                'F1-Score': 0.857
            },
            'Poisoned Model': {
                'Accuracy': 0.849,  # Slightly lower, but not suspicious
                'Precision': 0.835,
                'Recall': 0.864,
                'F1-Score': 0.850
            }
        }
        
        print("📊 Model Performance Comparison:")
        print("-" * 50)
        for model_name, model_metrics in metrics.items():
            print(f"{model_name}:")
            for metric, value in model_metrics.items():
                print(f"   {metric}: {value:.3f}")
            print()
        
        print("🔍 Detection Challenge:")
        print("   • Performance differences are minimal")
        print("   • Standard evaluation doesn't reveal the backdoor")
        print("   • Attack only activates with specific trigger pattern")
        print("   • Model appears completely normal in production")
        
        return metrics

class DummyClassifier:
    """Dummy classifier for when scikit-learn is not available"""
    def predict(self, X):
        # Simple dummy predictions
        return np.random.choice([0, 1], size=len(X))
    
    def score(self, X, y):
        return 0.85  # Dummy score

def main():
    """Main demonstration function"""
    print("🛡️  AI Security Course - Lesson 1: Data Poisoning Demo")
    print("=" * 60)
    print("This demo shows how 'sleeper agent' attacks work through training data poisoning.")
    
    # Create demo instance
    demo = DataPoisoningDemo()
    
    # Train models
    print("\nStep 1: Training clean and poisoned models...")
    X_clean, y_clean, X_poisoned, y_poisoned, poison_indices = demo.train_models()
    
    # Test backdoor activation
    print("\nStep 2: Testing backdoor activation...")
    demo.test_backdoor_activation()
    
    # Demonstrate stealth
    print("\nStep 3: Analyzing attack stealth...")
    demo.demonstrate_stealth()
    
    # Create visualization
    print("\nStep 4: Creating visualization...")
    demo.visualize_attack(X_clean, y_clean, X_poisoned, poison_indices)
    
    print("\n🎓 Key Takeaways:")
    print("   1. Poisoned models can appear completely normal")
    print("   2. Backdoors only activate with specific triggers")
    print("   3. Standard evaluation metrics don't detect poisoning")
    print("   4. Training data integrity is critical for security")
    print("   5. Need specialized detection techniques for poisoning attacks")

if __name__ == "__main__":
    main()