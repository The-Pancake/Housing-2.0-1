# what I maybe plan to do is that if there are no "perfect" matches,
# collect rooms that are good matches and sort between those and pick
# the best of them - this sort of emulates a best fit and ideal fit at
# the same time (will be two seperate sort functions *if a perfect fit
# is not found*)

# i want to have it working with just induvial students before I implement
# groups - though that shouldn't be hard since groups will pretty much always
# fit under the perfect fit category of things

potentialRooms = []

# weights rooms on a bunch of variables - to change, currently acts as just an example 
# of what it will be
def weightRoom(room, student):

    i = 0

    for j in room["occupants"]:
        if (j["major"] == student["major"]):
            i += 5

        if (j["geo"] == student["geo"]):
            i += 3
        
        for k in range(2):
            if (j["sleepHours"][k] == student["sleepHours"][k] or j["sleepHours"][k] + 1 == student["sleepHours"] or j["sleepHours"][k] - 1 == student["sleepHours"]):
                i += 1
        
        for k in j["musicPreference"]:
            if (k in student["musicPreference"]):
                i += 1
        
        for k in j["hobbies"]:
            if (k in student["musicPreference"]):
                i += 1

    if (i == 0 and len(room["occupants"]) == 0):
        i += 1

    k = 0    
    
    for j in student["dormPref"]:
        if (j == room["name"]):
            i += 5 - k
            k += 1

    return i

# after first search, uses potentialRooms to look
def idealSearch(student):

    bestMatch = potentialRooms[0]
    highestWeight = 0

    for i in range(len(potentialRooms)):
        w = weightRoom(potentialRooms[i], student)
        
        if (w > highestWeight):
            bestMatch = potentialRooms[i]
            highestWeight= i
            

    if (bestMatch["sex"] == "e"):
        bestMatch["sex"] = student["sex"]

    bestMatch["occupants"].append(student)
    student["dorm"] = bestMatch["name"]

    return

# looks to see if two students have commonality
def isPerfectMatch(room, student):

    i = 0

    for j in room["occupants"]:
        if (j["major"] == student["major"]):
            # print("same major")
            i += 5

        if (j["geo"] == student["geo"]):
            i += 1

        for k in range(2):
            if (j["sleepHours"][k] == student["sleepHours"][k] or j["sleepHours"][k] + 1 == student["sleepHours"] or j["sleepHours"][k] - 1 == student["sleepHours"]):
                i += 1
        
        for k in j["musicPreference"]:
            if (k in student["musicPreference"]):
                i += 1
        
        for k in j["hobbies"]:
            if (k in student["musicPreference"]):
                i += 1
        

    if (i > 4): 
        return True

    return False

# if there is a "perfect" fit, it matches the student there, otherwise collecting other
# decent fits to use in a sort of ideal search
def firstSearch(data, student):

    potentialRooms.clear()

    if (len(student["dormPref"]) != 0): # if there is a preferred dorm, look through those
        
        for i in student["dormPref"]:
            
            # move through dorm prefs - later on we can just move the iterablle to specific points in the array
            dorm = data.keys()  # list of dorms to use as keys

            for j in dorm:
                if (i in j): # find preferred dorm
                    
                    # see if possible to move into room
                    if ((student["sex"] == data[j]["sex"] or data[j]["sex"] == "e" or data[j]["sex"] == "i") and student["year"] == data[j]["year"] and 
                    len(data[j]["occupants"]) < data[j]["size"]) and data[j]["ra room"] == False:
                        
                        # for k in data[j]["occupants"]:
                        #     if k["name"] == student["name"]:
                        #             return False
                    
                        if (len(data[j]["occupants"]) > 0):
                            
                            if (isPerfectMatch(data[j], student)):
                                data[j]["occupants"].append(student)

                                return True
                            else:
                                potentialRooms.append(data[j])

                        if (len(data[j]["occupants"]) == 0):
                            potentialRooms.append(data[j])

    # the case in no dorm pref, or if it couldn't find it regardless
    if (len(potentialRooms) == 0):
        dorm = data.keys()
        # print(student)
        for j in dorm:

            if ((student["sex"] == data[j]["sex"] or data[j]["sex"] == "e" or data[j]["sex"] == "i") and student["year"] == data[j]["year"] and 
                len(data[j]["occupants"]) < data[j]["size"] and data[j]["ra room"] == False):
                #print(student)
                
                # for k in data[j]["occupants"]:
                #     if k["name"] == student["name"]:
                #         return False
                
                if (len(data[j]["occupants"]) > 0):
                    
                    if (isPerfectMatch(data[j], student)):
                        
                        data[j]["occupants"].append(student)

                        return True
                    else:
                        potentialRooms.append(data[j])

                if (len(data[j]["occupants"]) == 0):
                    potentialRooms.append(data[j])
               
    if (len(potentialRooms) != 0):
        idealSearch(student)
    else:
        return False
    

def groupSort(students):

    return