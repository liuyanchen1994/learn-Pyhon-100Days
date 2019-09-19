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


if __name__ == "__main__":
    main()
