def recursive_nth_fibo(number):
    if number <= 1:
        return number
    else:
        return recursive_nth_fibo(number - 1) + recursive_nth_fibo(number - 2)


def main():
    number = input("Zadaj poradie prvku: ")
    print(recursive_nth_fibo(int(number)))


if __name__ == "__main__":
    main()
