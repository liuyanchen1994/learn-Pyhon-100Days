def main():
    t = (1, 'hello world', False)
    for i in t:
        print(i)
    # t[0] = 2 元组的数据是不能修改的
    print(t[0])

    list1 = list(t)
    list1[0] = 2
    print(list1)
    t2 = tuple(list1)
    print(t2)


if __name__ == "__main__":
    main()
