# Emotion Detection Application

## Project Overview

A web application for **Emotion Detection** built using the **Watson NLP Embedded Library** and **Flask**. This project is part of the IBM AI Application Development Certification final project.

The application analyses user-provided text and detects the following emotions:
- **Anger**
- **Disgust**
- **Fear**
- **Joy**
- **Sadness**

It returns each emotion's confidence score and identifies the **dominant emotion**.

---

## Project Structure

```
oaqjp-final-project-emb-ai/
├── EmotionDetection/
│   ├── __init__.py              # Package initializer
│   └── emotion_detection.py    # Core emotion detection logic
├── static/
│   └── mywebscript.js          # Frontend JavaScript
├── templates/
│   └── index.html              # Main HTML page
├── server.py                   # Flask web server
├── test_emotion_detection.py   # Unit tests
└── README.md                   # This file
```

---

## Technologies Used

- **Python 3.x**
- **Flask** – Web framework
- **Requests** – HTTP library for API calls
- **Watson NLP Embedded Library** – Emotion prediction API
- **Pylint** – Static code analysis
- **Unittest** – Python unit testing framework

---

## Setup & Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/oaqjp-final-project-emb-ai.git
   cd oaqjp-final-project-emb-ai
   ```

2. Install dependencies:
   ```bash
   pip install flask requests pylint
   ```

3. Run the Flask application:
   ```bash
   python server.py
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

---

## Usage

Enter any text into the text box and click **"Run Sentiment Analysis"**. The application will display:

- Scores for all five emotions (anger, disgust, fear, joy, sadness)
- The **dominant emotion** highlighted in bold

### Example

**Input:** `"I am so happy today!"`

**Output:** `For the given statement, the system response is 'anger': 0.006, 'disgust': 0.002, 'fear': 0.009, 'joy': 0.97 and 'sadness': 0.013. The dominant emotion is **joy**.`

---

## Running Unit Tests

```bash
python -m unittest test_emotion_detection.py -v
```

---

## Static Code Analysis

```bash
pylint server.py
```

---

## API Reference

This application uses the Watson NLP Emotion Predict API:

- **Endpoint:** `https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict`
- **Method:** POST
- **Header:** `grpc-metadata-mm-model-id: emotion_aggregated-workflow_lang_en_stock`
- **Body:**
  ```json
  {
    "raw_document": {
      "text": "Your text here"
    }
  }
  ```

---

## Error Handling

- **Blank input:** Returns `"Invalid text! Please try again!"`
- **API status 400:** Returns `None` for all emotion scores and dominant emotion

---

## License

This project is submitted as part of the IBM AI Developer Professional Certificate final project assessment.
