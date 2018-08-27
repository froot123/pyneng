# -*- coding: utf-8 -*-
'''
Задание 5.1b

Преобразовать скрипт из задания 5.1a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv

address = argv[1].split('.')
netmask_short = int(argv[2])

address_bin = [bin(int(x))[2:].zfill(8) for x in address]

netmask_str = '1' * netmask_short + '0' * (32 - netmask_short)
netmask_bin = [netmask_str[i:i+8] for i in range(0, 32, 8)] 
print(netmask_bin)
netmask_long = [int(x,2) for x in netmask_bin]

print('''
Network:
{:<8}  {:<8}  {:<8}  {:<8}
{}  {}  {}  {}

Mask:
/{}
{:<8}  {:<8}  {:<8}  {:<8}
{}  {}  {}  {}
'''.format(*[int(address[i])&int(netmask_long[i]) for i in range(4)],
	*address_bin,
	netmask_short,
	*netmask_long,
	*netmask_bin))
