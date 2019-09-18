def abbreviate(words):
    bad_chars = [';', ':', '!', '*','-','\\','_']
    word = words.upper()
    for i in bad_chars : 
        word = word.replace(i, ' ') 
    wrds = word.split() 
    #print(wrds)
    hahah = []
    count = len(wrds)
    for i in range(count):
       hahah.append(wrds[i][0]) 
       i += 1
    acronym = "".join(hahah)
    string = str(acronym)
    return string 


       

