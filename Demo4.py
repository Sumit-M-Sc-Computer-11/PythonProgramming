def main():
    name = input("Enter the file name that you want to create")
    
    fobj = open(name,"r")   # create new file
    size = int(input("Enter number of characters to read"))
    
    print("Data from file is ")
    print(fobj.read(size))
    
if __name__ == "__main__":
    main()
