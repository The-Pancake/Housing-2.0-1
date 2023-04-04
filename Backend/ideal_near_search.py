#do we priortize earlier four person group (now two 2person groups), or later 2 person group?
#fiure out all different ways rpi labels rooms (letters,numbers,letters and numbers?)
def ideal_near_seach(group_list,group_preferences,campus):
  group_size = len(group_list)
  buildings = campus.keys()
  # print(buildings) #used for checking if the buildings are read in correctly

  middle_index = group_size // 2

  group1 = group_list[:middle_index]
  group2 = group_list[middle_index:]
  room_distance = 100000
  room_ids = []
  building = ''
  for dorm in group_preferences:#loops through all the dorms in the groups preferred list
    for room1 in campus[dorm]:#loops through the rooms in the building
      if len(room1["Occupants"]) == 0:#if first room can be used as a candidate
        for room2 in campus[dorm]:#loop through all other rooms in building
          if (room1 != room2) and len(room2["Occupants"]) == 0 and abs(room1-room2) < room_distance:
            room_distance = abs(room1-room2)
            room_ids = [room1,room2]
            building = dorm
  campus[building[room_ids[0]["Occupants"]]] = group1
  campus[building[room_ids[1]["Occupants"]]] = group2
  pass
