def add(num1: int, num2: int):
    return num1 + num2


def subtract(num1: int, num2: int):
    return num1 - num2


def multiply(num1: int, num2: int):
    return num1 * num2


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(add(a, b))
    print(subtract(a, b))
    print(multiply(a, b))
