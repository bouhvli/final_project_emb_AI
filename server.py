from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def emotion_analyser():
    text_to_analyse = request.args.get('textToAnalyze')
    results_of_analysis = emotion_detector(text_to_analyse)
    if results_of_analysis is None:
        return "Invalid input! Try again."
    return f"For the given statement, the system response is\
     'anger': {results_of_analysis['anger']}, 'disgust': {results_of_analysis['disgust']},\
      'fear': {results_of_analysis['fear']}, 'joy': {results_of_analysis['joy']}\
       and 'sadness': {results_of_analysis['sadness']}.\
        The dominant emotion is {results_of_analysis['dominant_emotion']}."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5000)