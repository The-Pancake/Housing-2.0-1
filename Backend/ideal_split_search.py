# Implement Algorithm Here:

# def idealSplitSearch():
#     return

import json 

'''
Will try to search for rooms with connected bathrooms in preferred dorms of the group preference
'''
def ideal_split_search(group_list,group_preferences,campus):
  group_size = len(group_list)
  buildings = campus.keys()
  print(buildings)

  middle_index = group_size // 2

  group1 = group_list[:middle_index]
  group2 = group_list[middle_index:]

  for dorm in group_preferences:#loops through all the dorms in the groups preferred list
    for floor in campus[dorm]: #loops through the floors of said building
      for room in campus[dorm][floor]:#loops through the rooms in the building
        #if the room size does not fit the group or it is occupied
        if campus[dorm][floor][room]["size"] != len(group1) or len(campus[dorm][floor][room]["Occupants"]) > 0: 
          continue
        else:
          if campus[dorm][floor][room]["shared_bathroom"] != False:
            connected_room = campus[dorm][floor][room]["shared_bathroom"]
            if campus[dorm][floor][connected_room]["size"] == len(group2) or len(campus[dorm][floor][room]["Occupants"]) > 0:
              campus[dorm][floor][room]["Occupants"] = copy.deepcopy(group1)
              campus[dorm][floor][room]["Occupants"] = copy.deepcopy(group2)
              a = open('C:/Users/dongm2/Documents/RPI/Personal_projects/Rcos/objects_changed.json', 'w')
              json.dump(campus,a, indent = 2)
              a.close()
              return 1
  return 0