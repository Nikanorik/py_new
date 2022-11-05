def main():
    number = input('Enter list number: ')
    summer = 0
    for i in number:
        i = int(i)
        summer += i
    print(summer)
    return (summer)


if __name__ == '__main__':
    main()
