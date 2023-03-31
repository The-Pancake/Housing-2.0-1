'''
    This is a helper function to generate a list (of random size) of hobbies/ interestes 
    that a person can potentially have. This will be used in my_students.json 

    THIS IS GENERATED FROM CHAT.OPENAI

'''
import random


def interests_generator():

    interests = ["reading", "painting", "gardening", "cooking", "playing video games", "writing", "yoga", 
               "playing an instrument", "dancing", "photography", "hiking", "traveling", "filming",
               "sports", "gym", "music" ]
    num_hobbies = random.randint(1, min(len(interests), 5))
    
    return random.sample(interests, num_hobbies)

if __name__ == "__main__":
    
    for i in range(10):
        print(interests_generator())