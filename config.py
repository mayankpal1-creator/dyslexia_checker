# DyslexiaCheck Configuration

# Flask Configuration
SECRET_KEY = 'your-secret-key-change-this-in-production'
DEBUG = True
TESTING = False

# Database Configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///dyslexia.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Upload Configuration
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file upload
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'wav', 'mp3'}

# Session Configuration
PERMANENT_SESSION_LIFETIME = 3600  # 1 hour

# Application Settings
APP_NAME = 'DyslexiaCheck'
APP_DESCRIPTION = 'Early Detection and Support Platform for Dyslexia'
