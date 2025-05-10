pi = 3.14

def circle_area(r):
    ans = r * r * pi
    return ans
    
def main():
    print("Enter radius of circle ")
    r = float(input())
    ans = circle_area(r)
    print("Area of circle ", ans)

if __name__ == "__main__":
    main()