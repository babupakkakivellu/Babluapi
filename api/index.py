from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

# Route for Tata Play channels
@app.route('/sun')
def get_tata_channels():
    try:
        response = requests.post(
            "https://babel-in.xyz/jplus/channels",
            json={"X-API-Key": "babel-23003cca3ba04020bade44a193"},
            headers={"User-Agent": "Babel/5.0"}
        )
        return jsonify(response.json())  # Return the JSON response
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/key', methods=['POST'])
def get_key():
    url = 'https://babel-in.xyz/jplus/key'
    data = {
        'X-API-Key': 'babel-23003cca3ba04020bade44a193',  # Replace with your actual API key
        'X-Channel-ID': '558'   # Replace with actual channel ID
    }

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Babel/5.0'
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return jsonify(response.json())  # Return the JSON response
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Default port 10000 or environment port
    app.run(host='0.0.0.0', port=port)
    
