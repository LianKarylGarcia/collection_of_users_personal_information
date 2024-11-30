# Put information in an array
# Use a while loop so it doesn't end if the input is invalid.
# Ask the user for inputs.
# Store it in a text file.

# Personal Information
full_name = []
birthday = []
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
    except: 
        print("Invalid Input")
