from flask import Flask, request, jsonify
from Data import Data

def fetch_data(link):
    data = Data(link)
    response = data.video_link_check()
    if not data.message:
        return jsonify(data.data)
    else:
        return jsonify(data.message)
app = Flask(__name__)


@app.route("/", methods=["POST"])
def main():
    try:
        if request.method == "POST":
            if request.is_json:
                try:
                    data = request.get_json()
                    if 'link' not in data:
                        return jsonify({"error": "'link' key is missing in the JSON data"}), 400
                    else:
                        return fetch_data(data['link'])
                except Exception as e:
                    return jsonify({"error": str(e)}), 400  # Return a 400 status for bad requests
            else:
                return jsonify({"error": "Request must contain JSON data"}), 400
        else:
            return jsonify(
                {"error": "Only POST requests are allowed"}), 405  # Return a 405 status for method not allowed
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
