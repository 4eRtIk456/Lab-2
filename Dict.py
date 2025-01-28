thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# Using the dict() method to make a dictionary:
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

"""
Access Items
"""

# Get the value of the "model" key:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

# Get the value of the "model" key:
x = thisdict.get("model")

# Get a list of the keys:
x = thisdict.keys()

# Get a list of the values:
x = thisdict.values()

# Get a list of the key:value pairs
x = thisdict.items()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

"""
Change Items
"""

# Change the "year" to 2018:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

thisdict.update({"year": 2020})

"""
Add Items
"""

thisdict["color"] = "red"
print(thisdict)

thisdict.update({"color": "red"})

"""
Remove Items
"""
thisdict.pop("model")
print(thisdict)

# The popitem() method removes the last inserted item:
thisdict.popitem()
print(thisdict)

del thisdict["model"]
print(thisdict)

thisdict.clear()
print(thisdict)
