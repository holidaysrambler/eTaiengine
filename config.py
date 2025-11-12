import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Base configuration class with environment variables"""
    
    # API Configuration
    BYTEZ_API_KEY = os.getenv('BYTEZ_API_KEY', 'your_bytez_api_key_here')
    BYTEZ_API_URL = os.getenv('BYTEZ_API_URL', 'https://api.bytez.com/v1/chat/completions')
    
    # Model Configuration
    AVAILABLE_MODELS = os.getenv('AVAILABLE_MODELS', 'qwen-coder,claude-instant,gpt-4').split(',')
    DEFAULT_MODEL = os.getenv('DEFAULT_MODEL', 'qwen-coder')
    
    # Server Configuration
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', '5001'))
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    
    # CORS Configuration
    ALLOWED_ORIGINS = os.getenv('ALLOWED_ORIGINS', 'https://etai-builder.netlify.app,http://localhost:3000,https://localhost:3000').split(',')
    
    # AI Generation Settings
    MAX_TOKENS = int(os.getenv('MAX_TOKENS', '2000'))
    TEMPERATURE = float(os.getenv('TEMPERATURE', '0.7'))
    TIMEOUT = int(os.getenv('TIMEOUT', '30'))
    
    # System Prompts
    SYSTEM_PROMPT = os.getenv('SYSTEM_PROMPT', """
    You are Lovable AI - an expert full-stack developer specializing in React, Next.js, and Tailwind CSS.
    
    VIBE CODING RULES:
    1. Generate COMPLETE, RUNNABLE React components
    2. Use TypeScript for type safety
    3. Implement responsive design with Tailwind CSS
    4. Include proper error handling and accessibility
    5. Use modern React hooks and patterns
    6. Export components properly
    7. Add realistic mock data when needed
    8. Include smooth animations and transitions
    9. Make it production-ready
    
    Always return clean, well-structured code that can be directly used in production.
    Return only the code without explanations.
    """)

class DevelopmentConfig(Config):
    """Development specific configuration"""
    DEBUG = True
    ALLOWED_ORIGINS = ['http://localhost:3000', 'https://localhost:3000', 'http://127.0.0.1:3000']

class ProductionConfig(Config):
    """Production specific configuration"""
    DEBUG = False
    ALLOWED_ORIGINS = ['https://etai-builder.netlify.app']

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

def get_config():
    """Get configuration based on environment"""
    env = os.getenv('FLASK_ENV', 'development')
    return config.get(env, config['default'])
