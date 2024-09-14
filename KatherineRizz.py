# Create a function to generate a multiplication table
def new_multiplication_table(number):
    # Loop over the numbers from 1 to 12
    for i in range(1, 13):
        # Calculate the product of the number
        product = number * i

        # Output the multiplication table entry
        print(f"{number} x {i} = {product}")

# Get the input from user
number = int(input("Enter a number: "))

# Display the multiplication table generated
new_multiplication_table(number)

# Ask the user for the author or book title they're searching for
search_term = input("Enter an author name or book title: ")

# Check if the search term is an author name or book title
Books = {
    "James Patterson": ["Kiss the girls", "First to die"],
    "George R.R. Martin": ["A Game of Thrones", "A Clash of Kings"],
    "J.K. Rowling": ["Harry Potter and the Deathly Hallows", "Harry Potter and the Prisoner of azkaban"],
    "Danelle Steele": ["Thurston House", "The Bungalow 2"]
}

if search_term in Books:
    # If it's an author name, print the list of book titles
    print(f"Books by {search_term}:")
    for book in Books[search_term]:
        print(f"- {book}")
elif search_term in [book for books_list in Books.values() for book in books_list]:
    # If it's a book title, print the author name
    for author, books_list in Books.items():
        if search_term in books_list:
            print(f"{search_term} is written by {author}.")
else:
    # If the search term is not found, print an error message
    print("No such book or author in the catalog.")

# Ask the user for the author name and book title to add to the dictionary
new_author = input("Enter an author name to add: ")
new_book = input("Enter a book title to add: ")

# Update the dictionary with the new entry
Books[new_author] = [new_book]

# Print the updated dictionary
print("Updated dictionary:")
for author, books_list in Books.items():
    print(f"{author}: {books_list}")