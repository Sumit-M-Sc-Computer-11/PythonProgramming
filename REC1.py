#Recursion: Calling the function from same function itself
def fun():
    i=1
    print(i)
    i=i+1
    fun():
    
     

def main():
    fun()
  
if __name__ == "__main__":
    main()