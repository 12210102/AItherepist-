from flask import Flask, request, jsonify
from waitress import serve
from emotion_detector import detect_emotion
from response_generator import generate_therapist_response
from recommender import recommend_resource
from crisis_manager import check_for_crisis

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    
    # Detect emotion
    emotion, confidence = detect_emotion(user_input)
    
    # Generate therapist response
    therapist_reply = generate_therapist_response(user_input)
    
    # Recommend resource
    resource = recommend_resource(emotion)
    
    response = {
        "emotion": emotion,
        "therapist_response": therapist_reply,
        "recommended_resource": resource
    }
    return jsonify(response)

if __name__ == "__main__":
    serve(app,host="0.0.0.0",port=8000)
