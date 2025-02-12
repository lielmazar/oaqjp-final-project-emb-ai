"""
Small flask application for detecing emotions from text
"""
from flask import Flask, render_template, request
import EmotionDetection

app = Flask("myApp")

@app.route("/")
def home():
    '''
    home route
    '''
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector():
    '''
    emotion detection route
    '''
    txt = request.args["textToAnalyze"]
    detected_emotions = EmotionDetection.emotion_detection.emotion_detector(txt)
    if detected_emotions['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    formatted_response = f"""
    For the given statement, 
    the system response is 'anger': {detected_emotions['anger']}, 
    'disgust': {detected_emotions['disgust']}, 'fear': {detected_emotions['fear']}, 
    'joy': {detected_emotions['joy']} and 'sadness': {detected_emotions['sadness']}. 
    The dominant emotion is {detected_emotions['dominant_emotion']}."""
    return formatted_response

if __name__ == "__main__":
    app.run(debug = True)
