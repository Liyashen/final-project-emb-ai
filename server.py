from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def render_index_page():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotionDetector():
    text = request.args.get('textToAnalyze')
    response = emotion_detector(text)
    if response['dominant_emotion'] is None:
        return {'message':'Invalid text! Please try again'}
        
    
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
