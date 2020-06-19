import scraper as s
import ankify as a
import anki_connect as ac
import json
import os
import shutil


to_upload_directory = "/Users/matthewwoo/Desktop/Kindle_Anki/Material/to_upload"
uploaded_directory = "/Users/matthewwoo/Desktop/Kindle_Anki/Material/uploaded"
note_directory = "/Users/matthewwoo/Desktop/Kindle_Anki/Material/notes"

def anki_cardify_loop(ref):
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

def create_anki_cards(to_upload_directory, uploaded_directory):
    for filename in os.listdir(to_upload_directory):
        to_upload_ref = (to_upload_directory+"/"+filename)
        anki_cardify_loop(to_upload_ref)
        uploaded_ref = (uploaded_directory+"/"+filename)
        shutil.move(to_upload_ref, uploaded_ref)

def create_notes(to_upload_directory, note_directory, uploaded_directory):
    for filename in os.listdir(to_upload_directory):
        to_upload_ref = (to_upload_directory+"/"+filename)
        s.md_format(to_upload_ref,note_directory)
        uploaded_ref = (uploaded_directory+"/"+filename)
        shutil.move(to_upload_ref, uploaded_ref)    

def create_notes_and_anki_cards(to_upload_directory, note_directory, uploaded_directory):
    for filename in os.listdir(to_upload_directory):
        to_upload_ref = (to_upload_directory+"/"+filename)
        s.md_format(to_upload_ref,note_directory)
        anki_cardify_loop(to_upload_ref)
        uploaded_ref = (uploaded_directory+"/"+filename)
        shutil.move(to_upload_ref, uploaded_ref)    

# create_anki_cards(to_upload_directory,uploaded_directory)
# create_notes(to_upload_directory, note_directory, uploaded_directory)
# create_notes_and_anki_cards(to_upload_directory,note_directory,uploaded_directory)

file = '/Users/matthewwoo/Desktop/Kindle_Anki/matthewedanwoo.json'

roam_doc = open(file)
roam_json = json.load(roam_doc)
print(type(roam_json))
print(roam_json[0]['title'])
list_values = [ key for key,val in roam_json.items() if val==value ]
# def myprint(d):
#     for k, v in d.items():
#         if isinstance(v, dict):
#             myprint(v)
#         else:
#             print("{0} : {1}".format(k, v)) 

# myprint(roam_json)





