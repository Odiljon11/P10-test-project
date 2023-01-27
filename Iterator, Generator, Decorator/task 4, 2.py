def even_parametrs(func):
    def inner(*args):

        for i in args:
            if i % 2 == 0:
                return func(*args)
            else:
                return "Iltimos, faqat juft raqamlarni qo'shing!"

    return inner


@even_parametrs
def multiply(a, b, c, d):
    return a * b * c * d


a = int(input("Enter the number of a ->"))
b = int(input("Enter the number of b ->"))
c = int(input("Enter the number of c ->"))
d = int(input("Enter the number of d ->"))

print(multiply(a, b, c, d))
