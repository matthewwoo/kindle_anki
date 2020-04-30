from models import Note
import pandas as pd

def md_ankify(md_list):
    highlights = []
    notes = []
    for i in range(0, len(md_list)): 
        if md_list[i][0] == "**": 
            highlights.append(md_list[i-1])
        else:
            notes.append(md_list[i])
    print(highlights[0])


def html_ankify(html_list):
    highlights = []
    notes = []
    for i in range(0, len(html_list)):
        if i % 2: 
            highlights.append(html_list[i])
        else: 
            notes.append(html_list[i])

## Input the highlights & notes into the pandas dataframe 
# data = {'front': highlights, 'back': notes[:21]}

# df = pd.DataFrame(data)

# a = Note('desk' , 'front', 'back', 'test')
# print(a.deck)


