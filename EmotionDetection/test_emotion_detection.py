import unittest
from emotion_detection import emotion_detector as ed

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        result = ed('I am glad this happened')['dominant_emotion']
        self.assertEqual(result, 'joy')
        result = ed('I am really mad about this')['dominant_emotion']
        self.assertEqual(result, 'anger')
        result = ed('I feel disgusted just hearing about this')['dominant_emotion']
        self.assertEqual(result, 'disgust')
        result = ed('I am so sad about this')['dominant_emotion']
        self.assertEqual(result, 'sadness')
        result = ed('I am really afraid that this will happen')['dominant_emotion']
        self.assertEqual(result, 'fear')

if __name__ == '__main__':
    unittest.main()