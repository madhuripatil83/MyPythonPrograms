def pig_latin(word):

    res = vowel_checker(word)
    if(res == 1):
       print("String consists of first letter as vowel")
    else:
       consonant_checker(word)

def vowel_checker(word):
    if(word[0] == 'a'):
      word = word +"way"
    elif(word[0] == 'e'):
      word = word +"way"
    elif(word[0] == 'i'):
      word = word +"way"
    elif(word[0] == 'o'):
      word = word +"way"
    elif(word[0] == 'u'):
       word = word +"way"
    else:
        print("Searched till end and found no vowels!!") 
        return 0
    print(word)
    return 1

def consonant_checker(word):
     letter = word[0]
     strlen = len(word)
     remword = word [1 : strlen]
     flag = 0
     if(letter !='a'):
         flag = 1
     elif(letter != 'e'):
         flag = 1
     elif(letter!='i'):
         flag =1
     elif(letter!='o'):
         flag=1
     elif(letter!='u'):
         flag =1
     if(flag == 1):
       remword = remword + letter + "ay"
       print(remword)
       
     
pig_latin("duck")

    
