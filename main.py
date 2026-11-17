# 1. Introduction to FastAPI
# 2. Creating a FastAPI application

# 3. Running a FastAPI application
# fastapi dev main.py -> Runs the application in development mode.
# fastapi run main.py -> Runs the application in production mode.

# 4. Decorators and HTTP methods
# 5. Multiple decorators on one function

# 6. Response classes
# 7. include_in_schema

# 8. API documentation
# /docs  -> Swagger UI documentation.
# /redoc -> ReDoc documentation.

# 9. Returning data
# 10. Python type annotations


from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Creating a FastAPI application instance
app = FastAPI()


# Demo data: List of dictionaries
books: list[dict] = [
    {
        "title": "Atomic Habits",
        "author": "James Clear",
        "content": "A practical guide to building good habits, breaking bad ones, and making small improvements every day.",
        "pages": 320
    },
    {
        "title": "Deep Work",
        "author": "Cal Newport",
        "content": "Explores the importance of focused, distraction-free work and how to develop the ability to concentrate deeply.",
        "pages": 296
    }
]


# Multiple decorators can point to the same function.
# HTMLResponse specifies that the response should be HTML.
# include_in_schema=False excludes these endpoints from API docs.

@app.get("/booktitle", response_class=HTMLResponse, include_in_schema=False)
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def home():

    # Returning an HTML heading using data from the books list.
    return f"<h1>{books[0]['title']}</h1>"

    # Incorrect syntax:
    # return f"<h1>{books[0]["title"]}</h1>"
    # The nested double quotes cause a syntax error.


# GET endpoint to retrieve all books.
# FastAPI automatically converts the returned list of dictionaries into JSON.
@app.get("/books")
def getbooks():
    return books


# API documentation:
# /docs  -> Swagger UI
# /redoc -> ReDoc
