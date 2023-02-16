l = [["ali",10000,0],["Hamza",50,0],["John",300,0],["Patrick",5000,0],["Ayesha",4000,0],["Maham",6000,0]]

def schedule(l):
    temp = []
    for i,x in enumerate(l):
        name, value,o = x
        curr = i
        while curr>=0:
            curr-=1
            if l[curr][1]<value:
                if l[curr][2] < 2:
                    
                    l[curr],l[i] = l[i],l[curr]
                    l[curr][2]=l[curr][2] + 1
                else:
                    continue
            
    print(l)
                
        
schedule(l)