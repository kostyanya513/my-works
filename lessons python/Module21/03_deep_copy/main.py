site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}
import copy


def creating_website(structure_site, product):
    if isinstance(structure_site, (int, float, bool, str)):
        new_list = []
        for index_struc in structure_site.split():
            if index_struc == 'телефон' or index_struc == 'iphone':
                index_struc = product
            new_list.append(index_struc)
        return ' '.join(new_list)
    elif isinstance(structure_site, dict):
        return {key: creating_website(value, product) for key, value in structure_site.items()}


list_site = []
quantity = int(input('Сколько сайтов: '))
for website in range(quantity):
    name_website = input('Введите название продукта для нового сайта:  ')
    print('Сайт для {}:'.format(name_website))
    next_site = copy.deepcopy(site)
    list_site.append(creating_website(next_site, name_website))
    for index in range(len(list_site)):
        print('sate =', list_site[index])
