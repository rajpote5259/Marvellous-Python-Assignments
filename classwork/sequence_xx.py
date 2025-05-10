pi = 3.14

def circle_area(rad):
    ans = rad * rad * pi
    return ans
    
def main():
    print("Enter radius of circle ")
    r = float(input())
    ans = circle_area(rad = r)
    print("Area of circle ", ans)

if __name__ == "__main__":
    main()