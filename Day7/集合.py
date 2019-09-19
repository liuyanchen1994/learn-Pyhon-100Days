def main():
    set1 = {1, 2, 3}
    set2 = {1, 2, 3, 4, 5, 6, 7}
    print(set1 & set2)  # 交集
    print(set1 | set2)  # 并集
    print(set1 - set2)
    print(set1 ^ set2)  # 差集
    print(set1 <= set2)


if __name__ == "__main__":
    main()
