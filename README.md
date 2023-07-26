# Book Inventory Management

This is a text-based book inventory management system built with Python. 

The project includes several initial functionalities with minimal error handeling and protection. Included in this current iteration is: adding books, removing books, searching by isbn, title, or author, and listing all currently available books.

# How to Run

1. Clone the repository.
```
git clone https://github.com/jaredonnelly/book-inventory-manager.git
```

3. Install dependencies (open the correct directory).
```
pip install -r requirements.txt
```

4. Run the application.
```
python main.py
```

# TODO
- list function, option to reverse display order.
- add books function, standardize ISBN input so it has no hyphens.
- add books function, option to fill in missing information using isbnlib.
- add books function, if book is already in database - ask if user would like to increasse stock 
- database, add additional safety measures to protect against sql injections.
- remove function, include isbn check. 
- remove funciton, add confirmation that the correct book was found.
- search function, allow search to be more broad using regex.
