from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (in-memory database)
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "1984", "author": "George Orwell"}
]

# Route to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({"books": books})

# Route to get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        return jsonify({"book": book})
    else:
        return jsonify({"message": "Book not found"}), 404

# Route to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    new_book["id"] = max(b["id"] for b in books) + 1
    books.append(new_book)
    return jsonify({"message": "Book added successfully", "book": new_book}), 201

# Route to update a book by ID
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        updated_book = request.get_json()
        book.update(updated_book)
        return jsonify({"message": "Book updated successfully", "book": book})
    else:
        return jsonify({"message": "Book not found"}), 404

# Route to delete a book by ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b['id'] != book_id]
    return jsonify({"message": "Book deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
