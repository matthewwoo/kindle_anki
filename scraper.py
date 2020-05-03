from bs4 import BeautifulSoup
import pandas as pd

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


