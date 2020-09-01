"""The program will ask for user's name"""
name = input("What is your name?")
age = ()
"""The program will ask for the user's year of birth"""

year_of_birth = input("What year were you born?" )

"""Python converts the birth year to usable numbers"""

year_of_birth = int(year_of_birth)

if 2008 == year_of_birth:
    print("Congratulations",(name), "You are as old as Python itself!")

elif 2008 >= year_of_birth:
    age = 2008-year_of_birth
    if age == 1:
        print("You are",(age),"year older than python")