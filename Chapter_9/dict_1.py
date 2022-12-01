import pickle
file=open('data_es.dat','rb')
# test_averages = {'Djon':98, 'Sam':87, 'Djennefir':92, 'Tomas':74, 'Salli':89, 'Zeb':84}
print(pickle.load(file))
file.close()