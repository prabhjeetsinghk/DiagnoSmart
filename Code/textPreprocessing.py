import warnings
warnings.filterwarnings('ignore')
from textblob import TextBlob
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


class proccessing:
    stop_words = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()

    def clean_duplicate(text, self):
        words = text.split()
        unique_words = set()
        result = []
        for word in words:
            if word not in unique_words:
                unique_words.add(word)
                result.append(word)

        cleanedData =  ' '.join(result)
        cleanedData = self.cleandata1(cleanedData)
        embedding = self.embeddings(cleanedData)
        return embedding

    def cleandata1(text, self):
        tag_mapping = {
        'NN': 'n',
        'NNS': 'n',
        'NNP': 'n',
        'NNPS': 'n',
        'VB': 'v',
        'VBD': 'v',
        'VBG': 'v',
        'VBN': 'v',
        'VBP': 'v',
        'VBZ': 'v',
        'JJ': 'a',
        'JJR': 'a',
        'JJS': 'a',
        'RB': 'r',
        'RBR': 'r',
        'RBS': 'r',
        'WRB':'r'
        }
        text = "".join([word.lower() for word in re.sub(r"[^a-zA-Z]", " ", text)])
        tokens = word_tokenize(text)
        text = [word for word in tokens if len(word)>2 or word not in stop_words]
        text = " ".join([lemmatizer.lemmatize(word, pos='n' if tag_mapping.get(TextBlob(word).tags[0][1]) == None else tag_mapping.get(TextBlob(word).tags[0][1])) for word in text])
        return text

    def embeddings(text, self):
        module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
        model = hub.load(module_url)
        embed = model(text)

    def 