from models import Card
import pandas as pd

# Ankify Methods

## Readwise
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

## Kindle HTML via Kindle App 
def html_ankify(html_list):
    note_highlights = []
    notes = []
    for i in range(0, len(html_list)):
        if i % 2: 
            note_highlights.append(html_list[i])
        else: 
            notes.append(html_list[i])
    return note_highlights, notes

## Kindle via Bookcision
def book_md_kindle_direct_ankify(md_list):
    notes = []
    note_highlights = []
    highlights = []
    title = md_list[0].replace(" ","-").rstrip('\n')
    author = md_list[1].replace(" ","-").rstrip('\n')
    # Notes & Note Highlight Arrays
    for i in range(2, len(md_list)):     
        if md_list[i][0:5] == "NOTE:":
            md_obj = md_list[i]
            md_highlight = md_list[i-1]
            md_location = md_list[i+1]
            md_obj = md_obj.lstrip("NOTE:").strip()
            notes.append(md_obj)
            note_highlights.append(md_highlight + '\n' + md_location)
            # note_highlights.append(md_highlight + '\n' + title + author + '\n' + md_location)
        else:
            continue

    # Highlights Array
    for i in range(2, len(md_list)):     
        if md_list[i][0:9] == "LOCATION:" and md_list[i-1][0:5] != "NOTE:":
            h_obj = md_list[i-1]
            h_location = md_list[i]
            h_obj = h_obj + "\n" + h_location
            highlights.append(h_obj)
        else:
            continue
    
    return title, author, notes, note_highlights, highlights    

## Creating a Card
def cardify(notes,note_highlights,tags):
    deck ="default"
    return Card(deck,notes,note_highlights,tags)
    
