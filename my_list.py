my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)

second_list = [50, 60, 70]

my_list.extend(second_list)

my_list.pop(-1)

my_list.sort()

position = my_list.index(30)
print(position)

print(my_list)