def get_key(value_to_find):
    listofkeys = []
    listofitems = my_dict.items()
    for item in listofitems:
        if item[1] == value_to_find:
            listofkeys.append(item[0])
    return listofkeys


n = int(input("Enter number of keys in dictionary"))
my_dict = {}
for i in range(n):
    keys = input("Enter a country")
    values = input("Enter a continent")
    my_dict[keys] = values
outputlist = get_key(input("Enter a continent which will get the countries of it"))
print(outputlist)