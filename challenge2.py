cars = {'number': 3,
        'vehicles':  [{'brand': 'Kia', 'model': 'Soul'},
                      {'brand': 'Tesla', 'model': 'ModelS'},
                      {'brand': 'Chevy', 'model': 'Tahoe'}],
        'colors': ['red', 'white', 'blue']}


#print(cars)

#print(f'I have {cars["number"]} cars; a {cars["colors"][0]} {cars["vehicles"][0]["brand"]} {cars["vehicles"][0]["model"]}, a {cars["colors"][1]} {cars["vehicles"][1]["model"]} {cars["vehicles"][1]["brand"]}, and a {cars["colors"][2]} {cars["vehicles"][2]["model"]} {cars["vehicles"][2]["brand"]}.')

print(f'I have {cars["number"]} cars')

i=0

while i < cars['number']:
    color=cars['colors'][i]
    print(f'a {color}')

    car=cars['vehicles'][i]

    print(car)

    j=0
    while j < 2:
        print(f'{car[j]}')
        j += 1

    i += 1
