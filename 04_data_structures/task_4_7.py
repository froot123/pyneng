# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес в двоичную строку (без двоеточий).

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

MAC = 'AAAA:BBBB:CCCC'
MAC = MAC.replace(':', '')
print(*[bin(int(MAC[i:i+2], 16))[2:].zfill(8) for i in range(len(MAC)-2)])
	
