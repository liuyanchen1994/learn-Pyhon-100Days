import sys


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    list1 = [1, 2, 3, 4, 5]
    print(list1)
    list2 = ['hello'] * 5
    print(list2)
    print(len(list1))
    print(list1[-1])
    print(list1[-2])
    list1.append(20)
    print(list1)
    list1.insert(1, 300)
    print(list1)
    list1.remove(5)
    print(list1)
    del list2[1]
    print(list2)
    f = [x for x in range(1, 10)]
    print(f)
    f = [x ** 2 for x in range(1, 1000)]
    print(f)
    print(sys.getsizeof(f))
    for val in f:
        print(val)
    for val in fib(20):
        print(val, end=' ')


if __name__ == "__main__":
    main()
