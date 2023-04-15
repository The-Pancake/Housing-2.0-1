import json 

# Single Person Ideal Search
# Finds a room for student that takes preferences into account


''' Takes a student as input where student is a dictionary'''
def single_ideal_search (student):
    # Grabs Preferencs
    listofPref = student['dormPref']
    # Opens dorm file
    file = open("/home/patty/my_projects/rcos/housing_project/Housing-2.0-B/my_campus.json")
    campus = json.load(file)
    file.close()

    # Store room with best match + student
    bestRoom = []
    
    # Iterate through list of dorm preferences 
    for dorm in listofPref:
        # Iterate through all rooms in preferred dormitory 
        for roomName in campus: 

            # Checking all dorms rooms with current preference
            if(dorm in roomName): 
                # Check if there are students in the room, if not we want to temporarily place
                # the student in here
                if(len(campus[roomName]["occupants"]) == 0 and len(bestRoom) == 0):
                    bestRoom = roomName
                    continue
                else:
                # if there is someone let's see how compatible they are
                    tempRoom = compatibility(student, campus[roomName]['occupants'], roomName)
                    bestRoom = setBestRoom(bestRoom, tempRoom)
            else: 
                break
    
    return bestRoom 

'''
    Functions below will "RATE" students by compatibility
    - Compatibility is determined by how many things students have in common
    - Will compare age, sex, place of origin, and interests [soon]
   
    Returns a list in the following format: [occupant, rating, room]
'''

# Making sure students are a good match
def compatibility(student, occupants, room):
    
    # search occupant and store student's information
    file = open('/home/patty/my_projects/rcos/housing_project/Housing-2.0-B/my_students.json')
    studentDataBase = json.load(file)
    file.close()    

    # Result array [occupant, rating, result]
    result = ["", 0, ""]    
    # Loop through occpuants [ FOR NOW ]
    for occupant in occupants: 
        occupantInfo = studentDataBase[occupant]
        rating = 0
        # Compare year
        if(student["year"] == occupantInfo["year"]):
            rating += 1 

        # Compare origin
        if(student["location"] == occupantInfo["location"]):
            rating += 1

        # Compare sex 
        if(student["sex"] == occupantInfo["sex"]):
            rating += 1

        # Compare major
        if(student["major"] == occupantInfo["major"]):
            rating += 1

        # Compare interests 
        rating += interestsComparator(student["interests"], occupantInfo["interests"])

        # If student is compatible add to room 
        if result[1] < rating:
            result[0] = occupant
            result[1] = rating
            result[2] = room

    return result
# Helper function for compatibility that takes two lists and compares them 
# This will return the amount of similarities between the two lists
def interestsComparator(studentList, OccupantList):
    similarities = 0 
    
    for interest in studentList:
        if(interest in OccupantList):
            similarities += 1

    print("Similar:", similarities)
    return similarities 

# Returning best room based on compability 
def setBestRoom(roomInfo1, roomInfo2):
    # Return room info if room is empty
    if(len(roomInfo1) == 0):
        return roomInfo2
    else:
        # We know the rating is at index 2 as created by compatibility so just compare them 
        # and return the corresponding room, but we have to make sure that the compatibility
        # of the student is great enough
        if (roomInfo1[1] < roomInfo2[1] and roomInfo2[1] > 4):
            return roomInfo2
        else:
            return roomInfo1 



if __name__ == "__main__":
    file = open("/home/patty/my_projects/rcos/housing_project/Housing-2.0-B/single_student_input.json")
    student = json.load(file)
    
    file.close()


    print(single_ideal_search(student))