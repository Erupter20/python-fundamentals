# Create a list of items and ask the user to enter an item. Check if the item is in the list and print a message indicating whether it is found or not.

list = ['GTA V', 'Valorant', 'The Last Of Us']
#print(list)

item = input("Enter a item    :  ")
list.append(item)
print(list)

# a = ['k','l']

# a.append("as")

# print(a)

# Check if item is in the list

print('GTA V' in list)