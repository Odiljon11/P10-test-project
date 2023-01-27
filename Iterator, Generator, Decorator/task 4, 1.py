def only_even_parameters(func):
    def inner(*args):

        for i in args:
            if i % 2 == 0:
                return func(*args)
            else:
                return "Iltimos, faqat juft raqamlarni qo'shing!"

    return inner


@only_even_parameters
def multiply(a, b):
    return a + b


a = int(input("Enter the number of a ->"))
b = int(input("Enter the number of b ->"))

print(multiply(a, b))
