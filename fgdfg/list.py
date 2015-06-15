import sys
import os
import random

gro_list = ['Juice','Tomato','Orange','Banana','Ma']
print('Grocesoty list : ',gro_list[2])
#gro_list[2] = 'Jira'
print('Grocesoty list : ',gro_list)
print(gro_list[1:3])

other_list = ['My Car','Volswagan','Toyta','Sanyoung','BMW']

to_do_list=[other_list,gro_list]
print(to_do_list)
print('\n'*2)
print(to_do_list[0][2:4])
''' append'''

gro_list.append('Onion')
print(to_do_list)
print('List Operation')
print('\n'*2)
gro_list.insert(1,'Pickel')
print('Insert OPeration ###### ')
print('\n'*1)
print(to_do_list)
gro_list.remove('Pickel')
gro_list.sort()
gro_list.reverse()
del gro_list[4]

print(to_do_list)
oto_do_list = gro_list+other_list
print(len(oto_do_list))
print(max(oto_do_list))
print(min(oto_do_list))