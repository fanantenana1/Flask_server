from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connexion à MongoDB
client = MongoClient("mongodb+srv://haaahiii:1234@cluster1.wmj7n.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1")
db = client['Data_ko']
collection = db['Data_collectio_nama']

@app.route('/insert', methods=['POST'])
def insert_data():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    result = collection.insert_one(data)
    return jsonify({"message": "Document inserted", "id": str(result.inserted_id)}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
