import json
import re
import pickle
import os
import pprint

pp = pprint.PrettyPrinter(indent=4)

'''
    convert word:tag list to dict
    regex search to find each word from
    usrinpt_strfld in text
    get w indices as tuple srt_end_loc
    save to a file 
    NOTE: you need this format for your data:
    ("body of text", [(startindex, endindex, 'tag')])
'''
def loc_substr(text_body, usrinpt_strfld):
    # load previously saved data
    nerdat_l = []
    if os.path.exists('NERdata.p'):
        with open('NERdata.p', 'rb') as nerdat:
            nerdat_l.append(pickle.load(nerdat))

    print(usrinpt_strfld)
    usrinpt_strfld = '{'+str(usrinpt_strfld)+'}'
    wordtag_d = json.loads(usrinpt_strfld)
    loc_tag_l = []

    for word, tag in wordtag_d.items():
        try:
            srt_end_loc = re.search(word, text_body).span()
            print('location of', word, ' : ', srt_end_loc)
            loc_tag_l.append((srt_end_loc[0], srt_end_loc[1], tag))
        except AttributeError as ae:
            return word + " not found in text_body."
    data_tup = (text_body, {'entities':loc_tag_l})
    # with open('NERdata.p', 'a') as f:
    #     pickler = pickle.Pickler(f)
    #     for txt_dat in data_tup:
    #         pickler.dump(data_tup)
    # add new data to old data
    nerdat_l.append(data_tup)
    # sync the data
    with open('NERdata.p', 'wb') as nerdat:
        pickle.dump(nerdat_l, nerdat)
    # reload for verification
    with open('NERdata.p','rb') as nerdat:
        nerdat_l.append(pickle.load(nerdat))
    pp.pprint(nerdat_l)
    return data_tup


# def mkNER_data(data_tup):
#     if os.path.exists('NERdata.p'):
#         with open(data_tup, 'rb') as dt:
            
