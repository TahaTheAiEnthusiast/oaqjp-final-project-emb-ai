
"""Flask application for detecting emotions in user-provided text."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector


app = Flask(__name__)


@app.route("/")
def home():
    """Render the home page of the emotion detection application."""
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    """Analyze user input and return the emotion detection results."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, "
        f"'disgust': {disgust}, "
        f"'fear': {fear}, "
        f"'joy': {joy} and "
        f"'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
