import unittest


class MyTestCase(unittest.TestCase):
    def exercise_one(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
