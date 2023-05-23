#Dictoriens are unordered, changable & indexed
myDict={
    "C":"Easy",
    "C++":"Moderate",
    "Java":"Tough"
    }
print(myDict)

x=myDict["C"]
x=myDict.get("C")


print(myDict.get("C"))
myDict=["Python"]="Cool"
myDict["PHP"]="Web"
print(myDict)

#removing value
del myDict["Java"]
print(myDict)
#New value
myDict["C"]="New Value"
print(myDict.get("C"))
myDict.pop("C")
print(myDict.get("C"))
