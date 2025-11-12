from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
from config import get_config

# Initialize Flask app
app = Flask(__name__)

# Load configuration
config = get_config()
app.config.from_object(config)

# Setup CORS
CORS(app, origins=config.ALLOWED_ORIGINS)

class CloudLovableAI:
    def __init__(self):
        self.api_key = config.BYTEZ_API_KEY
        self.base_url = config.BYTEZ_API_URL
        self.available_models = config.AVAILABLE_MODELS
        self.current_model = config.DEFAULT_MODEL
    
    def generate_code(self, prompt, model=None):
        if not model:
            model = self.current_model
        
        system_prompt = config.SYSTEM_PROMPT
        full_prompt = f"User Request: {prompt}"
        
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": full_prompt}
            ],
            "temperature": config.TEMPERATURE,
            "max_tokens": config.MAX_TOKENS
        }
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(self.base_url, json=payload, headers=headers, timeout=config.TIMEOUT)
            
            if response.status_code == 200:
                data = response.json()
                generated_code = data["choices"][0]["message"]["content"]
                
                return {
                    'success': True,
                    'code': generated_code,
                    'model': model,
                    'enhancements': ['type_safety', 'responsive', 'accessible', 'production_ready']
                }
            else:
                return {
                    'success': False,
                    'error': f"API Error: {response.status_code} - {response.text}"
                }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

# Initialize AI
lovable_ai = CloudLovableAI()

@app.route('/')
def home():
    return jsonify({
        'message': '🚀 Lovable AI Backend is running!',
        'version': '1.0.0',
        'environment': os.getenv('FLASK_ENV', 'development'),
        'endpoints': {
            '/api/health': 'GET - Health check',
            '/api/models': 'GET - List available models',
            '/api/generate': 'POST - Generate code'
        },
        'status': 'active'
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'models': lovable_ai.available_models,
        'current_model': lovable_ai.current_model,
        'environment': os.getenv('FLASK_ENV', 'development'),
        'service': 'lovable-ai-cloud-backend'
    })

@app.route('/api/generate', methods=['POST'])
def generate_code():
    data = request.json
    prompt = data.get('prompt', '')
    model = data.get('model', lovable_ai.current_model)
    
    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400
    
    result = lovable_ai.generate_code(prompt, model)
    return jsonify(result)

@app.route('/api/models', methods=['GET'])
def get_models():
    return jsonify({
        'models': lovable_ai.available_models,
        'current': lovable_ai.current_model
    })

@app.route('/api/models/switch', methods=['POST'])
def switch_model():
    data = request.json
    model = data.get('model')
    
    if model in lovable_ai.available_models:
        lovable_ai.current_model = model
        return jsonify({'success': True, 'message': f'Switched to {model}'})
    else:
        return jsonify({'error': 'Model not available'}), 400

if __name__ == '__main__':
    print(f"🚀 Starting Lovable AI Backend in {config.__class__.__name__} mode...")
    print(f"📍 Server running on {config.HOST}:{config.PORT}")
    print(f"🔧 Debug mode: {config.DEBUG}")
    print(f"🌐 Allowed origins: {config.ALLOWED_ORIGINS}")
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
