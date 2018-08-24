import random


def fresh_array():
	return [random.randint(1,100) for x in range(100)]

	
def bubble(a):
	last = len(a)
	while last > 0:
		for i in range(len(a)-1):
			if a[i] > a[i+1]:
				a[i], a[i+1] = a[i+1], a[i]
		last -= 1


def insert(a):
	for i in range(len(a)):
		j = i
		while j > 0 and a[j] < a[j-1]:
			a[j], a [j-1] = a[j-1], a[j]
			j -= 1


def select(a):
	for i in range(len(a)):
		min_index = i
		for j in range(i+1, len(a)):
			if a[j] < a[min_index]:
				min_index = j
		a[i], a[min_index] = a[min_index], a[i]
		

def merge(a):
	if len(a) < 2:
		return
	
	#sort
	left = a[:len(a)//2]
	right = a[len(a)//2:]
	
	merge(left)
	merge(right)
	
	#merge
	i = j = k = 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			a[k] = left[i]
			i += 1 
		else:
			a[k] = right[j]
			j += 1
		k += 1
		
	while i < len(left):
		a[k] = left[i]
		i += 1
		k += 1
	while j < len(right):
		a[k] = right[j]
		j += 1
		k += 1

def qsort(a):
	if len(a) < 2:
		return a
	barrier = random.choice(a)
	left = [x for x in a if x < barrier]
	mid = [barrier] * a.count(barrier)
	right = [x for x in a if x > barrier]
	return qsort(left) + mid + qsort(right)



test = fresh_array()
print(test)
#merge(test)
print(qsort(test))
		
