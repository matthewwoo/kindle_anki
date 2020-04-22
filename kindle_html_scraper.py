from bs4 import BeautifulSoup
html_doc = open('/Users/matthewwoo/Desktop/Kindle_Anki_Script/Story10x.html')
soup = BeautifulSoup(html_doc,'html.parser')
noteTexts = soup.find_all('div',{'class':'noteText'})
noteTexts_list = []
for note in noteTexts:
    noteTexts_list.append(note)
print(noteTexts_list[0])
print(noteTexts_list[1])





