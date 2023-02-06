class HashTable:

    def __init__(self,size):
        self.size = size
        self.hashTable = [[] for _ in range(self.size)]

    def hashedKey(self,key):
        hashedKey = hash(key) % self.size
        return hashedKey

    def setValue(self,key,value):

        # jo key arahi h usko hash kro
        hashedKey = self.hashedKey(key)

        # phr hashtable mn wo index dhoondo jo key h.. wo bhi ek array hi h q k multiple keys 1 hi number p map hoskti hn
        bucket = self.hashTable[hashedKey]

        for i,record in enumerate(bucket):
            recordKey,recordValue = record
            if key==recordKey:
                #If the bucket has same key as the key to be inserted, Update the key value
                bucket[i]=(key,value)
                return
        # Otherwise append the new key-value pair to the bucket
        bucket.append((key,value))

    def getValue(self,key):
        hashedKey = self.hashedKey(key)
        bucket = self.hashTable[hashedKey]

        for idx, record in enumerate(bucket):
            recordKey, recordValue = record
            if key == recordKey:
                return recordValue
        return -1

    def deleteValue(self,key):
        hashedKey = self.hashedKey(key)

        bucket = self.hashTable[hashedKey]

        for idx,record in enumerate(bucket):
            recordKey, recordValue = record
            if key == recordKey:
                return bucket.pop(idx)
        return 'key not found'


ht = HashTable(5)

ht.setValue('one','1')
ht.setValue('two','2')
ht.setValue('three','3')
ht.setValue('four','4')
ht.setValue('five','5')
ht.setValue('six','6')
ht.setValue('seven','7')
ht.setValue('eight','8')
ht.setValue('five','10')

print(ht.hashTable)

print()
print(ht.getValue('five'))
print(ht.getValue('seven'))
print(ht.getValue('nine'))

print()
print(ht.deleteValue('nine'))
print(ht.deleteValue('three'))
print(ht.deleteValue('six'))
print(ht.hashTable)
