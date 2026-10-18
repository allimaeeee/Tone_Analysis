import fitz

doc = fitz.open("The_Hunger_Games.pdf")
pages = [page.get_text() for page in doc]