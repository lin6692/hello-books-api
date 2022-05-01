from flask import Blueprint, jsonify, abort, make_response, request
from app.models.book import Book
from app import db

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["POST", "GET"])
def handle_books():
    if request.method == "POST":
            res = request.get_json()
            book = Book(
                title = res["title"],
                description = res["description"]
            )

            db.session.add(book)
            db.session.commit()

            return make_response(
                f"Book {book.title} ID {book.id} successfully created", 200
            )

    elif request.method == "GET":
        books = Book.query.all()
        res = []
        for book in books:
            res.append({
                "id":book.id,
                "title": book.title,
                "description" : book.description
            })

        return  jsonify(res), 200

@books_bp.route("/<id>", methods=["GET", "PUT", "DELETE"])
def handle_book(id):
    book = valid_book(id)
    if request.method == "GET":
        return {
                    "id":book.id,
                    "title": book.title,
                    "description" : book.description
                }, 200
    
    elif request.method == "PUT":
       res = request.get_json()

       book.title = res["title"]
       book.description = res["description"]

       db.session.commit()

       return make_response({
           "message": f"Book {id} has been updated successfully.",
           "data": {
               "id" : book.id,
               "title": book.title,
               "description": book.description
           }
       }, 200)

    elif request.method == "DELETE":
        db.session.delete(book)
        db.session.commit()
        return make_response(f"Book #{id} successfully deleted", 200)


def valid_book(id):
    try:
        id = int(id)
    except:
        abort(make_response({"message":f"book {id} invalid"}, 400))
    
    book = Book.query.get(id)  # pass in PK.   Model.query.get(PK)
    if not book:
        abort(make_response({"message":f"book {id} not found"}, 404))
    return book


'''
HELLO WORLD
'''
# hello_world_bp = Blueprint("hello_world", __name__)

# @hello_world_bp.route("/hello-world", methods=["GET"])
# def say_hello_word():
#     response_body = "Hello, World!"
#     return response_body

# @hello_world_bp.route("/hello/JSON", methods=["GET"])
# def get_json():
#     return {
#     "name": "Ada Lovelace",
#     "message": "Hello!",
#     "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#     }

# @hello_world_bp.route("/broken-endpoint-with-broken-server-code")
# def broken_endpoint():
#     response_body = {
#         "name": "Ada Lovelace",
#         "message": "Hello!",
#         "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#     }
#     new_hobby = "Surfing"
#     response_body["hobbies"].append(new_hobby)
#     return response_body
'''
BOOK HARDCODE
'''
# class Book:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description

# books = [
#     Book(1, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
#     Book(2, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
#     Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")
# ] 


# @books_bp.route("/<book_id>", methods=["GET"])
# def handle_book(book_id):
#     book = validdate_book(book_id)
#     return {
#         "id":book.id,
#         "title":book.title,
#         "description":book.description
#         }

# def validdate_book(book_id):
#     try:
#         book_id = int(book_id)
#     except:
#         abort(make_response({"message":f"book {book_id} invalid"}, 400))

#     for book in books:
#         if book.id == book_id:
#             return book

#     abort(make_response({"message":f"book {book_id} not found"}, 404))