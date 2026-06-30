from fastapi import Body,FastAPI

app = FastAPI()

Books=[ {'title':'My first book','author':'Author one','category':'science'},
        {'title':'My seocnd book','author':'Author second','category':'science'},
        {'title':'My third book','author':'Author third','category':'science'},
        {'title':'My fourth book','author':'Author fourth','category':'math'}
    ]




@app.get("/books")
async def read_all_books():
    return Books


@app.get("/books/mybook")
async def  read_all_books():
    return {'book_title':'My first book','book_category':'science'}

##Path parameter
@app.get("/books/{book_title}")
async  def read_All_book(book_title:str):
    for book in Books:
        if book.get('title').casefold() == book_title.casefold():
            return book

## Query Parameter
@app.get("/books/")
async def read_catgeory_by_query(category:str):
    books_to_return=[]
    for book in Books:
        if book.get('category').casefold()==category.casefold():
            books_to_return.append(book)
            return books_to_return

@app.get("/books/{book_author}/")
async def read_author_category_by_query( book_author:str,category:str):
    books_to_return=[]
    for book in Books:
        if  book.get('author').casefold()==book_author.casefold() and book.get('category').casefold()==category.casefold():
            books_to_return.append(book)
            return books_to_return



####//Post Method
@app.post("/book/create_book")
async def create_book(new_book=Body()):
    Books.append(new_book)


#put request
@app.put("/book/{update_book}")
async def update_book(updated_book=Body()):
 for  i in range(len(Books)):
     if Books[i].get('title').casefold()==updated_book.get('title').casefold():
         Books[i]=updated_book

## Delete  Request Method
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title:str):
 for i in range(len(Books)):
     if Books[i].get('title').casefold()==book_title.casefold():
         Books.pop(i)
         break



