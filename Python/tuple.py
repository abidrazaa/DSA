listOfTuples = [('candy','30',100), ('apple','10',50), ('baby','20',10)]


def sortTupleByParticularIndex(l):

    # dont need to store in any variable
    l.sort(key=lambda s:s[2])

    # need to store in a variable
    l = sorted(l, key = lambda s:s[2])

    print("sorted ==>",l)


sortTupleByParticularIndex(listOfTuples)