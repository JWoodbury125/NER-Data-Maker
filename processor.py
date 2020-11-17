import json
import re

def loc_substr(text, word):
    srt_end_loc = re.search(word, text).span()
    print('poop', srt_end_loc)
    return srt_end_loc, text, word

# if __name__ == "__main__":
#     texts = 'poop pop peep'
#     word = 'pop'
#     print(type(loc_substr(texts, word)))