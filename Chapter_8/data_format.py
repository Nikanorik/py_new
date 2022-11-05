def main(data):
    list = ['january', 'february', 'march', 'april', 'may', 'june', 'juli', 'august', 'september', 'october',
            'november', 'december']
    list_new = data.split('/')
    month = list[int(list_new[1])]
    print(f'{list_new[0]} {month} {list_new[2]} years')


if __name__ == '__main__':
    main('12/08/2022')
