# goals for the moment:
# get a baseline working with limited students and housing
# up the scale slowly and compare data structues with whatever else people write

import json
import sortSingles
import random

if __name__ == "__main__":
    
    with open("Backend/json/test.json") as json_file:
        data = json.load(json_file)

    # with open("Smith.json") as json_file:
    #     t1 = json.load(json_file)
    # with open("Doe.json") as json_file:
    #     t2 = json.load(json_file)
    # with open("Sherick.json") as json_file:
    #     t3 = json.load(json_file)
    # with open("He.json") as json_file:
    #     t4 = json.load(json_file)
    # with open("Smithy.json") as json_file:
    #     t5 = json.load(json_file)

    # sort.firstSearch(data, t1)
    # sort.firstSearch(data, t2)
    # sort.firstSearch(data, t3)
    # sort.firstSearch(data, t4)
    # sort.firstSearch(data, t5)

    with open("Backend/json/names.json") as json_file:
        names = json.load(json_file)
    with open("Backend/json/states.json") as json_file:
        states = json.load(json_file)
    with open("Backend/json/majors.json") as json_file:
        majors = json.load(json_file)
    with open("Backend/json/music.json") as json_file:
        music = json.load(json_file)
    with open("Backend/json/hobbies.json") as json_file:
        hobbies = json.load(json_file)
    
    s = ["m", "f"]
    
    for i in range(200):
        
        name = names[random.randrange(0, len(names))]
        sex = s[random.randrange(0, 2)]
        major = majors[random.randrange(0, len(majors))]
        state = states[random.randrange(0, len(states))]

        
        hours1 = [8, 9, 10, 11, 12, 1, 2]
        hours2 = [5, 6, 7, 8, 9, 10]

        sleepHours = [hours1[random.randrange(0, len(hours1))], hours2[random.randrange(0, len(hours2))]]

        musicPrefernce = []

        for j in range(random.randrange(0, 3)):
            k = random.randrange(0, len(music))
            if (music[k] not in musicPrefernce):
                musicPrefernce.append(music[k])

        studentHobbies = []

        for j in range(random.randrange(1, 3)):
            k = random.randrange(1, len(hobbies))
            if (hobbies[k] not in studentHobbies):
                studentHobbies.append(hobbies[k])

             

        randStudent = {
            "name": name,
            "sex": sex,
            "major": major,
            "dormPref": "",
            "year": "freshman",
            "geo": state,
            "sleepHours": sleepHours,
            "musicPreference": musicPrefernce,
            "hobbies": studentHobbies
        }

        sortSingles.firstSearch(data, randStudent)

        with open("Backend/json/test.json", "w") as outf:
            json.dump(data, outf, indent=4)

        st = str(i) + ".json"

        #with open(st, "w") as out:
        #    json.dump(randStudent, out, indent=4)