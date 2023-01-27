def add(a, b):
    def inner_add():
        return (a + b) * 2

    return inner_add


a = int(input("Enter the number of a ->"))
b = int(input("Enter the number of b ->"))

print(add(a, b))
