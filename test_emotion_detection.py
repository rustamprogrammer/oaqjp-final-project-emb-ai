"""Check the dominant emotion for each of the five course examples."""

import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Exercise the detector against the Watson NLP service."""

    def test_dominant_emotion(self):
        """Verify the expected dominant emotion for every example."""
        cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]
        for text, expected in cases:
            with self.subTest(emotion=expected):
                result = emotion_detector(text)
                self.assertEqual(result["dominant_emotion"], expected)


if __name__ == "__main__":
    unittest.main()
