def calculatepercentage(obtained = 400, total = 500):
    ans = (obtained / total)* 100
    return ans

def main():
#    print("Enter obtained marks:")
#    no1 = int(input())

#    print("Enter total marks:")
#    no2 = int(input())


    Total_Percentage = calculatepercentage(350,450)
    print("Total Percentage are ", Total_Percentage)
    
    Total_Percentage = calculatepercentage(350)
    print("Total Percentage are ", Total_Percentage)

    Total_Percentage = calculatepercentage()
    print("Total Percentage are ", Total_Percentage)

if __name__ == "__main__":
    main()
