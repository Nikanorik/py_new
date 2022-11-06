def main():
    text = input('Enter text: ')
    vowels = ['a','e','i','o','u','y']
    prep = [',','!','?','.',':',';',' ']
    count_vowels=0
    count_consonans=0
    for i in text:
        if i not in prep and i not in vowels:
            count_consonans+=1
        elif i in vowels:
            count_vowels+=1
    print(f'Amount vowels: {count_vowels} and amount consonans: {count_consonans}')



if __name__ == '__main__':
    main()