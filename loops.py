def print_squared_int_loop(num: int):
    if not (1 <= num <= 20):
        return
    for i in range(num):
        print(i * i)


if __name__ == "__main__":
    n = int(input())
    print_squared_int_loop(n)
