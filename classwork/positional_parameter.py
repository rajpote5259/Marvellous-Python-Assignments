def calculatepercentage(total,obtained):
    ans = (obtained / total)* 100
    return ans

def main():
    print("Enter Marks_1")
    no1 = int(input())

    print("Enter Marks_2")
    no2 = int(input())
    Total_Percentage = calculatepercentage(no1,no2) #positional_parameter
    print("Total Percentage are ", Total_Percentage)

if __name__ == "__main__":
    main()
