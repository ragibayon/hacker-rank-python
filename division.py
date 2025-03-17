def division(num1: int, num2: int, integer=True):
    if integer:
        return num1 // num2
    return num1 / num2


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(division(a, b))
    print(division(a, b, False))
