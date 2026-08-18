from flask import Flask, jsonify, request
from google.auth.transport import requests
from google.oauth2 import id_token
import os

app = Flask(__name__)

# These are the service accounts allowed to call this API
AUTHORIZED_ACCOUNTS = [
    "authorized-service@cloud-portfolio-789.iam.gserviceaccount.com",
]

@app.route('/api/secret', methods=['GET'])
def get_secret():
    """Protected endpoint - only authorized services can access."""

    # Get the Authorization header
    auth_header = request.headers.get('Authorization')

    if not auth_header:
        return jsonify({'error': 'Missing authorization header'}), 401

    try:
        # Extract the token
        token = auth_header.split(' ')[1]

        # Verify the token (signed by Google)
        request_obj = requests.Request()
        claims = id_token.verify_oauth2_token(token, request_obj)

        # Get the service account email from the token
        service_account = claims.get('email')

        print(f"[Protected API] Request from: {service_account}")

        # Check if authorized
        if service_account not in AUTHORIZED_ACCOUNTS:
            print(f"[Protected API] DENIED: {service_account} not in whitelist")
            return jsonify({
                'error': 'Unauthorized',
                'service_account': service_account
            }), 403

        # Authorized - return secret data
        print(f"[Protected API] ALLOWED: {service_account}")
        return jsonify({
            'secret': 'This is sensitive data - payment processing rules',
            'authorized_by': service_account,
            'access': 'GRANTED'
        }), 200

    except Exception as e:
        print(f"[Protected API] Error: {e}")
        return jsonify({'error': 'Invalid token'}), 401

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'service': 'protected-api'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
