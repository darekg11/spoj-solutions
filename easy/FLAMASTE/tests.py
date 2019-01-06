import unittest
import main

class FLAMASTE_Tests(unittest.TestCase):
    def test_single_characters(self):
        input_text = 'ABCDEFGHIJKLMNO'
        expected_text = 'ABCDEFGHIJKLMNO'
        output = main.convert_string(input_text)
        self.assertEqual(output, expected_text)

    def test_first_example(self):
        input_text = 'OPSS'
        expected_text = 'OPSS'
        output = main.convert_string(input_text)
        self.assertEqual(output, expected_text)
    
    def test_second_example(self):
        input_text = 'ABCDEF'
        expected_text = 'ABCDEF'
        output = main.convert_string(input_text)
        self.assertEqual(output, expected_text)
    
    def test_third_example(self):
        input_text = 'ABBCCCDDDDEEEEEFGGHIIJKKKL'
        expected_text = 'ABBC3D4E5FGGHIIJK3L'
        output = main.convert_string(input_text)
        self.assertEqual(output, expected_text)
    
    def test_fourth_example(self):
        input_text = 'AAAAAAAAAABBBBBBBBBBBBBBBB'
        expected_text = 'A10B16'
        output = main.convert_string(input_text)
        self.assertEqual(output, expected_text)


if __name__ == '__main__':
    unittest.main()