import unittest
import guessing_game

class TestGame(unittest.TestCase):
    
    def test_input(self):
        result = guessing_game.run_guess(4,4)
        self.assertTrue(result)

    def test_input_wrong(self):

        result = guessing_game.run_guess(5,0)
        self.assertFalse(result)
        
    def test_input_out_of_range(self):

        result = guessing_game.run_guess(5,11)
        self.assertFalse(result)
        
    def test_input_str(self):

        result = guessing_game.run_guess(5,'11')
        self.assertFalse(result)
        
if __name__ == '__main__':          
    unittest.main()