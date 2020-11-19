import json
import csv
import re

def loc_substr(text, word):
    word = '{'+word+'}'
    word_tag_dict = json.loads(word)
    word_dat_l = []
    for w,t in word_tag_dict.items():
        try:
            srt_end_loc = re.search(w, text).span()
            print('endpoints of string', srt_end_loc)
            # TODO: create a csv file, or append to csv file
            word_data = {}
            word_data["text"] = text
            word_data["word"] = w
            word_data["startIndx"] = srt_end_loc[0]
            word_data["endIndx"] = srt_end_loc[1]
            word_data["tag"] = t
            with open('nerdata.csv', 'a') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=['text','word','startIndx','endIndx','tag'])
                writer.writeheader()
                for data in word_data:
                    writer.writerow(data)
            outfile.close()
            word_dat_l.append(word_data)
        except AttributeError as ae:
            return w + " not found in text."
    return word_dat_l
