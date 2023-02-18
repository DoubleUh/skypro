import requests
import random
from basicword import BasicWord

def load_random_word():
    request = requests.get('https://www.jsonkeeper.com/b/ZS8F')
    words = request.json()
    word = random.choice(words)
    base_word = BasicWord(word["word"], word["subwords"])
    return base_word

