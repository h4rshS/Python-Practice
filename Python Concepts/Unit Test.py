import unittest

def parse_and_validate_input():
    num_str = input("Please Enter a number: ")
    return num_str.isdigit()

class CheckInput(unittest.TestCase):
    
    def test_func(self):
        result = parse_and_validate_input()
        self.assertTrue(result)
        
if __name__ == '__main__':
    unittest.main()