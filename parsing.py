import pymupdf

books = {
    #Title,
    "books/The_Hunger_Games.pdf": ("The Hunger Games"),
    "books/Catching_Fire.pdf": ("Catching Fire"),
    "books/Mockingjay.pdf": ("Mockingjay")
}

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

def get_source(pdf):
    """From the pdf if book, then source = book else movie """
    pass

def get_booktitle(pdf):
    """Whatever the name of the dataset is minus book or movie"""
    pass

def get_chapter(pdf):
    #current_chapter = 0
    #if text_font_size = whatever:
    #current_chapter += 1
    #how to handle epilogues or prologues
    pass

def get_sequence_num(pdf):
    #current_num = 0
    #for each sentence in each page:
        #current_num += 1
    pass

def get_sentence(pdf):
    """Adds each sentence to database with 
    Necessary information"""
    pass

def get_type(sentence):
    """If quotations then dialogue else narration"""
    pass

def get_pov_character(pdf):
    """if source == book, pov = katniss else...."""
    pass

# scene_id 
# cross_reference_id			
# speaker	
# Topic	
# emotion	
# tone	
# intensity 	
# method	
# confidence_score	

## 2D List. Each page has every sentence on that page
## [[sentence]] book[0] = page book[0][0] = sentence
## re.sub()