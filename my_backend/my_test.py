import my_best_search           # File to test
import my_ideal_search          # File to test
import my_ideal_split_search    # File to test
import my_add_student           # File to test

import json
import unittest                 # Testing framework

# In progress 
class Test_Ideal_Search(unittest.TestCase):

    ''' Testing Ideal Search for single student '''
    def test_single_ideal_search_out(self): 
        # Testing if output is correct
        # Opening file and passing it into single_ideal_search 
        file = open("/home/patty/my_projects/rcos/housing_project/Housing-2.0-B/single_student_input.json")
        student = json.load(file)
        file.close()
        
        testOutput = my_ideal_search.single_ideal_search(student)
        self.assertEqual(testOutput, ["JohnSmith", 7, "Warren1-1"])

    ''' Testing if adding student works ''' 
    def test_add_student(self):
        # Testing if output is correct
        # Opening file and passing it into single_ideal_search 
        file = open("/home/patty/my_projects/rcos/housing_project/Housing-2.0-B/single_student_input.json")
        student = json.load(file)
        file.close()
        
        # See if student has been added 
        self.assertEqual(my_add_student.add_student(student), "true")
        # Compare modified json after student has been added 
        self.assertEqual()        
    

# In progress
class Test_Best_Search(unittest.TestCase):
    def test_best_search_out(self):
        self.assertEqual()


if __name__ == "__main__":
    print("Testing Ideal_search.py ...")

    unittest.main()


    

    
    