myDict = {
    "rabish": "a coder",
    "rab" : "a setter of cnc hobbing",
    "new Dict": {"ravi" : "rabish your are not born to do small things "}
    }
# print(myDict)
# print(myDict["new Dict"]["ravi"])
print(myDict.keys())
print(myDict.values())
print(myDict.items())#this returns the keys and values of the content
updatedict = {
    "rahul" : "friend"
}
myDict.update(updatedict)# update the dictionary
print(myDict)
# the difference between .get and []syntax in a dictory.
print(myDict.get("rabish2"))
print(myDict["rabish2"])
