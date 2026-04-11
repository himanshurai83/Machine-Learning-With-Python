# thisDict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964,
#     "brand": "Toyota"
# }

# print(thisDict["brand"])
# thisDict["brand"] = "Ford"
# print(thisDict["brand"])
# print(len(thisDict))


thisDict = {
    "brand": "Ford",
    "electric": False,
    "colors": ["red", "white", "blue"]
}

# print(thisDict["colors"][2])
# print(type(thisDict))


# Dict constructor

# myDict = dict(name="Himanshu", age=20, college="Galgotias")
# print(myDict)


# get() Get any particular value.

# print(thisDict.get("colors"))

# key() Get only all the key inside the dictionary.
# print(thisDict.keys())
# thisDict["speed"] = "100km/h"  # adding another key-value that not exists..
# print(thisDict.keys())
# print(thisDict)

# value() Get only all the values inside the dictionary.
# print(thisDict.values())

# items() Get all the values and key inside the dictionary.
# print(thisDict.items())

# update() Update the key value.
thisDict['year'] = 2023
thisDict['sellYear'] = 2025
print(thisDict)

# thisDict.update({'year': 2020})
# print(thisDict)

# pop() Delete item to a specific key.
# print(thisDict.keys())
# key = input("Enter any key: ")
# if key in thisDict:
#     thisDict.pop(key)
#     print(thisDict)
# else:
#     print("Key does not exits!")

# popitem() Delete last inserted element..
# print(thisDict)
# thisDict.popitem()
# print(thisDict)
# thisDict.popitem()
# print(thisDict)

# del delete element according to key.
# del thisDict['electric']
# print(thisDict)
# del thisDict
# print(thisDict)

# clear() Empty dictionary.
# thisDict.clear()
# print(thisDict)
