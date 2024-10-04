from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

# Route for Tata Play channels
@app.route('/sun')
def get_tata_channels():
    try:
        response = requests.post(
            "https://babel-in.xyz/sunnxt",
            json={"X-API-Key": "babel-23003cca3ba04020bade44a193"},
            headers={"User-Agent": "Babel/5.0"}
        )
        return jsonify(response.json())  # Return the JSON response
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route for Tata Play HMAC
@app.route('/tata/hmac', methods=['GET'])  # Allow GET requests
def get_tata_hmac():
    # Get the 'channel_id' from query parameters
    channel_id = request.args.get("id")
    if not channel_id:
        return jsonify({'error': 'Channel ID is required'}), 400

    # Validate if 'channel_id' is a valid integer
    try:
        channel_id = int(channel_id)
    except ValueError:
        return jsonify({'error': 'Invalid Channel ID format. Must be an integer.'}), 400

    url = 'https://babel-in.xyz/tata/hmac'

    # Set headers for the API request
    headers = {
        'User-Agent': 'Babel/5.0'
    }

    # Data payload for the request
    data_payload = {
        'X-API-Key': "babel-23003cca3ba04020bade44a193X",
        'X-Channel-ID': str(channel_id),  # Use the dynamic Channel ID from query parameters
        'X-auth-token': "yDrEFGmOzB8Nrzt8QZDQRgrh0PmA9Ri0",  # Constant Auth Token
        'X-sub-ID': "1293097877",  # Constant Subscriber ID
    }

    try:
        # Send POST request with the specified headers and payload
        response = requests.post(url, headers=headers, json=data_payload)
        
        # Check for a successful response
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': f'Error: {response.status_code}', 'message': response.text}), response.status_code

    except requests.exceptions.RequestException as req_err:
        return jsonify({"error": f"Request error: {req_err}"}), 500
    except Exception as e:
        return jsonify({"error": f"Internal server error: {e}"}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Default port 10000 or environment port
    app.run(host='0.0.0.0', port=port)
    
