omlette = {'eggs': 3, 'tomato': 1, 'onion': 1, 'spices': ['salt', 'black '
                                                                  'pepper',
                                                          'red chilli']}
keys = omlette.keys()
values = omlette.values()

print(keys)
print(values)
print("-" * 40)
# view objects are dynamic and reflect dict changes
del omlette['eggs']
print(keys)  # No eggs anymore!

print(values)  # No eggs value (3) anymore!











# The Python 2 equivalent uses dishes.viewkeys() and dishes.viewvalues()