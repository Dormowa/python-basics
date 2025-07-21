# constant variable for the highlight threshold
HIGHLIGHT_THRESHOLD = 9.0

# check if the item rating is high enough to be highlighted
def is_highlight_item(rating):
    return rating >= HIGHLIGHT_THRESHOLD

# format item details
def format_item(name, category, rating):

    #clean and format name and category strings
    name = name.title().strip()
    category = category.title().strip()

    # convert rating to float to allow decimal values
    rating = float(rating)

    # return string with or without highlight label
    if is_highlight_item(rating):
        return f"{name} ({category}) - Rating: {rating:.1f} ★ Highlight Item!"
    else:
        return f"{name} ({category}) - Rating: {rating:.1f}"

# save the collection as a txt file    
def save_collection_to_file(collection, filename):
    with open(filename, 'w', encoding = 'utf-8') as file: # open the file in write mode, encode to support special characters

        # loop through the collection items and write in the file
        for item in collection:
            name, category, rating = item
            formatted = format_item(name, category, rating)
            file.write(formatted + '\n')

# create main function to run the collection tracker
def main():
    print("Welcome to the Book & Film Collection Tracker!")
    collection = []

    # break the while loop if user types 'done'
    while True:
        name = input("Enter the name of the item: ").strip()
        if name.lower() == "done":
            break

        # prompt user to enter catefory
        category = input("Enter the category (Book or Film): ").strip().title()
        if category not in ["Book", "Film"]:

            # print error if not a valid category
            print("Invalid category. Please enter 'Book' or 'Film'.")
            continue
        
        # prompt user to enter rating
        rating_input = input("Enter the rating (1-10): ").strip()

        # display error if rating is not a number
        try:
            rating = float(rating_input)
        except ValueError:
            print("Invalid rating. Please enter a number.")
            continue
        
        # add item to the collection
        collection.append((name, category, rating))
        print("Item added!")

    # display collection summary
    print("--- Collection Summary ---")
    for item in collection:
        name, category, rating = item
        print(format_item(name, category, rating))

    save_collection_to_file(collection, "collection.txt")
    print("Your collection has been saved to collection.txt.")

# call main function to begin program
main()