#!/usr/bin/env python
"""
DyslexiaCheck - Web Application for Dyslexia Detection and Support
Run this file to start the Flask application
"""

import os
import sys
from app import create_app

# Create Flask app
app = create_app()

if __name__ == '__main__':
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                     DYSLEXIACHECK                            ║
    ║         Early Detection & Support Platform                   ║
    ╚══════════════════════════════════════════════════════════════╝
    
    Starting the application...
    """)
    
    # Run the app
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
