''' Executing this function initiates the application of emotional
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

# Import the sentiment_analyzer function from the package created
app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def emotion_analyser():
    ''' This code receives the text from the HTML interface and 
        runs emotional detection over it using emotion_detector()
        function. The output returns a dict of emotions and the dominant emotion.
    '''
    text_to_analyse = request.args.get('textToAnalyze')
    results_of_analysis = emotion_detector(text_to_analyse)

    if results_of_analysis['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    return f"For the given statement, the system response is\
     'anger': {results_of_analysis['anger']}, 'disgust': {results_of_analysis['disgust']},\
      'fear': {results_of_analysis['fear']}, 'joy': {results_of_analysis['joy']}\
       and 'sadness': {results_of_analysis['sadness']}.\
        The dominant emotion is {results_of_analysis['dominant_emotion']}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5000)
