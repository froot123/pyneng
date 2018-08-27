# -*- coding: utf-8 -*-
'''
Задание 5.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

prefix = input('Network: ')
net_addr, mask = prefix.split('/')[0].split('.'), int(prefix.split('/')[1])
net_addr_bin = [bin(int(x))[2:].zfill(8) for x in net_addr]
mask_bin = ('1' * mask) + ('0' * (32-mask))
mask_bin_list = [mask_bin[0:8], mask_bin[8:16], mask_bin[16:24], mask_bin[24:32]]

print("""Network:
{:<8}  {:<8}  {:<8}  {:<8}
{}  {}  {}  {}

Mask:
/{}
{:<8}  {:<8}  {:<8}  {:<8}
{}  {}  {}  {}
""".format(*net_addr, 
	*net_addr_bin,
	mask,
	*[int(x,2) for x in mask_bin_list],
	*mask_bin_list))
	
