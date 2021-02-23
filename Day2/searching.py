shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] != item_to_find:
        continue
    print("I am at line 9")
    if shopping_list[index] == item_to_find:
        found_at = index
        break

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))
