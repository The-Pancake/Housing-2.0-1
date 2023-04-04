import json
import copy
# Implement Algorithm Here:

# def idealSplitSearch():
#     return

'''
Will try to search for rooms with connected bathrooms in preferred dorms of the group preference
'''
def best_split_search(group_list,campus):
  group_size = len(group_list)
  buildings = campus.keys()
  print(buildings)

  middle_index = group_size // 2

  group1 = group_list[:middle_index]
  group2 = group_list[middle_index:]

  for dorm in campus:#loops through all the dorms in the groups preferred list
    for room in campus[dorm]:#loops through the rooms in the building
      #if the room size does not fit the group or it is occupied
      if campus[dorm][room]["size"] != len(group1) or len(campus[dorm][room]["Occupants"]) > 0: 
        continue
      else:
        if campus[dorm][room]["shared_bathroom"] == True:
          connected_room = campus[dorm][room]["shared_bathroom"]
          if campus[dorm][connected_room]["size"] == len(group2) or len(campus[dorm][room]["Occupants"]) == 0:
            campus[dorm][room]["Occupants"] = copy.deepcopy(group1)
            campus[dorm][room]["Occupants"] = copy.deepcopy(group2)
            a = open('C:/Users/dongm2/Documents/RPI/Personal_projects/Rcos/objects_changed.json', 'w')
            json.dump(campus,a, indent = 2)
            a.close()
            return 1
  return 0