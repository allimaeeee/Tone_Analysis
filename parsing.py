import pymupdf

def get_text(pdf):
    doc = pymupdf.open(pdf)
    pages = [page.get_text() for page in doc]
    #Each book is currently a list of pages
    return pages

THG_Book = get_text("books/The_Hunger_Games.pdf")
CF_Book = get_text("books/Catching_Fire.pdf")
MJ_Book = get_text("books/MockingJay.pdf")

THG_Movie = get_text("scripts/The_Hunger_Games_Movie.pdf")
CF_Movie = get_text("scripts/Catching_Fire_Movie.pdf")


## 2D List. Each page has every sentence on that page
## [[sentence]] book[0] = page book[0][0] = sentence
## re.sub()