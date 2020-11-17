import json
import re
import pandas as pd

def loc_substr(text, word):
    word = '{'+word+'}'
    word_tag_dict = json.loads(word)

    for w,t in word_tag_dict.items():
        try:
            srt_end_loc = re.search(w, text).span()
            print('poop', srt_end_loc)
            # TODO: create a csv file, or append to csv file
        except AttributeError as ae:
            return w + " not found in text."
    return srt_end_loc, text, word

# if __name__ == "__main__":
#     texts = 'poop pop peep'
#     word = 'pop'
#     print(type(loc_substr(texts, word)))