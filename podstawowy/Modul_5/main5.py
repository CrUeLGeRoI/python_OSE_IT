import datetime

today = datetime.date.today()


global CURRENT_YEAR
CURRENT_YEAR = today.year


def wykonac_program():
    print("Hello, gimme your name and birth year. I swear its not for stealing your info :)")
    name = input("Give me your name: ")
    age = CURRENT_YEAR - int(input(f"Now, {name}, write down the year you were born: "))
    if age >= 18:
        print("Wow, you can buy vodka!!(Dont do that)")
    else:
        print("No vodka")
    if name[-1] == "a" or name == "Barnaba":
        print("I think you're a woman!!")
    else:
        print("I think you're a man!!")




if __name__ == '__main__':
    wykonac_program()
