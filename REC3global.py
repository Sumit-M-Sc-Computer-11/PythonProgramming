i=1                  #Define the variable--actuall memeory thene

def fun():
    global i       #Declare the variable
    print(i)
    i=i+1
    fun()

def main():
 fun()
  
if __name__ == "__main__":
    main()
