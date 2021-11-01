class Arithematic:                      # class definition aahe
    value=111                       #class variable
    
    def __init__(self,i,j):             #Class Constructor
        print("Inside Constructor")
        self.no1=30                      #no1 charecteristic///Class instance variable
        self.no2=40                      #no2 charecteristic aahe//Instance variable
        
    def Add(self):                      #instance method
        return self.no1+self.no2
        
    def Sub(self):                        #instance method
        return self.no1-self.no2
        
def main():
    print("class value is:",Arithematic.value)
    obj1=Arithematic(21,11)          #Arithematic(obj) --> __init__(obj)//__init__(obj1,21,11)
    obj2=Arithematic(101,51)            # __init__(obj2,101,51)
        
        
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
    
    
    
    
    
    
    ----------------------
    
    class Numbers:
        def __int__(self,no=10):
        self(size)=0
        
    
    def Summation(self):
     sum=0
     for i in range(self.size):
      sum =sum +selfarr[i];
      
      return sum
      
      
      for i range(self.size):
        if(self.arr[i]%2)==0
          print(selfarr[i]
          
        
      def EvenDisplay(self):
         print("Enter number of elements")
         value=int(input())
         "
      def PrefectDisplay(self):
      Sum=0
       for i in range(self.size):
         for jin range(1,int(self.arr[i]/2)+1):
            if(slef.arr[i]%j)==0:
              sum=sum+jin
              
         if sum ==self.arr[i]:
                print(self.arr[i])
            sum=0    
            
         def PrimeDisplay(self):
            Flag=False
            for i in range(self.size):
               for j in range(2,int(self.arr[i]/2)+1):
                    if(self.arr[i]%j)==0:
                      Flag=True 
                      break
                   if Flag==False:
                       print(self.arr[i])
                   Flag=False                        
               
       
      def main():
      print("Enter the numbers")
      value=int(input())
      
   
      obj1=Numbers(value)
      obj1.Accept()
      obj1.Display()
      ret=obj1.Summation()
      print("Summation of all elements:",ret)
      obj1.evenDisplay()
      print("Pefect numbers are")
      obj1.PefectDisplay()
      obj1.PefectDisplay()
      print(
      del obj1
      
 if __name__="__main__":
            main()
            
            