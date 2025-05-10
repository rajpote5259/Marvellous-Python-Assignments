def multiply(no1,no2):
    result=no1*no2
    return result

def main():
    print("Enter no1 :")
    no1 = int(input())

    print("Enter no2 :")
    no2 = int(input())

    ans = multiply(no1,no2)
    print("Ans :", ans)

if __name__=="__main__":
    main()