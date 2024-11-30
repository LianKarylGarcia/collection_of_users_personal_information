# Put information in an array
# Use a while loop so it doesn't end if the input is invalid.
# Ask the user for inputs.
# Store it in a text file.

# Personal Information
full_name = []
birthday = []
age = []
birthplace = []
address = []
mothers_name = []
fathers_name = []

# Education
school = []
year = []
course = []

# Preferences
favorite_movie = []
favorite_color = []
favorite_artist = []
favorite_song = []

while True: # First loop
    try:
        print("Greetings, please answer the following questions about yourself.")
        
        print("Please follow this format: Surname, First Name Middle Initial")
        full_name = input("What is your full name? ")

        birthday = input("When is your birthday? ")
        age = int(input("How old are you? "))
        birthplace = input("When were you born? ")
        address = input("Where do you live? ")
        mothers_name = input("What is your mother's name? ")
        fathers_name = input("What is your father's name? ")

        school = input("Where do you study? ")
        year = input("What year are you? ")
        course = input("What is your course? ")

        favorite_movie = input("What is your favorite movie? ")
        favorite_color = input("What is your favorite color? ")
        favorite_artist = input("Who is your favorite artist? ")
        favorite_song = input("What is your favorite song? ")
    except: 
        print("Invalid Input")
