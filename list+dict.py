my_var = []
your_var = {}

my_var += ['fluffy', 'kaya', 'max']
my_var.append('butch')
my_var.extend('tom')
print(my_var[0::2])

your_var.update({'dog': 'cujo'})
your_var['lizards'] = ['larry', 'beardy']
print(your_var)

###################################################

my_var = []
your_var = {}

my_var += ['fluffy', 'kaya', 'max']
my_var.append('butch')
my_var.extend('tom')
print(my_var[0::2])

your_var.update({'dog': 'cujo'})
your_var['lizards'] = ['larry', 'spot', 'beardy']
print(your_var)
print(your_var['lizards'][1])
                                          
