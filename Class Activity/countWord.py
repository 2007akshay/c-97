introWord = input("enter your self ")
wordCount = 1
characterCount = 0 
for i in introWord:
        characterCount=characterCount+1
        if (i ==" "):
            wordCount=wordCount+1
print("number of character : " )
print(characterCount)
print("number of words : ")
print(wordCount)


