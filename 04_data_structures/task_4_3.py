# -*- coding: utf-8 -*-
'''
Задание 4.3

Получить из строки CONFIG список VLANов вида:
['1', '3', '10', '20', '30', '100']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
VLANS = [int(x.strip()) if x.isdigit() else int(x[x.rfind(' ') + 1:].strip()) for x in CONFIG.split(',')]
print(VLANS)
