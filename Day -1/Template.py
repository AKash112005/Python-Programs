# Integer — whole numbers
    age = 20
    year = 2024

# Float — decimal numbers
    marks = 87.5
    cgpa = 8.3

# String — text (use quotes)
    name = "Ravi"
    college = 'IIT Coimbatore'

# Boolean — True or False only
    is_placed = False
    has_backlog = True

# Check the type of any variable
    print(type(age))      # <class 'int'>
    print(type(cgpa))     # <class 'float'>
    print(type(name))     # <class 'str'>
    print(type(is_placed)) # <class 'bool'>

# Type Casting (converting one type to another):
    pythonx = "100"        # this is a string
    y = int(x)       # now it's an integer → 100
    z = float(x)     # now it's a float → 100.0
    num = 42
    text = str(num)  # converts int to string → "42"
#Taking input from user:
    pythonname = input("Enter your name: ")
    age = int(input("Enter your age: "))   # input() always gives string, so convert!
    print("Hello", name, "you are", age, "years old")
