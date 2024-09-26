from transformers import pipeline

# Load pre-trained emotion classification model
emotion_classifier = pipeline('text-classification', model='bhadresh-savani/distilbert-base-uncased-emotion')

def detect_emotion(text):
    emotions = emotion_classifier(text)
    return emotions[0]['label'], emotions[0]['score']
