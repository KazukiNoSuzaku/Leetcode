# Transform each word to Goat Latin: vowel-starting gets 'ma', consonant-starting rotates + 'ma'.

# Author: Kaustav Ghosh

class Solution(object):
    def toGoatLatin(self, sentence):
        vowels = set('aeiouAEIOU')
        res = []
        for i, word in enumerate(sentence.split(), 1):
            if word[0] in vowels:
                res.append(word + 'ma' + 'a' * i)
            else:
                res.append(word[1:] + word[0] + 'ma' + 'a' * i)
        return ' '.join(res)
