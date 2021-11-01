class Arithematic:                      # class definition aahe
    value=111                       #class variable
    
    def __init__(self,i,j):             #Class Constructor
        print("Inside Constructor")
        self.no1=i                      #no1 charecteristic///Class instance variable
        self.no2=j                      #no2 charecteristic aahe//Instance variable
        
    def Add(self):                      #instance method
        return self.no1+self.no2
        
    def Sub(self):                        #instance method
        return self.no1-self.no2
        
def main():
    print("class value is:",Arithematic.value)
    obj1=Arithematic(21,11)          #Arithematic(obj) --> __init__(obj)//__init__(obj1,21,11)
    obj2=Arithematic(101,51)            # __init__(obj1,101,51)
        
        
    ret=obj1.Add()              #ret=Add(obj1)
    print("Addition is",ret)    
    ret=obj1.Sub()               #ret=Sub(obj1)
    print("Subtraction is",ret)
    
    
    ret=obj2.Add()                   #ret=Sub(obj2)
    print("Addition is",ret)
    ret=obj2.Sub()                   #ret=Sub(obj2)
    print("Subtraction is",ret)
    
if __name__== "__main__":
    main() 