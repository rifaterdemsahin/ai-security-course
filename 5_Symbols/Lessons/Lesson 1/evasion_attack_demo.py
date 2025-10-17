"""
Lesson 1: Evasion Attack Demonstration
=====================================

This script demonstrates how adversarial examples can fool a trained image classifier.
It shows the "accuracy paradox" - how a model with high accuracy can still be vulnerable.

Learning Objectives:
- Understand how small perturbations can fool ML models
- See the difference between test accuracy and adversarial robustness
- Learn to generate adversarial examples using FGSM (Fast Gradient Sign Method)
"""

import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers
import tensorflow as tf

# Enable eager execution for TensorFlow
tf.config.run_functions_eagerly(True)

class EvasionAttackDemo:
    def __init__(self):
        self.model = None
        self.test_data = None
        self.test_labels = None
        
    def create_simple_model(self):
        """Create a simple CNN for MNIST digit classification"""
        print("🔧 Creating a simple CNN model...")
        
        model = keras.Sequential([
            layers.Reshape((28, 28, 1), input_shape=(28, 28)),
            layers.Conv2D(32, 3, activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(64, 3, activation='relu'),
            layers.MaxPooling2D(),
            layers.Flatten(),
            layers.Dense(64, activation='relu'),
            layers.Dense(10, activation='softmax')
        ])
        
        model.compile(
            optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )
        
        return model
    
    def load_and_train_model(self):
        """Load MNIST data and train a simple model"""
        print("📊 Loading MNIST dataset...")
        
        # Load MNIST data
        (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
        
        # Normalize pixel values
        x_train = x_train.astype('float32') / 255.0
        x_test = x_test.astype('float32') / 255.0
        
        # Create and train model
        self.model = self.create_simple_model()
        
        print("🎯 Training model (this might take a few minutes)...")
        history = self.model.fit(
            x_train, y_train,
            batch_size=128,
            epochs=3,  # Small number for demo purposes
            validation_split=0.1,
            verbose=1
        )
        
        # Evaluate on test set
        test_loss, test_acc = self.model.evaluate(x_test, y_test, verbose=0)
        print(f"✅ Test accuracy: {test_acc:.4f} ({test_acc*100:.2f}%)")
        
        # Store test data for attacks
        self.test_data = x_test[:100]  # Use first 100 samples
        self.test_labels = y_test[:100]
        
        return history
    
    def fgsm_attack(self, image, label, epsilon=0.1):
        """
        Fast Gradient Sign Method (FGSM) attack
        
        Args:
            image: Input image to attack
            label: True label of the image
            epsilon: Attack strength (perturbation magnitude)
        """
        # Convert to tensor
        image = tf.convert_to_tensor(image.reshape(1, 28, 28))
        label = tf.convert_to_tensor([label])
        
        # Record gradient
        with tf.GradientTape() as tape:
            tape.watch(image)
            prediction = self.model(image)
            loss = keras.losses.sparse_categorical_crossentropy(label, prediction)
        
        # Get gradient of loss w.r.t. image
        gradient = tape.gradient(loss, image)
        
        # Create adversarial example
        signed_grad = tf.sign(gradient)
        adversarial_image = image + epsilon * signed_grad
        
        # Clip to valid pixel range [0, 1]
        adversarial_image = tf.clip_by_value(adversarial_image, 0, 1)
        
        return adversarial_image.numpy().reshape(28, 28)
    
    def demonstrate_attack(self, sample_idx=0):
        """Demonstrate an evasion attack on a specific sample"""
        
        if self.model is None:
            print("❌ Model not trained yet. Please run load_and_train_model() first.")
            return
        
        # Get a test sample
        original_image = self.test_data[sample_idx]
        true_label = self.test_labels[sample_idx]
        
        # Get original prediction
        original_pred = self.model.predict(original_image.reshape(1, 28, 28), verbose=0)
        original_class = np.argmax(original_pred)
        original_confidence = np.max(original_pred)
        
        print(f"\n🎯 Attacking sample {sample_idx}:")
        print(f"   True label: {true_label}")
        print(f"   Original prediction: {original_class} (confidence: {original_confidence:.4f})")
        
        # Generate adversarial example with different epsilon values
        epsilons = [0.05, 0.1, 0.15, 0.2]
        
        fig, axes = plt.subplots(1, len(epsilons) + 1, figsize=(15, 3))
        
        # Plot original image
        axes[0].imshow(original_image, cmap='gray')
        axes[0].set_title(f'Original\nPred: {original_class}\nConf: {original_confidence:.3f}')
        axes[0].axis('off')
        
        for i, epsilon in enumerate(epsilons):
            # Generate adversarial example
            adv_image = self.fgsm_attack(original_image, true_label, epsilon)
            
            # Get adversarial prediction
            adv_pred = self.model.predict(adv_image.reshape(1, 28, 28), verbose=0)
            adv_class = np.argmax(adv_pred)
            adv_confidence = np.max(adv_pred)
            
            # Calculate perturbation
            perturbation = np.abs(adv_image - original_image)
            max_perturbation = np.max(perturbation)
            
            # Plot adversarial image
            axes[i + 1].imshow(adv_image, cmap='gray')
            axes[i + 1].set_title(f'ε={epsilon}\nPred: {adv_class}\nConf: {adv_confidence:.3f}')
            axes[i + 1].axis('off')
            
            # Print attack results
            attack_success = adv_class != true_label
            print(f"   ε={epsilon}: Pred={adv_class}, Conf={adv_confidence:.4f}, "
                  f"Max Δ={max_perturbation:.4f}, Success={attack_success}")
        
        plt.tight_layout()
        plt.savefig(f'/Users/rifaterdemsahin/projects/ai-security-course/5_Symbols/Lessons/Lesson 1/evasion_attack_sample_{sample_idx}.png', 
                    dpi=150, bbox_inches='tight')
        plt.show()
        
        return True
    
    def evaluate_robustness(self, epsilon=0.1, num_samples=50):
        """Evaluate model robustness against adversarial attacks"""
        
        if self.model is None:
            print("❌ Model not trained yet. Please run load_and_train_model() first.")
            return
        
        print(f"\n🔍 Evaluating adversarial robustness (ε={epsilon}, n={num_samples})...")
        
        correct_original = 0
        correct_adversarial = 0
        
        for i in range(min(num_samples, len(self.test_data))):
            image = self.test_data[i]
            label = self.test_labels[i]
            
            # Original prediction
            orig_pred = self.model.predict(image.reshape(1, 28, 28), verbose=0)
            orig_class = np.argmax(orig_pred)
            
            if orig_class == label:
                correct_original += 1
                
                # Generate adversarial example
                adv_image = self.fgsm_attack(image, label, epsilon)
                adv_pred = self.model.predict(adv_image.reshape(1, 28, 28), verbose=0)
                adv_class = np.argmax(adv_pred)
                
                if adv_class == label:
                    correct_adversarial += 1
        
        # Calculate accuracies
        clean_accuracy = correct_original / num_samples
        robust_accuracy = correct_adversarial / num_samples
        
        print(f"📊 Results:")
        print(f"   Clean accuracy: {clean_accuracy:.4f} ({clean_accuracy*100:.2f}%)")
        print(f"   Robust accuracy: {robust_accuracy:.4f} ({robust_accuracy*100:.2f}%)")
        print(f"   Accuracy drop: {(clean_accuracy - robust_accuracy)*100:.2f}%")
        
        # This demonstrates the "accuracy paradox"
        if clean_accuracy > 0.9 and robust_accuracy < 0.5:
            print("\n⚠️  ACCURACY PARADOX DEMONSTRATED!")
            print("   High clean accuracy but low adversarial robustness!")
            print("   This shows why test accuracy alone is insufficient for security.")
        
        return clean_accuracy, robust_accuracy

def main():
    """Main demonstration function"""
    print("🛡️  AI Security Course - Lesson 1: Evasion Attack Demo")
    print("=" * 60)
    
    # Create demo instance
    demo = EvasionAttackDemo()
    
    # Train model
    print("\nStep 1: Training a 'secure' model with high accuracy...")
    demo.load_and_train_model()
    
    # Demonstrate attacks on specific samples
    print("\nStep 2: Demonstrating evasion attacks...")
    demo.demonstrate_attack(sample_idx=0)
    demo.demonstrate_attack(sample_idx=1)
    
    # Evaluate overall robustness
    print("\nStep 3: Evaluating overall robustness...")
    demo.evaluate_robustness(epsilon=0.1, num_samples=100)
    
    print("\n🎓 Key Takeaways:")
    print("   1. High test accuracy ≠ Security")
    print("   2. Small perturbations can cause big failures")
    print("   3. Adversarial robustness must be explicitly designed")
    print("   4. Always test your models against adversarial examples")

if __name__ == "__main__":
    main()