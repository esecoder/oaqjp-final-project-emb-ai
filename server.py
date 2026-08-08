from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector/<textToAnalyze>", methods=["GET", "POST"])
def emo_detector(textToAnalyze):
    result = emotion_detector(textToAnalyze)
    return 'For the given statement, the system response is \'anger\':' 
    + result['anger'] + ', \'disgust\':' 
    + result['disgust'] + ', \'fear\':'
    + result['fear'] + ', \'joy\':'
    + result['joy'] + 'and \'sadness\':'
    + result['sadness'] + '. The dominant emotion is ' + result['dominant_emotion']

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)