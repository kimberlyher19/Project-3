from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import pandas as pd
from bson import ObjectId  # Import ObjectId to handle it explicitly

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# MongoDB connection
mongo = MongoClient(port=27017)
spotify_db = mongo['SpotifyDataset']
songs = spotify_db['SpotifySongs']

# Convert ObjectId to string helper function
def object_id_to_str(data):
    if isinstance(data, ObjectId):
        return str(data)
    if isinstance(data, dict):
        return {k: object_id_to_str(v) for k, v in data.items()}
    if isinstance(data, list):
        return [object_id_to_str(item) for item in data]
    return data

# Route 1: Top 10 Artists by Song Count
@app.route('/top_artists', methods=['GET'])
def top_artists():
    try:
        pipeline = [
            {"$group": {"_id": "$artist", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 10}
        ]
        results = list(songs.aggregate(pipeline))
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route 2: Rihanna's Popularity
@app.route('/rihanna_songs', methods=['GET'])
def rihanna_songs():
    try:
        pipeline = [
            {"$match": {"artist": "rihanna"}},
            {"$project": {"song": 1, "popularity": 1}},
            {"$sort": {"popularity": -1}}
        ]
        results = list(songs.aggregate(pipeline))

        # Convert ObjectId to string
        results = object_id_to_str(results)

        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route 3: Danceability vs Energy
@app.route('/danceability_energy', methods=['GET'])
def danceability_energy():
    try:
        fields = {'danceability': 1, 'energy': 1, '_id': 0}
        data = list(songs.find({}, fields))
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route 4: Characteristics of Popular Songs
@app.route('/popular_songs', methods=['GET'])
def popular_songs():
    try:
        cursor = songs.find()
        df = pd.DataFrame(list(cursor))  # Ensure pandas is imported

        top_10_percent = df['popularity'].quantile(0.9)
        bottom_10_percent = df['popularity'].quantile(0.1)

        top_songs = df[df['popularity'] >= top_10_percent]
        bottom_songs = df[df['popularity'] <= bottom_10_percent]

        result = {
            "top_songs": top_songs[['loudness', 'valence', 'song', 'popularity']].to_dict(orient='records'),
            "bottom_songs": bottom_songs[['loudness', 'valence', 'song', 'popularity']].to_dict(orient='records')
        }

        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
