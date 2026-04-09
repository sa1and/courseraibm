import unittest
from unittest.mock import patch, MagicMock
import json
from EmotionDetection.emotion_detection import emotion_detector

class MockTest(unittest.TestCase):
    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_import_and_run(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = json.dumps({
            "emotionPredictions": [{"emotion": {'anger': 0.1, 'disgust': 0.1, 'fear': 0.1, 'joy': 0.6, 'sadness': 0.1}}]
        })
        mock_post.return_value = mock_response
        
        result = emotion_detector("I am happy")
        print(f"\nResult: {result}")
        assert result['dominant_emotion'] == 'joy'
        print("Test passed without errors!")

if __name__ == '__main__':
    unittest.main()
