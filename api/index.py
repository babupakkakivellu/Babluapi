from flask import Flask, jsonify, request
import requests
import json
import os

app = Flask(__name__)

# Route for the first API request (/tata/channels)
@app.route('/tata/channels')
def get_tata_channels():
    try:
        response = requests.post(
            "https://babel-in.xyz/tata/channels",
            json={"X-API-Key": "babel-23003cca3ba04020bade44a193"},
            headers={"User-Agent": "Babel/5.0"}
        )
        return jsonify(response.json())  # Return the JSON response
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route for the second API request (/tata/hmac)

BABLU_KEY = "babel-23003cca3ba04020bade44a193X"
TATAPLAY_AUTH_TOKEN = "yDrEFGmOzB8Nrzt8QZDQRgrh0PmA9Ri0"
TATAPLAY_SUBSCRIBER_ID = "1293097877"
TATAPLAY_SUBSCRIBER_NAME = "Mahesh Raut"

# Route for the HMAC API request
@app.route('/tata/hmac', methods=['GET', 'POST'])  # Allow both GET and POST requests
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
        'X-API-Key': BABLU_KEY,
        'X-Channel-ID': str(channel_id),  # Use the dynamic Channel ID from query parameters
        'X-auth-token': TATAPLAY_AUTH_TOKEN,  # Constant Auth Token
        'X-sub-ID': TATAPLAY_SUBSCRIBER_ID,  # Constant Subscriber ID
    }
    try:
        # Send POST request with the specified headers and payload
        response = requests.post(url, headers=headers, json=data_payload)
        
        # Check for a successful response
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            # Handle non-200 status codes
            return jsonify({'error': f'Error: {response.status_code}', 'message': response.text}), response.status_code

    except requests.exceptions.RequestException as req_err:
        return jsonify({"error": f"Request error: {req_err}"}), 500
    except Exception as e:
        return jsonify({"error": f"Internal server error: {e}"}), 500
 
# Route for the third API request (/jplus/key)
@app.route('/jplus/key')
def get_jplus_key():
    # Get 'id' from query parameters
    channel_id = request.args.get('id')

    # Check if 'id' is provided
    if not channel_id:
        return jsonify({'error': 'Channel ID is required'}), 400
    
    # Optional: Validate if 'id' is a valid integer
    try:
        channel_id = int(channel_id)
    except ValueError:
        return jsonify({'error': 'Invalid Channel ID format. Must be an integer.'}), 400

    url = 'https://babel-in.xyz/jplus/key'

    # Use the provided 'id' in the request payload
    data = {
        'X-API-Key': 'babelXXX',
        'X-Channel-ID': str(channel_id)  # Dynamically insert the channel ID
    }

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Babel/5.0'
    }

    try:
        # Send POST request with dynamic channel ID
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': f'Error: {response.status_code}', 'message': response.text}), response.status_code
    except Exception as e:
        return jsonify({'error': f'Error sending request: {e}'}), 500


# Route for the fourth API request (/jplus/channels)
@app.route('/jplus/channels')
def get_jplus_channels():
    url = 'https://babel-in.xyz/jplus/channels'

    data = {
        'X-API-Key': 'babel,
        'X-Channel-ID': 'your_channel_id'  # Replace with actual value
    }

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Babel/5.0'
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': f'Error: {response.status_code}', 'message': response.text}), response.status_code
    except Exception as e:
        return jsonify({'error': f'Error sending request: {e}'}), 500


# Route for the fifth API request (/tata/sliv)
@app.route('/tata/sliv')
def get_tata_sliv():
    url = 'https://babel-in.xyz/tata/sliv'

    data = {
        'X-API-Key': 'babel-'
    }

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Babel/5.0'
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': f'Error: {response.status_code}', 'message': response.text}), response.status_code
    except Exception as e:
        return jsonify({'error': f'Error sending request: {e}'}), 500


# Route for the sixth API request (/zee5)
@app.route('/zee5')
def get_zee5_data():
    url = 'https://babel-in.xyz/zee5'

    data = {
        'X-API-Key': 'babel'
    }

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Babel/5.0'
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': f'Error: {response.status_code}', 'message': response.text}), response.status_code
    except Exception as e:
        return jsonify({'error': f'Error sending request: {e}'}), 500


# Route for the seventh API request (/samsung)
@app.route('/samsung')
def get_samsung_data():
    url = 'https://babel-in.xyz/samsung'

    data = {
        'X-API-Key': 'babel-'
    }

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Babel/5.0'
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': f'Error: {response.status_code}', 'message': response.text}), response.status_code
    except Exception as e:
        return jsonify({'error': f'Error sending request: {e}'}), 500


# Route for the eighth API request (/akashgo)
@app.route('/akashgo')
def get_akashgo_data():
    url = 'https://babel-in.xyz/akashgo'

    data = {
        'X-API-Key': 'babel-'
    }

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Babel/5.0'
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': f'Error: {response.status_code}', 'message': response.text}), response.status_code
    except Exception as e:
        return jsonify({'error': f'Error sending request: {e}'}), 500


# Route for the /tata/key API request
@app.route('/tata/key')
def get_tata_key():
    channel_id = request.args.get('id')
    if not channel_id:
        return jsonify({'error': 'Channel ID is required'}), 400

    try:
        channel_id = int(channel_id)
    except ValueError:
        return jsonify({'error': 'Invalid Channel ID format. Must be an integer.'}), 400

    url = 'https://babel-in.xyz/tata/key'
    headers = {
        'User-Agent': 'Babel/5.0',
        'Content-Type': 'application/json'
    }
    data = {
        'X-API-Key': 'babel-',
        'X-Channel-ID': channel_id
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': f'Error: {response.status_code}', 'message': response.text}), response.status_code

    except Exception as e:
        return jsonify({'error': f'Error sending request for channel ID {channel_id}: {e}'}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
  
