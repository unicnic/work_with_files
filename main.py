

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
                ingrds_dict['ingredient_name'] = ingrds_list[0]
                ingrds_dict['quantity'] = ingrds_list[1]
                ingrds_dict['measure'] = ingrds_list[2]
                ingredient.append(ingrds_dict)
                cook_book[dish] = ingredient


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for i in range(len(cook_book[dish])):
            if cook_book[dish][i]['ingredient_name'] not in shop_list.keys():
                shop_list[cook_book[dish][i]['ingredient_name']] = {'measure' : cook_book[dish][i]['measure'], 'quantity' : int(cook_book[dish][i]['quantity']) * person_count}
            else:
                shop_list[cook_book[dish][i]['ingredient_name']]['quantity'] += int(cook_book[dish][i]['quantity']) * person_count
    return shop_list


