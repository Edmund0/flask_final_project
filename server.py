"""This module does such and such."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotional Damage")

@app.route('/')
def home():
    '''Demonstrates triple double quotes
    docstrings and does nothing really.'''
    return render_template("index.html")

@app.route('/emotionDetector')
def emotion_detection():
    '''Demonstrates triple double quotes
    docstrings and does nothing really.'''
    text_to_analyze = request.args.get('textToAnalyze')
    main_response = emotion_detector(text_to_analyze)

    if main_response['dominant_emotion'] is None:
        result_text = "Invalid text! Please try again!"
    else:
        dominant_emotion = main_response['dominant_emotion']
        result_text_1 = f"For the given statement, the system response is {main_response}."
        result_text = result_text_1 + f" The dominant emotion is {dominant_emotion}"
    return result_text

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
