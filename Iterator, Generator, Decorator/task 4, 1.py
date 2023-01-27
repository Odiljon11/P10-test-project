def even_parametrs(func):
    def inner(*args):

        for i in args:
            if i % 2 == 0:
                return func(*args)
            else:
                return "Iltimos, faqat juft raqamlarni qo'shing!"

    return inner


@even_parametrs
def multiply(a, b):
    return a + b


a = int(input("Enter the number of a ->"))
b = int(input("Enter the number of b ->"))

print(multiply(a, b))
