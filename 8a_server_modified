"""
Flask web server for the Emotion Detection application.

Exposes the /emotionDetector route which accepts text input via GET request,
analyses the emotions using the EmotionDetection package, and returns
a formatted response to the user.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyses the emotion of the given text using the emotion_detector function.

    Reads the 'textToAnalyse' query parameter from the GET request,
    calls the emotion_detector function, and returns a formatted string
    with the emotion scores and dominant emotion.

    Returns:
        str: A formatted response string with emotion analysis results,
             or an error message for blank input.
    """
    text_to_analyse = request.args.get('textToAnalyse')

    result = emotion_detector(text_to_analyse)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant_emotion = result['dominant_emotion']

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )


@app.route("/")
def render_index_page():
    """Renders the main index page of the application."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
