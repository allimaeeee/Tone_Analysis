import nltk
import re
import string
import ssl
import pandas as pd

# macOS python.org builds often lack root certs, which breaks nltk.download.
try:
    import certifi
    ssl._create_default_https_context = lambda *a, **k: ssl.create_default_context(cafile=certifi.where())
except ImportError:
    ssl._create_default_https_context = ssl._create_unverified_context

from nltk.corpus import wordnet
for _pkg in ("stopwords", "wordnet", "punkt", "punkt_tab",
        "averaged_perceptron_tagger_eng", "averaged_perceptron_tagger"):
    nltk.download(_pkg, quiet=True)
#lemmatizer = WordNetLemmatizer()
#english_stopwords = set(nltk.corpus.stopwords.words('english'))

"""CLEANING"""

def clean_text(text):
    # convert to lowercase
    text = text.lower()
    # remove s's with whitespace or at end of words
    text = re.sub(r"'s(?=\s|$)", "", text)
    # remove apostrophes
    text = re.sub(r"'", "", text)
    return text.strip()

def tokenize(cleaned_text):
    tokens = nltk.word_tokenize(cleaned_text)
    final_tokens = []
    for token in tokens:
        sub_tokens = re.findall(r'[0-9a-zA-Z]+', token)
        final_tokens.extend(sub_tokens)
    return final_tokens

def lemmatize(tokens, stopwords = {}):
    lemmatized_tokens = []
    lemmatizer = nltk.stem.WordNetLemmatizer()
    for token in tokens:
        pos_tag = nltk.pos_tag([token])[0][1]

        if pos_tag.startswith('J'):
            pos = wordnet.ADJ
        elif pos_tag.startswith('V'):
            pos = wordnet.VERB
        elif pos_tag.startswith('R'):
            pos = wordnet.ADV
        else:
            pos = wordnet.NOUN

        lemma = lemmatizer.lemmatize(token, pos)

        if lemma not in stopwords and len(lemma) >= 2:
            lemmatized_tokens.append(lemma)

    return lemmatized_tokens

def preprocess_text(text, stopwords = {}):
    # do not modify this function
    cleaned_text = clean_text(text)
    tokens = tokenize(cleaned_text)
    return lemmatize(tokens, stopwords)

"""
WORD --> SENTIMENT
1. Adjective dataset with words and sentiment
    - training dataset
    - probability of next instance being positive or negative
"""
"""
def build word table(training df, alpha = 1.0):
- count eah word once per sentence
- Smoothing? If yes --> Laplace smoothing
- log_odds(w) = log P(word|position in sentence) - log P(word|negative)
- p_positive(word) = sigmoid(log_odds + prior logs-odds)
- return table data frame, model dictionary used by predict
"""

"""def predict (tokens, model):
return (label, p_positive). For now - unseen words are ignored**
"""

"""
def evaluate(testing df, model):
- predict sentiment (pos or neg) for testing set using 
predict(tokens for testing set, model)
- report accuracy ((TP + TN)/ (TP + TN + FP + FN))
- report precision ((TP) / (TP + FP))
- report recall ((TP) / (TP + FN))
"""


"""
WORD + SENTIMENT --> EMOTION
    - intensity
    - word + sentiment + probability --> fits emotion, or categorize it as its own
"""

## Turn .txt into db with "text" and "score"
## 1 = positive
## 0 = negative
## 2 training sets 1 test set 

