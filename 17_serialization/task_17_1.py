# -*- coding: utf-8 -*-
'''
Задание 17.1

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Для выполнения задания нужно создать две функции.

Функция parse_sh_version:
* ожидает аргумент output в котором находится вывод команды sh version (не имя файла)
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"

Функция write_to_csv:
* ожидает два аргумента:
 * имя файла, в который будет записана информация в формате CSV
 * данные в виде списка списков, где:
    * первый список - заголовки столбцов,
    * остальные списки - содержимое
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает

Остальное содержимое скрипта может быть в скрипте, а может быть в ещё одной функции.

Скрипт должен:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в файл routers_inventory.csv

В файле routers_inventory.csv должны быть такие столбцы:
* hostname, ios, image, uptime

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается на sh_vers.
Вы можете раскомментировать строку print(sh_version_files), чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.
'''

import glob
import re
import csv


headers = ['hostname', 'ios', 'uptime', 'image']


def parse_sh_version(output):
	r = re.compile('\), Version '
		'(?P<ios>\S+)'
		',.+router uptime is '
		'(?P<uptime>\d+\s\w+,\s\d+\s\w+,\s\d+\s\w+)'
		'.+System image file is '
		'(?P<image>\"\S+\")', re.DOTALL)
	m = re.search(r, output)
	if m:
		print(m.groups())
		return m.groups() 
	
	
def write_to_csv(filename, data):
	with open(filename, 'w') as f:
		writer = csv.writer(f)
		for row in data:
			writer.writerow(row)
		

sh_version_files = glob.glob('sh_vers*')
# print(sh_version_files)

data = [headers]

for i in sh_version_files:
	hostname = [i[i.rindex('_')+1: i.index('.')]]
	with open(i, 'r') as f:
		hostname.extend(list(parse_sh_version(f.read())))
		data.append(hostname)

write_to_csv('routers_inventory.csv', data)

