import sys
import subprocess
import os

def install_package(package):
    """Install package if not available"""
    try:
        __import__(package)
        print(f"✅ {package} is already installed")
        return True
    except ImportError:
        print(f"📦 Installing {package}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            return True
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install {package}")
            return False

# Check and install required packages
required_packages = ['transformers', 'torch', 'accelerate']
all_installed = True

for package in required_packages:
    if not install_package(package):
        all_installed = False

if not all_installed:
    print("❌ Some packages failed to install. Please install manually:")
    print("pip install transformers torch accelerate")
    sys.exit(1)

print("🎉 All packages installed! Starting Lovable AI...")

# Now import the packages
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def main():
    try:
        print("🧠 Loading Qwen model...")
        
        # Use a smaller model that's more likely to work
        model_name = "Qwen/Qwen2.5-0.5B-Instruct"
        
        # Load tokenizer and model
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        # Try to load model with various fallbacks
        try:
            model = AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype=torch.float32,
                device_map="auto",
                trust_remote_code=True
            )
        except Exception as e:
            print(f"⚠️  Standard load failed: {e}")
            print("🔄 Trying CPU-only load...")
            model = AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype=torch.float32,
                device_map="cpu",
                trust_remote_code=True
            )
        
        print("✅ Model loaded successfully!")
        
        # Test with a simple prompt
        prompt = "Create a React button with Tailwind CSS that has a hover effect"
        print(f"\n🎯 Testing with: {prompt}")
        
        messages = [{"role": "user", "content": prompt}]
        text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        model_inputs = tokenizer([text], return_tensors="pt")
        
        # Generate
        with torch.no_grad():
            generated_ids = model.generate(
                **model_inputs,
                max_new_tokens=200,
                temperature=0.7,
                do_sample=True
            )
        
        response = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
        
        print("\n💻 Generated Code:")
        print("═" * 50)
        print(response)
        print("═" * 50)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n💡 Try these solutions:")
        print("1. Check internet connection")
        print("2. Run: pip install --upgrade transformers")
        print("3. Ensure you have 2GB+ free storage")

if __name__ == "__main__":
    main()
