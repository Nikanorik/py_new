dict = {'Kat':'1','Gerda':'3','Slom':'2'}
for ket,value in dict.items():
    print(ket,value)
dict['_Deda']='2'
print(dict)
del dict['Gerda']
print(dict)
print(len(dict))