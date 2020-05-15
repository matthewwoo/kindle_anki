from models import Card
import pandas as pd

# Ankify Methods

def book_md_ankify(md_list):
    highlights = []
    note_highlights = []
    notes = []
    for i in range(0, len(md_list)): 
        if md_list[i][0] == "*": 
            md_list[i] = md_list[i].lstrip("**Note:**")
            md_list[i] = md_list[i].strip()
            notes.append(md_list[i])
            note_highlights.append(md_list[i-2])
        elif md_list[i][0] == "#": 
            md_list[i] = md_list[i].lstrip("#")
            md_list[i] = md_list[i].strip()
            title = md_list[i]
        elif md_list[i][0] == "": 
            continue 
        else:
            highlights.append(md_list[i])
    return title, notes, note_highlights

def html_ankify(html_list):
    note_highlights = []
    notes = []
    for i in range(0, len(html_list)):
        if i % 2: 
            note_highlights.append(html_list[i])
        else: 
            notes.append(html_list[i])
    return note_highlights, notes

def book_md_kindle_direct_ankify(md_list):
    notes = []
    note_highlights = []
    highlights = []
    md_list_highlights = md_list
    for i in range(0,9):
        print(i,md_list_highlights[i])

    title = md_list[0].replace(" ","-").rstrip('\n')
    author = md_list[1].replace(" ","-").rstrip('\n')
    print(md_list[4][0:5])
    for i in range(2, len(md_list)):     
        if md_list[i][0:5] == "NOTE:":
            md_list[i] = md_list[i].lstrip("NOTE:")
            md_list[i] = md_list[i].strip()
            notes.append(md_list[i])
            note_highlights.append(md_list[i-1] + '\n' + md_list[i+1])
        else:
            continue
    for i in range(2,len(md_list_highlights)): 
        if md_list_highlights[i][0:9] == "LOCATION:" and md_list_highlights[i-1][0:5] == "NOTE:":
            continue
        elif md_list_highlights[i] == "" :
            continue 
        else:
            highlights.append(md_list_highlights[i])
            # highlights.append(md_list_highlights[i-1] + "\n" + md_list_highlights[i])
    return title, author, notes, note_highlights, highlights


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

