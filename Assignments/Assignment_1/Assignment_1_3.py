def add(num1,num2):
    ans = num1 + num2
    print("Addition is : ",ans)   

def main():
    print("Enter First Number")
    num1 = int(input())
    print("Enter Second Number")
    num2 = int(input())
    add(num1,num2)

if __name__ == "__main__":
    main()