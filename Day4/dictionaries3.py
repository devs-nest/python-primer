my_dict = {"A": "Apple",
         "B": "Boy",
         "C": "Cat",
         "D": "Devsnest!!",
         "E": "No, not an elephant. "}

print(my_dict.items())
print("-" * 80)
my_dict_tuple = tuple(my_dict.items())
print(my_dict_tuple)

"""for t in my_dict_tuple:
    item, description = t
    print(item + " is " + description)
"""
print(dict(my_dict_tuple))