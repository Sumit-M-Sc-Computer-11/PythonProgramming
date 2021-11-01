#Recursion: Calling the function from same function itself

def DisplayIF(no1):
   for i in range(no): #iteration using for loop
       print("Hello")
       
 def DisplayIW(no):
    while no!=0: #iteration using while loop
       print("Hello")      
       no=no-1
       

def DisplayR(no):
    if no!=0:
        no=no-1
        print("Hello")
        DisplayR(no)    #Recursive call    

def main():
   print("Enter the number of iterations")
   value=int(input())
    
    print("calling itterative function with for loop")    
    DisplayIF(value)
    
     print("calling itterative function with While loop ")    
    DisplayIW(value)
    
     print("calling itterative function")    
    DisplayR(value)
    
if __name__ == "__main__":
    main()
