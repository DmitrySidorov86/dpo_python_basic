import copy


def deepcopy(simpl, number, site_dict={}):
    deepcopy_site = copy.deepcopy(simpl)
    if number == 0:
        return
    product = input('Введите название продукта для нового сайта: ')
    deepcopy_site['html']['head']['title'] = 'Куплю/продам {} недорого'.format(product)
    deepcopy_site['html']['body']['h2'] = 'У нас самая низкая цена на {}'.format(product)
    site_dict[product] = copy.deepcopy(deepcopy_site)
    for key, values in site_dict.items():
        print(f'Сайт для {key}:')
        print(values)
    deepcopy(site, number - 1)


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
site_number = int(input('Сколько сайтов:'))
deepcopy(site, site_number)
