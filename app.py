from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({'status': 'healthy', 'version': '1.0.0'})

@app.route('/api/message', methods=['GET'])
def message():
    """Return a message."""
    return jsonify({
        'message': 'This pipeline was deployed by GitHub Actions!',
        'environment': 'production'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
