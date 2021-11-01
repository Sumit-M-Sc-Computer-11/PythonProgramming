
import sys

def main():
    print("Reccursion limit is:",sys.getrecursionlimit())
    
    sys.setrecursionlimit(1500)
    print("New Reccursion limit is:",sys.getrecursionlimit())
    
  
if __name__ == "__main__":
    main()
