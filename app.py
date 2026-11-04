import os
import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
DB_FILE = "database.json"

def load_db():
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            pass
    return {
        "users": { "santosh123kumar": { "pass": "santosh123kumar", "balance": 20000.00 } },
        "settings": {
            "qrUrl": "https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=UPI://Pay?pa=cardingweb@okaxis&pn=CardingWeb",
            "bannerImg": "https://images.unsplash.com/photo-1639762681485-074b7f938ba0?q=80&w=1000&auto=format&fit=crop",
            "bannerLink": ""
        },
        "banks": ["SBI", "HDFC", "ICICI", "AXIS"],
        "cards": [
            { "id": 1, "category": "HDFC", "tier": "PLATINUM", "name": "INFINIA VIP", "number": "4532889145328891", "expiry": "12/28", "cvv": "389", "limit": "₹5,00,000", "price": 500, "holder": "SANTOSH KUMAR", "bgImg": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=800&auto=format&fit=crop" }
        ],
        "unlocked": {}
    }

def save_db(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/get_data', methods=['GET'])
def get_data():
    return jsonify(load_db())

@app.route('/api/save_data', methods=['POST'])
def save_data():
    req = request.json
    if req:
        save_db(req)
        return jsonify({"status": "success"})
    return jsonify({"status": "error"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
