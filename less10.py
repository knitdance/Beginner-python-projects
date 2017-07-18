list1 = [1, 1, 10, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for element in list1:
	if element < 5:
		print(element)
#this prints numbers less than 5, one by one: 1, 1, 2, 3 
############

list2 = []
for element in list1:
	if element < 5:
		list2.append(list1[element])
print(list2)
#this prints the numbers in positions 0 - 4 as a list: 1, 1, 10, 2.  
#############

list2 = []
for element in list1:
	if element < 5:
		list2.append(element)
print(list2)
#this prints the same as the first time - so (list1[element]) refers to position, (element) refers to the element.
#############

list3 = []
number = int(input("Pick a number: "))
for element in list1:
	if element < number:
		list3.append(element)
print(list3)
#prints numbers less than the number chosen