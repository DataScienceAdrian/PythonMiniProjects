# Zad 1
import random

random_integers = random.sample(range(100, 200), 50)
# print(max(random_integers))
# print(min(random_integers))
#
# # Last element of the list
# print(random_integers[-1])
# print(len(random_integers))

# Zad 2
a = [1, 1, 3, 1, 2, 1, 7, 2, 8]

count_ones = a.count(1)
# print(count_ones)

# Zad 3
a = [1, 2, 3, 4, 5, 7, 7]

# for number in a:
# print(a.index(number))

# Zad 4

numbers = random.sample(range(0, 100), 50)

squared_numbers = []
for n in numbers:
    n = n ** 2
    squared_numbers.append(n)
    #print(squared_numbers)

# Zad 5

cities_list = ['Warsaw', 'Chi', 'New York', 'London', 'Paris', 'Rome', 'Moscow', 'Prague', 'Helsinkisssssss', 'Sofia']

for item in cities_list:
    if len(item) >= 3 and len(item) < 7:
        print(item)

cities_list.sort()
print(cities_list)

cities_list.sort(key=len)
print(cities_list)

cities_list.sort(key=len, reverse=True)
print(cities_list)

upper_list = []

for item in cities_list:
    upper_list.append(item.upper())

print(upper_list)

print(max(cities_list))

print(min(cities_list))


# Zad 6
tuples_list = [(4, 5), (6, 1), (4, 5), (6, 1)]

unique_tuples = []

for tuple in tuples_list:
    if tuple not in unique_tuples:
        unique_tuples.append(tuple)
        print(unique_tuples)


# Zad 7

a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

my_dict = {}

for item in a:
    my_dict[item] = a.count(item)

print(my_dict)