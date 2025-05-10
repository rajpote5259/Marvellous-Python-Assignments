def ChkNum(num):
    if num % 5 == 0 : 
        print("True")
    else:
        print("False")
       
def main():
    print("Enter Number")
    num = int(input())
    ChkNum(num)

if __name__ == "__main__":
    main()