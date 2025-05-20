from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotional Damage");

@app.route('/')
def Home():
    return render_template("index.html")

@app.route('/emotionDetector')
def emotionDetector():
    text_to_analyze = request.args.get('textToAnalyze')
    main_response = emotion_detector(text_to_analyze)
    dominant_emotion = main_response['dominant_emotion']
    # main_response.del('dominant_emotion')

    result_text = f"For the given statement, the system response is {main_response}. The dominant emotion is {dominant_emotion}"

    return result_text 

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
