

with open('recipes.txt', 'r', encoding='utf8') as f:
    cook_book = {}
    for line in f:
        ingredient = []
        if line != '\n':
            dish = line.strip('\n')
            count_ingrds = f.readline().strip('\n')
            for i in range(int(count_ingrds)):
                ingrds_dict = {}
                ingrds_list = f.readline().strip('\n').split(sep=' | ')
                ingrds_dict['ingridient_name'] = ingrds_list[0]
                ingrds_dict['quantity'] = ingrds_list[1]
                ingrds_dict['measure'] = ingrds_list[2]
                ingredient.append(ingrds_dict)
                cook_book[dish] = ingredient
print(cook_book)


