def help(no):
    print("inside help")
    no = no + 1
    return no

value = 10
i = help(value)
print("i contains",i)