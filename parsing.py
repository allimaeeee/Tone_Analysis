import pymupdf
import re
import pysbd
import pandas as pd

seg = pysbd.Segmenter(language = "en", clean = False)

books = {
    #Title,
    "books/The_Hunger_Games.pdf": ("The Hunger Games"),
    "books/Catching_Fire.pdf": ("Catching Fire"),
    "books/MockingJay.pdf": ("MockingJay")
}

def clean(text):
    text = text.replace("\u00ad", "")                
    text = re.sub(r"(\w)-\s+(\w)", r"\1\2", text)    
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def get_text(path):
    """Return a list of dicts: page, text."""
    doc = pymupdf.open(path)
    pages = []
    last = None
    for page in doc:
        text = re.sub(r"\s+", " ", page.get_text()).strip()
        sent = [s.strip() for s in seg.segment(text) if s.strip()]
        if sent and last is not None and not re.compile(r"[.?!\"'”’…]$").search(pages[last][-1]):
            pages[last][-1] += " " + sent.pop(0)
            ## Could we use something similar for dialogue
        pages.append(sent)
        if sent:
            last = len(pages) - 1
    return pages
    
if __name__ == "__main__":
    THG_Book = get_text("books/The_Hunger_Games.pdf")
    rows = [
        {"page": p, "sentence_num": i, "text": s}
        for p, sents in enumerate(THG_Book)
        for i, s in enumerate(sents, start = 1)
    ]
    df = pd.DataFrame(rows)
    df.to_csv("hunger_games_sentences.csv", index = False)
    #CF_Book = get_text("books/Catching_Fire.pdf")
    #MJ_Book = get_text("books/MockingJay.pdf")

    #THG_Movie = get_text("scripts/The_Hunger_Games_Movie.pdf")
    #CF_Movie = get_text("scripts/Catching_Fire_Movie.pdf")

# def get_source(pdf):
#     """From the pdf if book, then source = book else movie """
#     pass

# def get_booktitle(pdf):
#     """Whatever the name of the dataset is minus book or movie"""
#     pass

# def get_chapter(pdf):
#     #current_chapter = 0
#     #if text_font_size = whatever:
#     #current_chapter += 1
#     #how to handle epilogues or prologues
#     pass

# def get_sequence_num(pdf):
#     #current_num = 0
#     #for each sentence in each page:
#         #current_num += 1
#     pass

# def get_sentence(pdf):
#     """Adds each sentence to database with 
#     Necessary information"""
#     pass

# def get_type(sentence):
#     """If quotations then dialogue else narration"""
#     pass

# def get_pov_character(pdf):
#     """if source == book, pov = katniss else...."""
#     pass

# # scene_id 
# # cross_reference_id			
# # speaker	
# # Topic	
# # emotion	
# # tone	
# # intensity 	
# # method	
# # confidence_score	

# ## 2D List. Each page has every sentence on that page
# ## [[sentence]] book[0] = page book[0][0] = sentence
# ## re.sub()