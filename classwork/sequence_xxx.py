def circle_area(rad,pi = 3.14):
    ans = rad * rad * pi
    return ans
    
def main():
    print("Enter radius of circle ")
    r = float(input())
    ans = circle_area(r,7.14)
    print("Area of circle ", ans)

if __name__ == "__main__":
    main()