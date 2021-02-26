my_dict = {"A": "Apple",
         "B": "Boy",
         "E": "No, not an elephant.",
         "C": "Cat",
         "D": "Devsnest!!"}


# my_dict["F"] = "Fox"
# my_dict["C"] = "Cow"
# print(my_dict)
# del my_dict["C"]
# my_dict.clear()
# print(my_dict)
# print(my_dict["G"])
# print(my_dict.get("G"))
# print(my_dict)


while True:
    dict_key = input("Please enter something: ")
    if dict_key == "quit":
        break
    description = my_dict.get(dict_key, f"we don't have a {dict_key}")
    print(description)

