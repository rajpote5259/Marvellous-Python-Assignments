def calculatepercentage(obtained, total = 100):
    ans = (obtained / total)* 100
    return ans

def main():
    print("Enter obtained marks:")
    no1 = int(input())

    print("Enter total marks:")
    no2 = int(input())

    Total_Percentage = calculatepercentage(total = no2,obtained = no1)
    Total_Percentage_2 = calculatepercentage(obtained = no1)
    print("Total Percentage are ", Total_Percentage)
    print("Total Percentage are ", Total_Percentage_2)

if __name__ == "__main__":
    main()


 