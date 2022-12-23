def domain_name(url):
    print(url)
    if '//www' in url:
        return (url.split('.'))[1]
    elif '//' in url:
        one = url.split('//')
        two = one[1].split('.')
        return two[0]
    elif 'www.' in url:
        return (url.split('.'))[1]
    elif '.' in url:
        return (url.split('.'))[0]


domain_name("www.xakep.ru")





