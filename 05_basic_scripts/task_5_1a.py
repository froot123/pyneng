# -*- coding: utf-8 -*-
'''
Задание 5.1a

Всё, как в задании 5.1. Но, если пользователь ввел адрес хоста, а не адрес сети,
то надо адрес хоста преобразовать в адрес сети и вывести адрес сети и маску, как в задании 5.1.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

prefix = input('Prefix: ')

address = prefix.split('/')[0].split('.')
netmask_short = int(prefix.split('/')[1])

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





