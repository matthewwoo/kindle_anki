from bs4 import BeautifulSoup
from models import Note
import pandas as pd

# Open the HTML and store all highlight in a list
html_doc = open('/Users/matthewwoo/Desktop/Kindle_Anki/Story10x.html')
soup = BeautifulSoup(html_doc,'html.parser')
noteTexts = soup.find_all('div',{'class':'noteText'})
noteTexts_list = []
for note in noteTexts:
    noteTexts_list.append(note)

# Open Markdown to store all highlights 
def md_highlights(file):
    md_doc = open(file)
    md_Texts_list = []
    with md_doc as md: 
        for line in md: 
            md_Texts_list.append(line)
    return md_Texts_list

# Store all the highlights and notes into separate list
highlights = []
notes = []

for i in range(0, len(noteTexts)):
    if i % 2: 
        highlights.append(noteTexts[i])
    else: 
        notes.append(noteTexts[i])

## Input the highlights & notes into the pandas dataframe 
data = {'front': highlights, 'back': notes[:21]}

df = pd.DataFrame(data)

a = Note('desk' , 'front', 'back', 'test')
print(a.deck)


