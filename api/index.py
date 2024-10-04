from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

# Route for Tata Play channels
@app.route('/jcinema')
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

# Route for Tata Play channels
@app.route('/jckeys', methods=['POST'])
def get_tata_channels():
    try:
        # Prepare data for the request
        data = {
            'X-API-Key': 'babel-23003cca3ba04020bade44a193',  # Replace with actual API key
            'X-Channel-ID': '{channelID}',  # Replace with actual Channel ID
        }
        # Make the POST request
        response = requests.post(
            "https://babel-in.xyz/jplus/key",
            json=data,
            headers={"Content-Type": "application/json", "User-Agent": "Babel/5.0"}
        )
        
        # Check if the response was successful
        if response.status_code != 200:
            return jsonify({"error": "Error sending request"}), response.status_code
        
        # Return the JSON response
        return jsonify(response.json())
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Default port 10000 or environment port
    app.run(host='0.0.0.0', port=port)
    
