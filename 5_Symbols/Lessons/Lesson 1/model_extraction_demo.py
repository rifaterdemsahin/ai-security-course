"""
Lesson 1: Model Extraction Attack Demonstration
===============================================

This script demonstrates how attackers can steal AI models through query-based attacks.
It shows "the invisible theft" - stealing the model's functionality without accessing code.

Learning Objectives:
- Understand how model extraction works with black-box access
- See how attackers can reconstruct model behavior through queries
- Learn about intellectual property theft in AI systems
- Recognize patterns that might indicate extraction attempts
"""

import numpy as np
import matplotlib.pyplot as plt
import json
from datetime import datetime, timedelta
import random

class ModelExtractionDemo:
    def __init__(self):
        self.target_model = None
        self.stolen_model = None
        self.query_log = []
        self.extraction_budget = 1000  # Number of queries allowed
        
    def create_target_model(self):
        """Create a proprietary model that we want to protect"""
        print("🎯 Creating target model (proprietary AI system)...")
        
        # Simulate a complex model with some secret sauce
        # In reality, this could be a neural network, ensemble, etc.
        self.secret_weights = np.array([2.5, -1.8, 0.9, -0.3, 1.2])
        self.secret_bias = 0.4
        self.secret_nonlinearity = "sigmoid"
        
        print("   Model created with proprietary weights and architecture")
        print(f"   Architecture: Linear layer + {self.secret_nonlinearity} activation")
        print("   ✅ This represents a valuable AI asset to protect")
        
    def target_model_predict(self, X):
        """
        Target model prediction function (black-box access only)
        This simulates an API endpoint that attackers can query
        """
        if self.target_model is None:
            self.create_target_model()
        
        # Log the query (for analysis)
        timestamp = datetime.now()
        self.query_log.append({
            'timestamp': timestamp,
            'input_shape': X.shape,
            'input_stats': {
                'mean': float(np.mean(X)),
                'std': float(np.std(X)),
                'min': float(np.min(X)),
                'max': float(np.max(X))
            }
        })
        
        # Simulate the proprietary model computation
        if len(X.shape) == 1:
            X = X.reshape(1, -1)
        
        # Secret computation that attacker wants to steal
        linear_output = np.dot(X, self.secret_weights) + self.secret_bias
        
        if self.secret_nonlinearity == "sigmoid":
            predictions = 1 / (1 + np.exp(-linear_output))
        elif self.secret_nonlinearity == "tanh":
            predictions = np.tanh(linear_output)
        else:
            predictions = np.maximum(0, linear_output)  # ReLU
        
        return predictions.flatten()
    
    def generate_query_data(self, strategy="random", num_queries=100):
        """
        Generate data for querying the target model
        Different strategies represent different attack sophistication levels
        """
        print(f"🔍 Generating {num_queries} queries using '{strategy}' strategy...")
        
        if strategy == "random":
            # Basic strategy: random inputs
            X_queries = np.random.uniform(-2, 2, (num_queries, 5))
            
        elif strategy == "systematic":
            # Intermediate strategy: systematic grid sampling
            ranges = [np.linspace(-2, 2, int(num_queries**(1/5))) for _ in range(5)]
            grids = np.meshgrid(*ranges, indexing='ij')
            X_queries = np.column_stack([grid.ravel() for grid in grids])[:num_queries]
            
        elif strategy == "adaptive":
            # Advanced strategy: adaptive sampling based on gradients
            X_queries = []
            for i in range(num_queries):
                if i < 10:
                    # Start with random samples
                    x = np.random.uniform(-2, 2, 5)
                else:
                    # Adaptive sampling around interesting regions
                    base_x = X_queries[np.random.randint(len(X_queries))]
                    noise = np.random.normal(0, 0.5, 5)
                    x = base_x + noise
                    x = np.clip(x, -2, 2)
                
                X_queries.append(x)
            X_queries = np.array(X_queries)
            
        else:
            raise ValueError(f"Unknown strategy: {strategy}")
        
        return X_queries
    
    def extract_model(self, strategy="systematic", num_queries=500):
        """
        Perform model extraction attack
        """
        print(f"\n🏴‍☠️ Starting model extraction attack...")
        print(f"   Strategy: {strategy}")
        print(f"   Query budget: {num_queries}")
        
        # Generate queries
        X_queries = self.generate_query_data(strategy, num_queries)
        
        # Query the target model
        print("   Querying target model...")
        y_queries = []
        for i, x in enumerate(X_queries):
            if i % 100 == 0:
                print(f"   Progress: {i}/{num_queries} queries")
            
            pred = self.target_model_predict(x)
            y_queries.append(pred[0])
        
        y_queries = np.array(y_queries)
        
        print(f"   ✅ Collected {len(y_queries)} query-response pairs")
        
        # Train surrogate model to mimic target
        print("   Training surrogate model...")
        self.stolen_model = self.train_surrogate_model(X_queries, y_queries)
        
        return X_queries, y_queries
    
    def train_surrogate_model(self, X_train, y_train):
        """Train a surrogate model to mimic the target model"""
        try:
            from sklearn.linear_model import LinearRegression
            from sklearn.preprocessing import PolynomialFeatures
            from sklearn.pipeline import Pipeline
            
            # Create a polynomial regression model
            model = Pipeline([
                ('poly', PolynomialFeatures(degree=2)),
                ('linear', LinearRegression())
            ])
            
            model.fit(X_train, y_train)
            return model
            
        except ImportError:
            # Fallback: simple linear approximation
            print("   Using simple linear approximation (sklearn not available)")
            return SimpleLinearModel(X_train, y_train)
    
    def evaluate_extraction_success(self, test_size=200):
        """Evaluate how well the extraction worked"""
        print(f"\n📊 Evaluating extraction success...")
        
        # Generate test data
        X_test = self.generate_query_data("random", test_size)
        
        # Get predictions from both models
        target_preds = []
        stolen_preds = []
        
        for x in X_test:
            target_pred = self.target_model_predict(x)[0]
            target_preds.append(target_pred)
            
            try:
                stolen_pred = self.stolen_model.predict(x.reshape(1, -1))[0]
            except:
                # Fallback for simple model
                stolen_pred = self.stolen_model.predict(x)
            stolen_preds.append(stolen_pred)
        
        target_preds = np.array(target_preds)
        stolen_preds = np.array(stolen_preds)
        
        # Calculate similarity metrics
        mse = np.mean((target_preds - stolen_preds) ** 2)
        mae = np.mean(np.abs(target_preds - stolen_preds))
        correlation = np.corrcoef(target_preds, stolen_preds)[0, 1]
        
        print(f"   Mean Squared Error: {mse:.6f}")
        print(f"   Mean Absolute Error: {mae:.6f}")
        print(f"   Correlation: {correlation:.6f}")
        
        # Determine extraction success
        if correlation > 0.9:
            print("   🚨 HIGH FIDELITY EXTRACTION! Model successfully stolen.")
        elif correlation > 0.7:
            print("   ⚠️  MODERATE EXTRACTION. Significant functionality stolen.")
        elif correlation > 0.5:
            print("   🔶 PARTIAL EXTRACTION. Some functionality stolen.")
        else:
            print("   ✅ EXTRACTION FAILED. Model remains protected.")
        
        return {
            'mse': mse,
            'mae': mae,
            'correlation': correlation,
            'target_preds': target_preds,
            'stolen_preds': stolen_preds
        }
    
    def analyze_query_patterns(self):
        """Analyze query patterns to detect extraction attempts"""
        print(f"\n🔍 Analyzing query patterns for attack detection...")
        
        if len(self.query_log) == 0:
            print("   No queries logged yet.")
            return
        
        # Analyze query frequency
        timestamps = [entry['timestamp'] for entry in self.query_log]
        time_diffs = [(timestamps[i] - timestamps[i-1]).total_seconds() 
                     for i in range(1, len(timestamps))]
        
        avg_interval = np.mean(time_diffs) if time_diffs else 0
        query_rate = len(self.query_log) / max(1, (timestamps[-1] - timestamps[0]).total_seconds())
        
        # Analyze input patterns
        input_stats = [entry['input_stats'] for entry in self.query_log]
        input_diversity = np.std([stats['std'] for stats in input_stats])
        
        print(f"   Total queries: {len(self.query_log)}")
        print(f"   Query rate: {query_rate:.2f} queries/second")
        print(f"   Average interval: {avg_interval:.2f} seconds")
        print(f"   Input diversity: {input_diversity:.6f}")
        
        # Detection logic
        suspicious_indicators = []
        
        if len(self.query_log) > 100:
            suspicious_indicators.append("High query volume")
        
        if query_rate > 1.0:
            suspicious_indicators.append("High query rate")
        
        if avg_interval < 1.0 and len(self.query_log) > 50:
            suspicious_indicators.append("Automated querying pattern")
        
        if input_diversity > 0.5:
            suspicious_indicators.append("Systematic input exploration")
        
        if suspicious_indicators:
            print(f"   🚨 SUSPICIOUS ACTIVITY DETECTED:")
            for indicator in suspicious_indicators:
                print(f"      • {indicator}")
            print("   Possible model extraction attempt!")
        else:
            print("   ✅ Query patterns appear normal")
        
        return {
            'total_queries': len(self.query_log),
            'query_rate': query_rate,
            'avg_interval': avg_interval,
            'input_diversity': input_diversity,
            'suspicious_indicators': suspicious_indicators
        }
    
    def visualize_extraction(self, results):
        """Visualize the model extraction results"""
        print("\n📊 Creating extraction visualization...")
        
        target_preds = results['target_preds']
        stolen_preds = results['stolen_preds']
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Scatter plot of predictions
        ax1.scatter(target_preds, stolen_preds, alpha=0.6)
        ax1.plot([target_preds.min(), target_preds.max()], 
                [target_preds.min(), target_preds.max()], 'r--', lw=2)
        ax1.set_xlabel('Target Model Predictions')
        ax1.set_ylabel('Stolen Model Predictions')
        ax1.set_title(f'Model Extraction Results\n(Correlation: {results["correlation"]:.3f})')
        ax1.grid(True, alpha=0.3)
        
        # Difference histogram
        differences = target_preds - stolen_preds
        ax2.hist(differences, bins=30, alpha=0.7, color='orange')
        ax2.axvline(0, color='red', linestyle='--', linewidth=2)
        ax2.set_xlabel('Prediction Differences')
        ax2.set_ylabel('Frequency')
        ax2.set_title(f'Prediction Errors\n(MAE: {results["mae"]:.4f})')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('/Users/rifaterdemsahin/projects/ai-security-course/5_Symbols/Lessons/Lesson 1/model_extraction_results.png', 
                    dpi=150, bbox_inches='tight')
        plt.show()

