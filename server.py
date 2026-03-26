""" 
This module receives input from users and calls emotion_detector function to analyze the input and 
lastly returns the response back to the user

"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def render_index_page():
    """Render the index.html page"""
    return render_template('index.html')


@app.route('/emotionDetector')
def emotion_detect():
    """Send request to emotion_detector function and get a response back"""
    # Retrieve the text to analyze from the request arguments
    text = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text)

    # Check if the dominant_emotion is None, indicating an error or invalid input if it is None
    if response['dominant_emotion'] is None:
        return {'message':'Invalid text! Please try again'}
    # If the dominant_emotion is not None, extract emotions and dominant emotion from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    output = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. The dominant emotion is "
        f"{dominant_emotion}."
    )
    return output

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
