def ChkNum(num):
    if num < 0 : 
        print("Negative Number")
    elif num > 0: 
        print("Positive number")
    else:
        print("Zero")        

def main():
    print("Enter Number")
    num = int(input())
    ChkNum(num)

if __name__ == "__main__":
    main()