import scraper as s
import ankify as a
import anki_connect as ac
import json

book = "/Users/matthewwoo/Desktop/Kindle_Anki/Kindle.Highlights_Thinking.in.Systems.A.Primer_1588859187986.txt"
md_list = s.md_notes(book)
print(md_list[0])
result = a.book_md_kindle_direct_ankify(md_list)
# 0 = title
# 1 = author
# 2 = notes
# 3 = note_highlights 
# 4 = highlights
title = result[0]
author = result[1]
notes = result[2]
note_highlights = result[3]
highlights = result[4]
tags = [title, author]
print(tags)
print(notes[0])
print(note_highlights[0])
print(highlights[2])
print(len(notes))
# for i in range(0,len(notes)):
#     card = a.cardify(notes[i],note_highlights[i],tags)
#     card = card.anki_jsonify()
#     result = ac.invoke('addNote',note=card)
# print("done")


# test_card = a.cardify(result[1],result[2],"test")
# print(test_card.front)
# print(test_card.back)
# x = test_card.anki_jsonify()
# ac.invoke('addNote',note=x)
# ac.invoke('createDeck', deck='test1')




