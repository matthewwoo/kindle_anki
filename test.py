import scraper as s
import ankify as a

md_list = s.md_notes("/Users/matthewwoo/Desktop/Kindle_Anki/Why We Sleep by Matthew Walker.md")
a.md_ankify(md_list)

