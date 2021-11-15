i = 0

txt = input("input text to search: ")
txt = txt.lower()
txtarry = txt.split()

search = input("Please input word to search for: ")
search = search.lower()
print("")

while(i < len(txtarry)):
    if(str(search) == txtarry[i]):
        print(search, " has been found in the given words")
        input("")
        quit()
    else:
        print(txtarry[i], "does not match the given search word")
        print("")
    i = i + 1
input("")
quit()