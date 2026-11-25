# testing testing testing 

# NOT FINISHED :(
#Searching(ROUGH OUTLINE TO GET THE LOGIC AND IDEAS DOWN)
books = [
    {"Title": "Mistborn", "Aruthor": "Brandon Sanderson"}, {"Title": "Hunger Games", "Aruthor": "Suzanne Collins"}, {"Title": "Silent Patient", "Aruthor": "Alex Michaelides"}
]

bookPick = input("Search Book").lower() # Gets the users input
for BOOK  in books: # cycles through each book in the list and temporaley puts it in BOOK
    if bookPick in BOOK["Title"].lower() or bookPick in BOOK["Aruthor"].lower(): #checks to see if what the user wrote is inside BOOK
        print("Title:", BOOK["Title"])
        print("Author:", BOOK["Aruthor"])




