with open('cook_book_start.txt', 'r+', encoding='UTF-8') as f:
    alldishes = []
    dish = []
    for i in f:
        if i != '\n':
            dish.append(i.rstrip('\n'))
        else:
            alldishes.append(dish)
            dish = []
    alldishes.append(dish)
    cook_book1 = {}
    
    for j in alldishes:
        cook_book1.setdefault(j[0],[])
        for k in range(int(j[1])):
            n = {'ingredient_name': '', 'quantity': '', 'measure': ''}
            s = (j[2+k].split('|'))
            n['ingredient_name'] = s[0].strip()
            n['quantity'] = s[1].strip()
            n['measure'] = s[2].strip()
            cook_book1[j[0]].append(n)
    print(cook_book1)
