def get_shop_list_by_dishes(dishes, person_count):
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
            cook_book1.setdefault(j[0], [])
            for k in range(int(j[1])):
                n = {'ingredient_name': '', 'quantity': '', 'measure': ''}
                s = (j[2 + k].split('|'))
                n['ingredient_name'] = s[0].strip()
                n['quantity'] = int(s[1])
                n['measure'] = s[2].strip()
                cook_book1[j[0]].append(n)

    final = {}
    for m in dishes:
        if m in cook_book1.keys():
            for b in cook_book1[m]:
                y = {'measure': '', 'quantity': ''}
                x = b.values()
                final.setdefault(list(x)[0],y)
                y['quantity'] = (list(x)[1] * person_count)
                y['measure'] = list(x)[2]
        else:
            print("В списке блюд утверждённых для банкета, данное блюдо к сожалению отсутствует")
    return print(final)


get_shop_list_by_dishes(['Омлет'], 2)
