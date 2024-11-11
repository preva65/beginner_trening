    #point 2
my_dict= {'Paul': 1965, 'Ivan': 1964, 'Piter': 1989}
print('Dict:', (my_dict))
print('Existing value:', (my_dict['Ivan']))
print('No existing value:', (my_dict.get('Serg')))
my_dict.update({'Victor': 2001, 'Iren': 2003})
print('Modified dictionary 1:', (my_dict))
del my_dict['Paul']
print('Modified dictionary 2:', (my_dict))
b= my_dict.pop('Piter')
print('Deleted value:', (b))

    #point 3
my_set= {1, 1, 2, 3, 5, 'ACTG','ATCG', 'GCTA', 'ACTG', (1, 2.2, 3.3)}
print('Set:', (my_set))
my_set.update([345, 'TTCC'])
my_set.remove('ACTG')
print('Modified set:', (my_set))