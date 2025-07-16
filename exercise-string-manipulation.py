# Split the values
to_be_changed = "John Glenn|Neil Armstrong|Sally Ride|Douglas Wheelock|Mae Jemison"
changed_values = to_be_changed.split("|")
print(changed_values)

# Split the lyrics
lyrics = """
Katie Casey was baseball mad,
Had the fever and had it bad.
Just to root for the home town crew,
Ev'ry sou
Katie blew.
On a Saturday her young beau
Called to see if she'd like to go
To see a show, but Miss Kate said "No,
I'll tell you what you can do:"
"""
lyrics_split = lyrics.split("\n")
print(lyrics_split)

# Use something other than split
lyrics = """
Katie Casey was baseball mad,
Had the fever and had it bad.
Just to root for the home town crew,
Ev'ry sou
Katie blew.
On a Saturday her young beau
Called to see if she'd like to go
To see a show, but Miss Kate said "No,
I'll tell you what you can do:"
"""
changed_values = lyrics.splitlines()
print(changed_values)

# How long is the name string
long_village_name = "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"
string_length = len(long_village_name)
print(string_length)

# Folders w/o spaces
my_path = ' /c/Users/instructor/Downloads/Submit Relating the Nonrelational Assessment Download May 10, 2021 917 AM '
my_folders = my_path.strip().split("/")
print(my_folders)

# Change the third name
composers="Beethoven,Ludwig von;Liszt,Franz;Mozart,Wolfgang;Copland,Aaron"
composers = composers.replace('Mozart,Wolfgang', 'Wolfgang Mozart')
print(composers)

# Separate the composers
composers_split = composers.split(";")
print(composers_split)

# Get the third composer
third_composer = composers_split[2]
print(third_composer)

# Find the comma in the name
comma_position = third_composer.find(",")
print(comma_position)

# Use the slicing notation to get the last name
# last_name = third_composer[]

# Use the slicing notation to get the first name
# first_name = third_composer[]

# Join the names to get the 3rd composer's name in "first last" format
first_name = "Wolfgang"
last_name = "Mozart"
full_name = first_name + " " + last_name
print(f"{first_name} {last_name}")
print(full_name)

# Print the composer's name
# print(third_composer_name)

# clean the strings
left_padded = '         Operators are standing by.'
right_padded = 'Call now           '
print(left_padded)
print(right_padded)
left_clean = left_padded.strip()
right_clean = right_padded.strip()
cleaned_string = right_clean + '!' + ' ' + left_clean
print(cleaned_string)

# old style formatting
student_name = "Owen"
grade = 94.75
assignment_number = 12
print('Student name: %s, Assignment ID: %04d, Grade: %.2f%%' % (student_name, assignment_number, grade))

employee_id = "30"
employee_id_padded = employee_id
print(employee_id_padded)

employee_id = "30"
employee_id_padded = employee_id.zfill(6)
print(employee_id_padded)

# Use raw strings
print(r"\n represents a new line.")

# Convert based on variable names
i_want_to_yell = 'yeah'
I_NEED_TO_BE_QUIET = 'SHHHHH'
this_is_a_title = 'this is a title'
sWAPcASE = 'sWAPcASE'
capitalize_this = 'capitalize this'

i_want_to_yell = 'yeah'
i_want_to_yell = i_want_to_yell.upper()
print(i_want_to_yell)

I_NEED_TO_BE_QUIET = 'SHHHHH'
I_NEED_TO_BE_QUIET = I_NEED_TO_BE_QUIET.lower()
print(I_NEED_TO_BE_QUIET)

this_is_a_title = 'this is a title'
this_is_a_title = this_is_a_title.title()
print(this_is_a_title)

sWAPcASE = 'sWAPcASE'
sWAPcASE = sWAPcASE.swapcase()
print(sWAPcASE)

capitalize_this = 'capitalize this'
capitalize_this = capitalize_this.capitalize()
print(capitalize_this)