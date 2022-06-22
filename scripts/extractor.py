from PyPDF2 import PdfFileReader

reader = PdfFileReader("pfe.pdf")
number_of_pages = reader.numPages

def isAbb(word:str):
    return word.isalnum() and len(word) > 1 and word.isupper() 

list_of_abbreviations = set()
for i in range(number_of_pages):
    page = reader.pages[i]
    text = page.extractText()
    words = text.split()
    extracted = list(filter(isAbb, words))
    for word in extracted: 
        list_of_abbreviations.add(word)

print(list_of_abbreviations)