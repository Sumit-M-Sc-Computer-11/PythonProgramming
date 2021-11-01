def main():
    batches = {"PPA":12500, "LB":11000, "Python":13000, "Angular" : 10000, "LSP":11000}
    
    print("Enter the batch name")
    name = input()
    
    print(batches.get(name,"There is no such batch"))
        
if __name__ == "__main__":
    main()
