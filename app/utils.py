import re
import string

def preprocess(text):
    """
    Lowercases and removes punctuation from input text.
    """
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)
    return text
