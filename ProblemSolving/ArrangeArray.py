
arr = [1,4,-4,2,-9,2,-1,-12,4]


# O(n)
def arrangeNegativeValuesInTheLast(arr):
    for i in range(len(arr)):
        if arr[i]>0:
            curr = i
            prev = i
            flag=True
            while prev-1>=0 and flag:
                prev-=1
                if arr[prev]<0:
                    arr[prev],arr[curr] = arr[curr],arr[prev]
                    curr-=1

                else:
                    flag=False
    print(arr)

arrangeNegativeValuesInTheLast(arr)