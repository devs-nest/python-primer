my_dict = {"A": "Apple",
         "C": "Cat",
          "D": "Devsnest!!",
         "B": "Boy",
         "E": "No, not an elephant. "}

print(my_dict)


ordered_keys = list(my_dict.keys())
ordered_keys.sort()

for k in ordered_keys:
    print(k + " - " + my_dict[k])



for k in my_dict:
   print(k  + " - " + my_dict[k])

for val in my_dict.values():
    print(val)

