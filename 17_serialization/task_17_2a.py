# -*- coding: utf-8 -*-
'''
Задание 17.2a

С помощью функции parse_sh_cdp_neighbors из задания 17.2,
обработать вывод команды sh cdp neighbor из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Объединить все словари, которые возвращает функция parse_sh_cdp_neighbors,
в один словарь topology и записать его содержимое в файл topology.yaml.

Структура словаря topology должна быть такой:
{'R4': {'Fa0/1': {'R5': 'Fa0/1'},
        'Fa0/2': {'R6': 'Fa0/0'}},
 'R5': {'Fa0/1': {'R4': 'Fa0/1'}},
 'R6': {'Fa0/0': {'R4': 'Fa0/2'}}}

При этом интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

Не копировать код функции parse_sh_cdp_neighbors
'''
 
from task_17_2 import parse_sh_cdp_neighbors
import glob
import yaml
from pprint import pprint

if __name__ == '__main__':
	
	files = glob.glob('sh_cdp_n_*.txt')
	
	topology = {}
	# Объединить все словари, которые возвращает функция parse_sh_cdp_neighbors,
    #в один словарь topology
	for i in files:
		with open(i, 'r') as f:
			topology.update(parse_sh_cdp_neighbors(f.read()))
	
	# записать его содержимое в файл topology.yaml
	with open('topology.yaml', 'w') as f:
		yaml.dump(topology, f)
	

