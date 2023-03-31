# The following function will add a student into the student data base
import json
'''
    @param studentInfo
    @modifies my_students.json
'''
# {FINISH}
def add_student(studentInfo):
    # Opening student data base 
    file = open("/home/patty/my_projects/rcos/housing_project/Housing-2.0-B/my_students.json")
    
    studentData = json.load(file)

    file.close()

    # Check if student is inside 
    if(check_if_in_data(studentInfo["name"], studentData)):
        return 
    else:
        # Delete dorm preference and a dorm key 
        del studentInfo["dormPref"]
        studentInfo["dorm"] = ""
        # Add student to data base
        studentData[studentInfo["name"]] = studentInfo

    return studentData

# Helper function to see if student is inside the data base
'''
    @param studentName != Null, studentData = database
    @return if student in data, return true | else, return false 
'''
def check_if_in_data(studentName, studentData):
    return studentName in studentData.keys()

# {FINISH}
# Helper function to update anything in student database
'''
    @param studentName !=null
    @param thingToUpdate == list with
'''
def update_database(studentName, thingToUpdate, studentData):
    studentData[studentName] = ""

if __name__ == "__main__":
    file = open("/home/patty/my_projects/rcos/housing_project/Housing-2.0-B/single_student_input.json")
    student = json.load(file)

    print(add_student(student))