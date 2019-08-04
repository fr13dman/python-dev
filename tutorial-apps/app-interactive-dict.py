import json
import os

from difflib import get_close_matches

fn = os.path.join(os.path.dirname(__file__), "data/data.json")
data = json.load(open(fn))

def translate(word):
    w = word.lower()
    if w in data:
        return data[w]
    
    w = get_close_matches(w, data.keys())
    if len(w) > 0:
        _in = input("Did you mean %s instead (y/n)? " % (w[0]))
        if (_in.lower() == 'n'):
            return "The word doesn't exist. Please double check it!"
        else:
            return data[w[0]]
    else:
        return "The word doesn't exist. Please double check it!"

word = input("Enter word: ")
output = translate(word)

if type(output) == list:
    cnt = 1
    for w in output:
        print("%d: %s" % (cnt, w))
        cnt += 1
else:
    print("%d: %s" % (++cnt, output))