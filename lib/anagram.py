# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Convert the word to lowercase 

    def match(self, words):
        matches = []
        for w in words:
            # Check if the word is an anagram by comparing sorted letters
            if sorted(w.lower()) == sorted(self.word) and w.lower() != self.word:
                matches.append(w)
        return matches