# Basic resource recommendations
resources = {
    "anger": "Here's a guide to managing anger: [link to resource]",
    "sadness": "You might find this article on coping with sadness helpful: [link to resource]",
    "joy": "It's great to feel joyful! Check out this mindfulness exercise: [link to resource]",
    "fear": "Here are some relaxation techniques: [link to resource]",
    "surprise": "Here's something to help stay grounded: [link to resource]",
    "disgust": "Here's how to navigate feelings of disgust: [link to resource]",
}

def recommend_resource(emotion):
    return resources.get(emotion.lower(), "Sorry, no resources for this emotion right now.")
