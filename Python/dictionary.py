
instructors = {
    "Maths" : "Sir Farhan",
    "English" : "Sir Jaffer",
    "Chemistry" : "Sir Ahad",
    "Physics" : "Sir Taqi Mehdi",
    "Urdu" : "Sir Shah"
}


def iteratingDictionary(dict):
    for key,value in dict.items():
        print(key,":",value)
    
    for key in dict.keys():
        print(key)

    for value in dict.values():
        print(value)


def swapDictionaryKeyValues(dict):
    swappedDictionary = {}

    for key,value in dict.items():
        swappedDictionary[value] = key

    print('Swapped Dictionary ==>',swappedDictionary)



def CRUD(dict):
    # DELETE from a dictionary
    dict.pop("Maths")
    # Another way to delete
    del dict["Urdu"]

    # ADD key value pair (can also be used to update value of a key)
    dict["Maths"] = "Sir Abid"

    # UPDATE value of a key
    dict.update({"Physics":"Sir Hammad"})

    print(dict)


iteratingDictionary(instructors)
swapDictionaryKeyValues(instructors)
CRUD(instructors)








marksOfStudents = {
    "Abid" : 50,
    "Shah" : 90,
    "Raza" : 88,
    "Mesum" : 76,
    "Naqvi" : 45,
    "Unknown" : 33
}

def sortDictionaryByValues(dictionary):

    # sorted return an array. "dict" as the prefix is helping to retain answer in dictionary format
    # otherwise if we remove dict from start, we will get sorted array of tuples where tuple represents key values
    sortedDict = dict(sorted(dictionary.items(), key=lambda s:s[1]))

    print("sortedDict==>",sortedDict)

sortDictionaryByValues(marksOfStudents)