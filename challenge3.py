#!/usr/bin/python3

names = [ 'fluffy', 'spot', 'cujo' ]
ages = [ 3, 7, 12 ]
animal_type = [ 'cat', 'dog', 'mean dog' ]

pets = {}

i=0

for name in names:
    age = ages[i]
    species = animal_type[i]
    print(f'{name} {age} {species}')
    i += 1
    pets.update( { name:  { 'age' : age, 'animal_type' : species } } )

print()
print(pets)
print(type(pets))
print()

#####  ALTERNATIVELY  #####

pets = {}

for i in range(len(names)):
    pets.update( { names[i]:  { 'age' : ages[i], 'animal_type' : animal_type[i] } } )

print(pets)
print(type(pets))
