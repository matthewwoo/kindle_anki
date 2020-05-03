from models import Card
import pandas as pd

# Ankify Methods

def book_md_ankify(md_list):
    highlights = []
    note_highlights = []
    notes = []
    for i in range(0, len(md_list)): 
        if md_list[i][0] == "*": 
            notes.append(md_list[i])
            note_highlights.append(md_list[i-2])
        elif md_list[i][0] == "#": 
            title = md_list[i]
        elif md_list[i][0] == "": 
            continue 
        else:
            highlights.append(md_list[i])
    return title, note_highlights, notes

def html_ankify(html_list):
    note_highlights = []
    notes = []
    for i in range(0, len(html_list)):
        if i % 2: 
            note_highlights.append(html_list[i])
        else: 
            notes.append(html_list[i])
    return note_highlights, notes

# Creating a Card

def cardify(notes,note_highlights,tags):
    deck ="default"
    return Card(deck,notes,note_highlights,tags)
    

# def deckify(highlights,note_highlights,notes): 



## Input the highlights & notes into the pandas dataframe 
# data = {'front': highlights, 'back': notes[:21]}

# df = pd.DataFrame(data)

# a = Note('desk' , 'front', 'back', 'test')
# print(a.deck)

