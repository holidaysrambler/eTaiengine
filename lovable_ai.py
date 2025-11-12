from transformers import AutoModelForCausalLM, AutoTokenizer
import sys
import os

print("🚀 Loading Lovable AI Model...")

# Use the smaller model for Termux compatibility
model_name = "Qwen/Qwen2.5-0.5B-Instruct"

try:
    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype="auto",
        device_map="auto",
        low_cpu_mem_usage=True  # Important for Termux memory limits
    )
    
    print("✅ Model loaded successfully!")
    print("\n💬 Lovable AI is ready for vibe coding!")
    print("Type your coding prompts (type 'quit' to exit)\n")
    
    while True:
        # Get user input
        user_input = input("🎯 Your vibe: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("👋 Goodbye!")
            break
            
        if not user_input:
            continue
            
        print("🔄 Generating code...")
        
        try:
            # Enhanced prompt for better code generation
            enhanced_prompt = f"""
            You are Lovable AI - an expert full-stack developer. Generate clean, modern React code with Tailwind CSS.
            
            USER REQUEST: {user_input}
            
            REQUIREMENTS:
            - Return complete, runnable React components
            - Use TypeScript for type safety  
            - Implement responsive design with Tailwind CSS
            - Include proper error handling
            - Add accessibility features
            - Export components properly
            - Make it production-ready
            
            Generate the code:
            """
            
            messages = [{"role": "user", "content": enhanced_prompt}]
            text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
            model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
            
            # Generate with appropriate settings for Termux
            generated_ids = model.generate(
                **model_inputs,
                max_new_tokens=512,
                temperature=0.7,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id
            )
            
            response = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
            
            # Extract just the code part if it's in markdown blocks
            if "```" in response:
                # Extract code from markdown code blocks
                import re
                code_blocks = re.findall(r'```(?:jsx|javascript|typescript)?\n(.*?)```', response, re.DOTALL)
                if code_blocks:
                    response = code_blocks[0].strip()
            
            print("\n💻 Generated Code:")
            print("═" * 50)
            print(response)
            print("═" * 50)
            print()
            
        except Exception as e:
            print(f"❌ Generation error: {e}")
            
except Exception as e:
    print(f"❌ Model loading failed: {e}")
    print("\n💡 Troubleshooting tips:")
    print("1. Run: pip install transformers torch accelerate")
    print("2. Check internet connection for first-time download")
    print("3. Ensure you have at least 2GB free storage")
    print("4. If memory error, try closing other apps")
