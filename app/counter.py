import re

def count_word(text, word):
    words = re.findall(r'\b\w+\b', text.lower())
    
    print("WORDS:", words)   # 👈 DEBUG
    
    return words.count(word.lower())
