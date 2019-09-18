def abbreviate(words):
    wrds = words.split()
    #print(wrds)
    hahah = []
    count = len(wrds)
    for i in range(count):
       hahah.append(wrds[i][0]) 
       i += 1
    acronym = "".join(hahah)
    print(acronym)
        
abbreviate("Portable Network Graphics")
        
    
