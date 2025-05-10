def display(*a):
    print(type(a))
    print("Inside display" , a)


def main():
    display(10,20,30,40)
    display(10,20,30,40,50)
    display(10,20,30)
    display(10)
    display()

if __name__ == "__main__":
    main() 