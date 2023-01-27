def add(a, b):
    def addd():
        return (a + b) * 2

    return addd


a = int(input("Enter the number of a ->"))
b = int(input("Enter the number of b ->"))

print(add(a, b))
