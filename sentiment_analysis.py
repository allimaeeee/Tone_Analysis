nltk.download("stopwords", quiet = True)
nltk.download("wordnet", quiet = True)
nltk.download("punkt", quiet = True)
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('averaged_perceptron_tagger', quiet = True)
lemmatizer = WordNetLemmatizer()
english_stopwords = set(nltk.corpus.stopwords.words('english'))

"""
WORD --> SENTIMENT
1. Adjective dataset with words and sentiment
    - training dataset
    - probability of next instance being positive or negative


WORD + SENTIMENT --> EMOTION
    - intensity
    - word + sentiment + probability --> fits emotion, or categorize it as its own
"""

## Turn .txt into db with "text" and "score"
## 1 = positive
## 0 = negative
## 2 training sets 1 test set 

