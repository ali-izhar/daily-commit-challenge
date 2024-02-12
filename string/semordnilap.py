"""
PROBLEM: Semordnilap
A semordnilap is a word or a phrase that spells a different word when backwards ("semordnilap" is a semordnilap of "palindromes").

words = ["diaper", "abc", "test", "cba", "repaid"]
output = [["diaper", "repaid"], ["abc", "cba"]]
"""

def semordnilap(words):
    word_dict = {}
    result = []

    for word in words:
        if word[::-1] in word_dict:
            result.append([word, word[::-1]])
        word_dict[word] = True

    return result