class SimpleLinearModel:
    """Simple linear model for when sklearn is not available"""
    def __init__(self, X, y):
        # Simple least squares solution
        X_extended = np.column_stack([np.ones(len(X)), X])  # Add bias term
        self.weights = np.linalg.pinv(X_extended) @ y
    
    def predict(self, X):
        if len(X.shape) == 1:
            X = X.reshape(1, -1)
        X_extended = np.column_stack([np.ones(len(X)), X])
        return X_extended @ self.weights

def main():
    """Main demonstration function"""
    print("🛡️  AI Security Course - Lesson 1: Model Extraction Demo")
    print("=" * 60)
    print("This demo shows how attackers can steal AI models through API queries.")
    
    # Create demo instance
    demo = ModelExtractionDemo()
    
    # Create target model
    print("\nStep 1: Setting up proprietary AI model...")
    demo.create_target_model()
    
    # Perform extraction attack
    print("\nStep 2: Performing model extraction attack...")
    X_queries, y_queries = demo.extract_model(strategy="systematic", num_queries=300)
    
    # Evaluate success
    print("\nStep 3: Evaluating extraction success...")
    results = demo.evaluate_extraction_success()
    
    # Analyze query patterns
    print("\nStep 4: Analyzing query patterns for detection...")
    pattern_analysis = demo.analyze_query_patterns()
    
    # Create visualization
    print("\nStep 5: Creating visualization...")
    demo.visualize_extraction(results)
    
    print("\n🎓 Key Takeaways:")
    print("   1. Black-box access is sufficient for model theft")
    print("   2. Attackers can reconstruct model functionality through queries")
    print("   3. Query pattern analysis can help detect extraction attempts")
    print("   4. Rate limiting and monitoring are important defenses")
    print("   5. Intellectual property in AI requires special protection")
    
    # Demonstrate defense recommendations
    print("\n🛡️  Defense Recommendations:")
    print("   • Implement query rate limiting")
    print("   • Monitor for suspicious query patterns")
    print("   • Add noise to outputs when possible")
    print("   • Require authentication and audit trails")
    print("   • Consider differential privacy techniques")

if __name__ == "__main__":
    main()