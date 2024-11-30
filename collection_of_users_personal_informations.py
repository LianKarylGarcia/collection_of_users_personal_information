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
        # To clear the file for new data
        with open("user_infos.txt","a") as file:
            pass 

        print("Greetings, please answer the following questions about yourself.")
        
        # Use .append function to add new user input.
        # Personal Information
        full_name.append = input("What is your full name? ")
        print(f"Hi {full_name}!")
        
        birthday.append = input("When is your birthday? ")
       
        age.append = int(input("How old are you? "))
        if age >= 18:
            print("You are an adult")
        else:
            print("You are a minor")

        birthplace.append = input("Where were you born? ")
        
        address.append = input("Where do you live? ")

        mothers_name.append = input("What is your mother's name? ")

        fathers_name.append = input("What is your father's name? ")
            
        # Education
        school.append = input("Where do you study? ")

        year.append = input("What year are you? ")
        
        course.append = input("What is your course? ")
        
        # Preferences
        favorite_movie.append = input("What is your favorite movie? ")

        favorite_color.append = input("What is your favorite color? ")
        
        favorite_artist.append = input("Who is your favorite artist? ")
        favorite_song.append = input("What is your favorite song? ")

        print("Wow! You have good taste!")

        print(f"Thank you for answering, {full_name[-1]}!")

        # To store user's input in a txt file
        with open("user_info.txt","a") as file:
            file.write(f"Full Name: {full_name[-1]}\n")
    
    except ValueError:
        print("Input invalid. Try aagin :)")






