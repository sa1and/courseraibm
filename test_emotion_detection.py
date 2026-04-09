"""
Unit tests for the emotion_detector function in the EmotionDetection package.

Tests verify that the dominant emotion returned for known phrases
matches the expected emotion classifications.
Uses unittest.mock to patch the Watson NLP API for local testing.
"""

import unittest
from unittest.mock import patch, MagicMock
import json
from EmotionDetection.emotion_detection import emotion_detector


def make_mock_response(emotions_dict, status_code=200):
    """Helper to build a mock requests.Response object."""
    mock_response = MagicMock()
    mock_response.status_code = status_code
    response_body = {
        "emotionPredictions": [
            {
                "emotion": emotions_dict
            }
        ]
    }
    mock_response.text = json.dumps(response_body)
    return mock_response


class TestEmotionDetector(unittest.TestCase):
    """Test cases for the emotion_detector function."""

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_joy_for_joy_statement(self, mock_post):
        """Test that a joyful statement returns 'joy' as dominant emotion."""
        mock_post.return_value = make_mock_response({
            'anger': 0.006, 'disgust': 0.002, 'fear': 0.009,
            'joy': 0.965, 'sadness': 0.013
        })
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_anger_for_anger_statement(self, mock_post):
        """Test that an angry statement returns 'anger' as dominant emotion."""
        mock_post.return_value = make_mock_response({
            'anger': 0.852, 'disgust': 0.141, 'fear': 0.073,
            'joy': 0.007, 'sadness': 0.064
        })
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_disgust_for_disgust_statement(self, mock_post):
        """Test that a disgusting statement returns 'disgust' as dominant emotion."""
        mock_post.return_value = make_mock_response({
            'anger': 0.074, 'disgust': 0.834, 'fear': 0.043,
            'joy': 0.005, 'sadness': 0.122
        })
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_fear_for_fear_statement(self, mock_post):
        """Test that a fearful statement returns 'fear' as dominant emotion."""
        mock_post.return_value = make_mock_response({
            'anger': 0.043, 'disgust': 0.012, 'fear': 0.897,
            'joy': 0.006, 'sadness': 0.098
        })
        result = emotion_detector("I am scared to death by this")
        self.assertEqual(result['dominant_emotion'], 'fear')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_sadness_for_sad_statement(self, mock_post):
        """Test that a sad statement returns 'sadness' as dominant emotion."""
        mock_post.return_value = make_mock_response({
            'anger': 0.034, 'disgust': 0.018, 'fear': 0.029,
            'joy': 0.007, 'sadness': 0.921
        })
        result = emotion_detector("I feel so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_blank_input_returns_none(self):
        """Test that blank input returns None for all emotion scores."""
        result = emotion_detector("")
        self.assertIsNone(result['dominant_emotion'])
        self.assertIsNone(result['anger'])
        self.assertIsNone(result['disgust'])
        self.assertIsNone(result['fear'])
        self.assertIsNone(result['joy'])
        self.assertIsNone(result['sadness'])

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_status_400_returns_none(self, mock_post):
        """Test that a 400 API response returns None for all emotion scores."""
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_post.return_value = mock_response
        result = emotion_detector("some invalid input")
        self.assertIsNone(result['dominant_emotion'])


if __name__ == '__main__':
    unittest.main()
