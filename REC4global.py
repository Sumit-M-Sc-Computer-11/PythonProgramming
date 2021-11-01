def Addition(data):
    sum=0
    for i in range(len(data)):sum=sum+data[i]
    return sum    
def AdditionR(data):
    sum=0
    for i in range(len(data)):sum=sum+data[i]
    AdditinR(data)

def main():
    arr=[]
    size=int(input("Enter size of array"))
    for i in range(size):arr.append(int(input())
    
        print("Data is:",arr)
    
        print ("Addition is:"Addition(arr))
    
        print (addition of Recursive fun is " AdditionR(data))
    
if __name__ == "__main__":
    main()
