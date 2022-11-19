import random


def main():
    vocabulary = {'step by step': 'шаг за шагом', 'arrive': 'прибывать', 'join': 'присоединиться', 'soon': 'ближайший',
                  'the entrance exams': 'вступительные экзамены', 'take driving lessons': 'брать уроки вождения',
                  'advice': 'совет', 'be on time': 'будь вовремя', 'simple': 'простое', 'compaund': 'составное',
                  'carry': 'нести', 'still': 'все еще', 'lie': 'лежать', 'break': 'перерыв', 'tidy up': 'прибраться',
                  'A yong man is standing at the window': 'молодой мужчина стоит у окна', 'paint': 'красить',
                  'neighbors': 'соседи', 'sink': 'раковина', 'where am I': 'где я?',
                  'is he from USA': 'Он из Америки?', 'how old are you': 'сколько тебе лет?', 'ceiling': 'потолок',
                  'next time': 'следующий раз', 'take an english exam': ' сдавать английский экзамен',
                  'do makeovers': 'делать ремонт', 'feed the cat': 'кормить кота',
                  'enter the university': 'поступать в университет', 'stay at home': 'оставаться дома',
                  'how will you get visa': 'как ты будешь получать визу?',
                  'take english classes': 'брать уроки английского языка', 'tell the truth': 'говорить правду',
                  'invite': 'пригласить', 'organize a party': 'устраивать вечеринку',
                  'repair the computer': 'чинить компьютер', 'solve the problem': 'решить проблему',
                  'take an exam': 'сдавать экзамен', 'truth': 'правда', 'the day after tomorrow': 'послезавтра',
                  'how many classes will you have tomorrow': 'как много уроков ты имеешь завтра?',
                  'i study well at school': 'я учусь хорошо в школе', 'let is talk': 'позволь нам поговорить',
                  'make a present': 'делать подарки', 'be married': 'быть замужем',
                  'groccery store': 'продуктовый магазин', 'give present': 'дарить подарки',
                  'brush teeth': 'чистить зубы', 'take a shower': 'принимать душ', 'film videos': 'делать видео',
                  'run in the forest': 'бегать в лесу', 'why are you at home': 'почему ты дома?', 'dirty': 'грязный',
                  'single': 'одинокий', 'where are you from': 'откуда ты?', 'there': 'там', 'i am out': 'я на руже',
                  'much love': 'много любви', 'much joi': 'много радости', 'much tolerance': 'много терпения',
                  'much jealosy': 'много ревности', 'much passion': 'много страсти', 'much knowledge': 'много знаний',
                  'living': 'живущие', 'are there': 'есть ли', 'pets': 'домашние питомцы',
                  'wild animal': 'дикое животное', 'speak the language': 'говорить на языке',
                  'smoke cigarettes': 'курить сигареты', 'how many friends do you have': 'сколько друзей ты имеешь?',
                  'how much work do you have': 'сколько работы ты имеешь?',
                  'how much coffee do you drink': 'сколько кофе ты пьешь?', 'candies': 'конфеты', 'candy': 'конфета',
                  'siblings': 'братья и сестры',
                  'how much light is there in the room': 'сколько света в этой комнате?', 'garage': 'гараж',
                  'i read much': 'я много читаю', 'i travel much': 'я много путешествую',
                  'little': ' мало(неисчисляемое)', 'few': 'мало(исчисляемое)', 'a little': 'несколье(неисчисляемое)',
                  'a few': 'мало(исчисляемое)', 'he gives us many apples': 'он дает нам много яблок',
                  'spend time': 'проводить время', 'i have no time': 'у меня нет времени', 'exercise book': 'тетрадь',
                  'chalk': 'мел', 'snow': 'снег', 'article': 'статья', 'soup': 'мыло', 'grass': 'трава',
                  'palace': ' дворец', 'the first': 'первый', 'the second': 'второй', 'the third': 'третий',
                  'the fourth': 'четвертый', 'wash the dishes': 'мыть посуду', 'paint the house': 'красить дом',
                  'meet friends': 'встречаться с друзьями', 'monument': 'памятник', 'church': 'церковь',
                  'turn left': 'повернуть на лево', 'turn right': 'повернуть на право', 'go straight on': 'идти прямо',
                  'must': 'должен', 'opposite': 'напротив', 'next to': 'рядом', 'pharmacy': 'аптека',
                  'behind': 'позади', 'a garage': 'гараж', 'between': 'между', 'in front of': 'перед',
                  'a lawn': 'газон', 'bench': 'скамейка', 'a parking lot': 'парковка', 'on the left': 'слева',
                  'on the right': 'справа', 'newsagent': 'киоск с газетами', 'greengrocer': 'овощной магазин',
                  'chemist': 'парфюмерия', 'celebrate': 'праздновать', 'call your parents': 'звонить твоим родителям',
                  'wait for a course': 'ждать курса', 'make mistakes': 'делать ошибки', 'wash the floor': 'мыть пол',
                  'upload': 'загружать', 'take part in these copmetitions': 'принимать участие в этих соревнованиях',
                  'wear': 'носить', 'get on board': 'садиться на самолет', 'tell lies': 'лгать',
                  'not funny anecdots': 'несмешные анекдоты', 'everywhere': 'везде', 'recognize': 'узнавать',
                  'hear': 'слушать', 'smell': 'пахнуть', 'i am out now': 'я не дома сейчас', 'handbag': 'ручная кладь',
                  'luggage': 'багаж', 'difficult': 'сложно', 'noisily': 'шумно', 'forget about it': 'забудь об этом',
                  'doorway': 'дверной проем', 'sea': 'море', 'tape recording': 'магнитофонная запись',
                  'rather': 'скорее', 'prepare': 'подготовить', 'as a rule': 'как правило', 'keep': 'хранить',
                  'argue': 'спорить', 'worry': 'волноваться', 'ruth': 'жалость',
                  'do not disturb him': 'не мешайте ему', 'gone with the wind': 'унесенные ветром',
                  'hurry up': 'торопиться', 'busy': 'занятый',
                  'there is a black car in front of my house': ' перед моим домом черная машина', 'may': 'можно',
                  'should': 'следует', 'happen': 'случаться', 'it can be truth': 'это может быть правдой',
                  'i can washh the dishes': 'я могу помыть посуду', 'i can happen today': 'это может случиться завтра',
                  'be late': 'быть опаздавшим', 'drive and mend a car': 'водить и чинить машину',
                  'ride a motorbike': 'ездить на мотоцикле', 'change the appearance': 'сменить внешнешность',
                  'fly a plane': 'летать на самолете', 'take a pictures': 'делать фотографии',
                  'speak some foreign languages': 'говорить на нескольких иностранных языках',
                  'ski': 'кататься на лыжах', 'climb mountains': 'взбираться по горам',
                  'play an instrument': 'играть на музыкальном инструменте', 'take a risk': 'рисковать',
                  'it means': 'это значет', 'however': 'однако', 'do not worry': 'не беспокойся',
                  'exciting': 'захватывающая', 'afraid': 'боюсь', 'how about': 'что насчет', 'be busy': 'быть занятым',
                  'either': 'так же', 'move house': ' переезжать', 'quarter': 'четверть',
                  'the day before yesterday': 'позавчера', 'three days ago': '3 дня назад', 'a year ago': 'год назад',
                  'be born': ' быть рожденным', 'last time': 'последний раз', 'i was out':'быть на улице' }
    flag = True
    check_plus = 0
    check_minus = 0
    while flag:
        i = random.randint(0, len(vocabulary) - 1)
        answ_one = list(vocabulary)[i]
        print(vocabulary[answ_one])
        answer = input('Enter answer: ')

        if answer == answ_one:
            print('It is right!!!')
            check_plus += 1
            new_answer = input('Will you next?(y/n): ')
            if new_answer != 'y':
                flag = False
        else:
            check_minus -= 1
            print('Wrong!!!')
            print(f'Right answer: {answ_one}')
            new_answer = input('Will you next?(y/n): ')
            if new_answer != 'y':
                flag = False

    print(f'Thank you!!! Plus: {check_plus}, Minus: {check_minus}')


if __name__ == '__main__':
    main()
