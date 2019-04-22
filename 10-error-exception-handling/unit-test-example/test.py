import unittest
import cap


class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = "python"
        result = cap.cap_text(text)
        # we check, that result of the functin executino is equal to
        # expected result
        self.assertEqual(result, "Python")

    def test_multiple_words(self):
        text = "monty python"
        result = cap.cap_text(text)
        self.assertEqual(result, "Monty Python")


# the way of executing unittest is:
if __name__ == "__main__":
    unittest.main()
