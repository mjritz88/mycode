#!/usr/bin/python3

names = [ 'fluffy', 'spot', 'cujo' ]
ages = [ 3, 7, 12 ]
animal_type = [ 'cat', 'dog', 'mean dog' ]

pets = {}

count=0

for name in names:
    age = ages[count]
    atype = animal_type[count]
    print(f'{name} {age} {atype}')
    count += 1
    pets.update( { name:  { "age" : age, "animal_type" : atype } } )

type(pets)
print(pets)
