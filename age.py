def get_user_age():
    age_to_check = int(input("enter your age: "))
    if age_to_check < 0:
        raise ValueError("who has negative age?")
    return age_to_check
try:
    get_user_age()
except ValueError as e:
    print(e.args)
    get_user_age()