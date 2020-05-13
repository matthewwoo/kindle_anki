import scraper as s
import ankify as a
import anki_connect as ac
import json

book = "/Users/matthewwoo/Desktop/Kindle_Anki/The Little Book of Common Sense Investing by John C. Bogle.md"
md_list = s.md_notes(book)
result = a.book_md_ankify(md_list)
title = result[0].replace(" ","-")
print(title)
notes = result[1]
note_highlights = result[2]
tags = [title,"Investing","Index Funds", "John-C.-Bogle"]
print(tags)
print(notes[1])
print(len(notes))
for i in range(0,len(notes)):
    card = a.cardify(notes[i],note_highlights[i],tags)
    card = card.anki_jsonify()
    result = ac.invoke('addNote',note=card)
print("done")


# test_card = a.cardify(result[1],result[2],"test")
# print(test_card.front)
# print(test_card.back)
# x = test_card.anki_jsonify()
# ac.invoke('addNote',note=x)
# ac.invoke('createDeck', deck='test1')




