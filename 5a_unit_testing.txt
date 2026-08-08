from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):

    def test_emotional_detector_joy(self):
        text = "I am glad this happened"
        result = emotion_detector(text)

        self.assertIn("dominant_emotion", result)
        self.assertEqual(result["dominant_emotion"], "joy")
        print("--> Test 1 Passed!")

    def test_emotional_detector_anger(self):
        text = "I am really mad about this"
        result = emotion_detector(text)

        self.assertIn("dominant_emotion", result)
        self.assertEqual(result["dominant_emotion"], "anger")
        print("--> Test 2 Passed!")

    def test_emotional_detector_disgust(self):
        text = "I feel disgusted just hearing about this"
        result = emotion_detector(text)

        self.assertIn("dominant_emotion", result)
        self.assertEqual(result["dominant_emotion"], "disgust")
        print("--> Test 3 Passed!")

    def test_emotional_detector_sadness(self):
        text = "I am so sad about this"
        result = emotion_detector(text)

        self.assertIn("dominant_emotion", result)
        self.assertEqual(result["dominant_emotion"], "sadness")
        print("--> Test 4 Passed!")

    def test_emotional_detector_fear(self):
        text = "I am really afraid that this will happen"
        result = emotion_detector(text)

        self.assertIn("dominant_emotion", result)
        self.assertEqual(result["dominant_emotion"], "fear")
        print("--> Test 5 Passed!")


if __name__ == "__main__":
    print("Initializing test runner...")
    unittest.main()