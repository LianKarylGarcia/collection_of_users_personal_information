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
        
        full_name = input("What is your full name? ")
        print(f"Hi {full_name}!")
        full_name.append(full_name)

        birthday = input("When is your birthday? ")
        birthday.append(birthday)
        
        age = int(input("How old are you? "))
        if age >= 18:
            print("You are an adult")
        else:
            print("You are a minor")
        age.append(age)

        birthplace = input("Where were you born? ")
        birthplace.append(birthplace)

        address = input("Where do you live? ")
        address.append(address)

        mothers_name = input("What is your mother's name? ")
        mothers_name.append(mothers_name)

        fathers_name = input("What is your father's name? ")
        fathers_name.append(fathers_name)

        school = input("Where do you study? ")
        school.append(school)


        year = input("What year are you? ")
        year.append(year)

        course = input("What is your course? ")
        course.append(course)

        favorite_movie = input("What is your favorite movie? ")
        favorite_movie.append(favorite_movie)

        favorite_color = input("What is your favorite color? ")
        favorite_color.append(favorite_color)

        favorite_artist = input("Who is your favorite artist? ")
        favorite_artist.append(favorite_artist)

        favorite_song = input("What is your favorite song? ")
        favorite_song.append(favorite_song)

        print("Wow! You have good taste!")

        print(f"Thank you for answering, {full_name}!")
        
    except: 
        print("Invalid Input")

