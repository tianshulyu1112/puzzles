def find_anagrams(word, candidates):
    
    anag = []
    for elem in candidates:
        if (sorted(word) == sorted(elem)):
            anag.append(elem)
    if anag:
        print(anag)
    else:
        print('No anagrams found')
        
