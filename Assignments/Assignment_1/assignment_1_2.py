def ChkNum(num):
    if num % 2 == 0 : 
        print("Even Number")
    else: 
        print("Odd number")    

def main():
    print("Enter Number")
    num = int(input())
    ChkNum(num)

if __name__ == "__main__":
    main()