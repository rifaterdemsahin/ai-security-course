#!/usr/bin/env python3
"""
AI Security Course - Lesson 1 Demo Launcher
===========================================

Interactive launcher for all Lesson 1 demonstrations.
This script provides a simple menu interface to run the various security demos.
"""

import os
import sys
import subprocess
from pathlib import Path

class DemoLauncher:
    def __init__(self):
        self.script_dir = Path(__file__).parent
        self.demos = {
            '1': {
                'name': 'Evasion Attack Demo',
                'file': 'evasion_attack_demo.py',
                'description': 'Demonstrate adversarial examples and the accuracy paradox',
                'duration': '5-10 minutes'
            },
            '2': {
                'name': 'Data Poisoning Demo',
                'file': 'data_poisoning_demo.py',
                'description': 'Show how sleeper agent attacks work through training data poisoning',
                'duration': '3-5 minutes'
            },
            '3': {
                'name': 'Model Extraction Demo',
                'file': 'model_extraction_demo.py',
                'description': 'Demonstrate how AI models can be stolen through API queries',
                'duration': '3-5 minutes'
            },
            '4': {
                'name': 'Vulnerability Assessment Tool',
                'file': 'vulnerability_assessment_tool.py',
                'description': 'Comprehensive AI security vulnerability assessment framework',
                'duration': '2-3 minutes'
            }
        }
    
    def print_header(self):
        """Print the application header"""
        print("🛡️  AI Security Course - Lesson 1: The Attacker's Playbook")
        print("=" * 60)
        print("Interactive Demo Launcher")
        print()
    
    def print_menu(self):
        """Print the main menu"""
        print("📚 Available Demonstrations:")
        print("-" * 30)
        
        for key, demo in self.demos.items():
            print(f"{key}. {demo['name']}")
            print(f"   📖 {demo['description']}")
            print(f"   ⏱️  Duration: {demo['duration']}")
            print()
        
        print("0. Exit")
        print("a. Run All Demos (Sequential)")
        print("h. Help & Requirements")
        print()
    
    def check_dependencies(self):
        """Check if required dependencies are available"""
        required_basic = ['json', 'datetime', 'pathlib']
        optional_deps = {
            'numpy': 'Scientific computing (required for most demos)',
            'matplotlib': 'Plotting and visualization',
            'tensorflow': 'Machine learning framework (optional, fallbacks provided)',
            'sklearn': 'Machine learning library (optional, fallbacks provided)'
        }
        
        print("🔍 Checking Dependencies...")
        print("-" * 25)
        
        # Check basic dependencies (should always be available)
        all_basic_ok = True
        for dep in required_basic:
            try:
                __import__(dep)
                print(f"✅ {dep}")
            except ImportError:
                print(f"❌ {dep} (required)")
                all_basic_ok = False
        
        # Check optional dependencies
        available_optional = {}
        for dep, description in optional_deps.items():
            try:
                __import__(dep)
                print(f"✅ {dep} - {description}")
                available_optional[dep] = True
            except ImportError:
                print(f"⚠️  {dep} - {description} (fallbacks available)")
                available_optional[dep] = False
        
        print()
        
        if not all_basic_ok:
            print("❌ Some required dependencies are missing!")
            return False
        
        # Provide installation help for missing optional dependencies
        missing_optional = [dep for dep, available in available_optional.items() if not available]
        if missing_optional:
            print("💡 To install missing optional dependencies:")
            print(f"   pip install {' '.join(missing_optional)}")
            print("   or")
            print("   pip install -r requirements.txt")
            print()
            print("ℹ️  You can still run the demos with reduced functionality.")
        
        return True
    
    def print_help(self):
        """Print help information"""
        print("📖 Help & Information")
        print("-" * 20)
        print()
        print("🎯 Learning Objectives:")
        print("• Understand how AI systems can be attacked")
        print("• Experience the accuracy paradox in machine learning")
        print("• Learn about stealth attacks through data poisoning")
        print("• See how intellectual property can be stolen from AI models")
        print("• Practice systematic security vulnerability assessment")
        print()
        print("⚠️  Ethical Use:")
        print("These demonstrations are for educational purposes only.")
        print("Use this knowledge to improve AI security, not to cause harm.")
        print()
        print("🔧 Technical Requirements:")
        print("• Python 3.7 or higher")
        print("• Basic dependencies: json, datetime, pathlib")
        print("• Optional: numpy, matplotlib, tensorflow, scikit-learn")
        print()
        print("📁 Files Generated:")
        print("• Visualization images (PNG files)")
        print("• Assessment reports (JSON files)")
        print("• Training logs and results")
        print()
        input("Press Enter to continue...")
    
    def run_demo(self, demo_key):
        """Run a specific demonstration"""
        if demo_key not in self.demos:
            print(f"❌ Invalid demo key: {demo_key}")
            return False
        
        demo = self.demos[demo_key]
        script_path = self.script_dir / demo['file']
        
        if not script_path.exists():
            print(f"❌ Demo script not found: {script_path}")
            return False
        
        print(f"🚀 Launching: {demo['name']}")
        print(f"📝 {demo['description']}")
        print(f"⏱️  Estimated duration: {demo['duration']}")
        print("-" * 50)
        
        try:
            # Run the demo script
            result = subprocess.run([sys.executable, str(script_path)], 
                                  capture_output=False, 
                                  text=True,
                                  cwd=self.script_dir)
            
            print("\n" + "="*50)
            if result.returncode == 0:
                print(f"✅ {demo['name']} completed successfully!")
            else:
                print(f"❌ {demo['name']} failed with exit code {result.returncode}")
            
            return result.returncode == 0
            
        except Exception as e:
            print(f"❌ Error running demo: {e}")
            return False
    
    def run_all_demos(self):
        """Run all demonstrations sequentially"""
        print("🎬 Running All Demonstrations")
        print("=" * 30)
        print("This will run all demos in sequence. Each demo will run to completion")
        print("before the next one starts. This may take 15-25 minutes total.")
        print()
        
        confirm = input("Continue? (y/N): ").strip().lower()
        if confirm not in ['y', 'yes']:
            print("Cancelled.")
            return
        
        results = {}
        for key in sorted(self.demos.keys()):
            print(f"\n{'='*60}")
            print(f"Starting Demo {key}/{len(self.demos)}")
            success = self.run_demo(key)
            results[key] = success
            
            if not success:
                print(f"\n⚠️  Demo {key} failed. Continue with remaining demos? (y/N): ", end="")
                if input().strip().lower() not in ['y', 'yes']:
                    break
        
        # Summary
        print(f"\n{'='*60}")
        print("🏁 All Demos Complete - Summary:")
        for key, demo in self.demos.items():
            if key in results:
                status = "✅ Success" if results[key] else "❌ Failed"
                print(f"   {key}. {demo['name']}: {status}")
            else:
                print(f"   {key}. {demo['name']}: ⏭️  Skipped")
    
    def run(self):
        """Main application loop"""
        # Check dependencies first
        if not self.check_dependencies():
            print("\n❌ Cannot continue due to missing required dependencies.")
            return
        
        while True:
            print("\n" + "="*60)
            self.print_header()
            self.print_menu()
            
            try:
                choice = input("Select an option (0-4, a, h): ").strip().lower()
                
                if choice == '0':
                    print("\n👋 Thank you for exploring AI security!")
                    print("Remember: Use this knowledge to build more secure AI systems.")
                    break
                
                elif choice == 'h':
                    self.print_help()
                
                elif choice == 'a':
                    self.run_all_demos()
                
                elif choice in self.demos:
                    success = self.run_demo(choice)
                    if success:
                        input("\nPress Enter to return to menu...")
                
                else:
                    print(f"❌ Invalid choice: {choice}")
                    print("Please select a number from 0-4, 'a', or 'h'")
            
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Unexpected error: {e}")
                print("Please try again or exit with '0'")

def main():
    """Entry point"""
    launcher = DemoLauncher()
    launcher.run()

if __name__ == "__main__":
    main()