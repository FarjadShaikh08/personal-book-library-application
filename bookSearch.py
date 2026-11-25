# testing testing testing 

# NOT FINISHED :(
#Searching(ROUGH OUTLINE TO GET THE LOGIC AND IDEAS DOWN)
books = [
    {"Title": "Mistborn", "Aruthor": "Brandon Sanderson"}, {"Title": "Hunger Games", "Aruthor": "Suzanne Collins"}, {"Title": "Silent Patient", "Aruthor": "Alex Michaelides"}
]




#for BOOK  in books: # cycles through each book in the list and temporaley puts it in BOOK
  #  if bookPick in BOOK["Title"].lower() or bookPick in BOOK["Aruthor"].lower(): #checks to see if what the user wrote is inside BOOK
    #    print("Title:", BOOK["Title"])
    #    print("Author:", BOOK["Aruthor"]) 




def search_function(books, bookPick):
    information = []
    #########################################
    for BOOK in books:
        if bookPick.lower() in BOOK["Title"].lower() or bookPick.lower() in BOOK["Aruthor"].lower():
            information.append(BOOK)
    return information
#################################################################
bookPick = input("Search Book").lower() # Gets the users input
Finaloutput = search_function(books, bookPick)


for BOOK in Finaloutput :
    print("Title:", BOOK["Title"])
    print("Author:", BOOK["Aruthor"])

    #Not to SELF MAKE THE HANDLER FOR WHEN NO BOOK IN LIST &