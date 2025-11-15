current_year = 2025

def generate_profile(age:int)->str:
    if age <0:
        category = "Invalid life stage"
    elif age <= 12:
        category = "Child"
    elif age > 12 and age <= 19:
        category = "Teenager"
    elif age > 19:
        category = "Adult"
    return category

def generate_hobbies_list(hobby:str)->list:
    hobbies = []
    while hobby!="stop" and len(hobby)>1:
        hobbies.append(hobby.capitalize())
        hobby = input("Enter a favorite hobby or type 'stop' to finish: ").lower()
    return hobbies

def create_user_profile()-> dict:
    user_name = input("Enter your full name: ").title()
    birth_year = int(input("Enter your birth year: "))
    current_age = current_year - birth_year
    hobbies = generate_hobbies_list(input("Enter a favorite hobby or type 'stop' to finish: ").lower())
    life_stage = generate_profile(current_age)
    return dict(name=user_name, age=current_age, stage=life_stage, hobbies=hobbies)

user_profile = create_user_profile()

def display_profile(profile:dict):
    print(f"Profile summary: \n"
          f"Name: {user_profile.get('name')}\n"
          f"Age: {user_profile.get('age')}\n"
          f"Life stage: {user_profile.get('stage')}"
          )
    if len(user_profile.get('hobbies'))>0:
        print(f"Favorite hobbies {len(user_profile.get('hobbies'))}:")
        for hobby_type in user_profile.get('hobbies'):
            print(f"- {hobby_type}")
    else:
        print(f"You didn't mention any hobbies.")

display_profile(user_profile)







































