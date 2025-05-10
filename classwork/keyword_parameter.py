def calculatepercentage(total,obtained):
    ans = (obtained / total)* 100
    return ans

def main():
    print("Enter obtained marks:")
    no1 = int(input())

    print("Enter total marks:")
    no2 = int(input())
    Total_Percentage = calculatepercentage(total=no2,obtained=no1) #keyword_parameter
    print("Total Percentage are ", Total_Percentage)

if __name__ == "__main__":
    main()
