from bs4 import BeautifulSoup
import pandas as pd
import os
import shutil
import json

# Open the HTML and store all highlight in a list
def html_notes(file):
    html_doc = open(file)
    soup = BeautifulSoup(html_doc,'html.parser')
    noteTexts = soup.find_all('div',{'class':'noteText'})
    noteTexts_list = []
    for note in noteTexts:
        noteTexts_list.append(note)

# Open Markdown to store all highlights 
def md_notes(file):
    md_doc = open(file)
    md_Texts_list = []
    with md_doc as md: 
        for line in md: 
            md_Texts_list.append(line)
    return md_Texts_list

## Format Kindle Layout for Notes 
def md_format(file, directory): 
    md_doc = open(file)
    md_list = md_doc.readlines()
    title = md_list[0]
    md_lines = []
    for i in range(0, len(md_list)): 
        if md_list[i][0:5]=="NOTE:" or md_list[i][0:9]=="LOCATION:": 
            md_obj = md_list[i]
            md_obj = "\t" + md_obj
            md_lines.append(md_obj)
        else:
            md_obj = md_list[i]
            md_lines.append(md_obj)
    f = open(title +'.txt',"w+")
    file_title = "/" + title + ".txt"
    for i in range(0, len(md_lines)): 
        f.write(md_lines[i])
    f.close()
    shutil.move(os.getcwd()+file_title, directory+file_title)

## Get Roam Entire JSON library 
def roam(file): 
    roam_doc = open(file)
    roam_json = json.load(roam_doc)
    print(roam_json)

    

    


