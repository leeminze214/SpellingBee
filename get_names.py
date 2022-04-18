with open('food.txt') as a:
    aa = list(a)
fin =[]
for i in aa:
    if '-' in i or '&' in i:
        aa.remove(i)
    else:
        
        fin.append(i[0].capitalize()+i[1:-1])
print(set(fin))
    
