def main():
    text = input('Enter text: ')
    text_new = text.split()
    list_new=[]
    for i in text_new:
        text_custom = i[1:]+i[0].lower()+'ki'
        list_new.append(text_custom)
    new_words = ' '.join(list_new)
    print(new_words)
if __name__ == '__main__':
    main()