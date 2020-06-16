import scraper as s
import ankify as a
import anki_connect as ac
import json
import os
import shutil


to_upload_directory = "/Users/matthewwoo/Desktop/Kindle_Anki/Material/to_upload"
uploaded_directory = "/Users/matthewwoo/Desktop/Kindle_Anki/Material/uploaded"

for filename in os.listdir(to_upload_directory):
    to_upload_ref = (to_upload_directory+"/"+filename)
    uploaded_ref = (uploaded_directory+"/"+filename)
    shutil.move(to_upload_ref, uploaded_ref)    
    
def upload_loop():
    md_list = s.md_notes(ref)
    result = a.book_md_kindle_direct_ankify(md_list)
    title = result[0]
    author = result[1]
    notes = result[2]
    note_highlights = result[3]
    highlights = result[4]
    tags = [title, author]
    for i in range(0,len(notes)):
        card = a.cardify(notes[i],note_highlights[i],tags)
        card = card.anki_jsonify()
        print(i)
        try:
            result = ac.invoke('addNote',note=card)
        except: 
            pass
    print("done")




