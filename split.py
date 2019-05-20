
# coding: utf-8

# In[ ]:
import os

def read_file(i,filename):
    with open(filename, 'r') as f:
        line = f.readline()
        index = 0
        while line:
            information = line.split(' ')
            identifier = information[0]
            if identifier.find('/') != -1:
                identifier = identifier.split('/')
                identifier = ' '.join(identifier)
                #print(identifier)
            #os.makedirs('new_' + str(i) +'/')
            with open('new_' + str(i) +'/' + identifier + '.txt', 'a') as f_new:
                if information[1].isdigit():
                    f_new.write(information[1] + ' ')
                    f_new.write(' '.join(information[2:]))
                    #print(information[1])
                else:
                    line = f.readline()
                    continue
            #print(identifier)
            print(index)
            index += 1
            line = f.readline()

i = 99   
while i < 109:
    os.makedirs('new_' + str(i) +'/')
    read_file(i, 'wiki-' + str(i+1) + '.txt')
    print('commit ' + 'wiki-' + str(i+1) + '.txt')
    i += 1
#read_file('wiki-001.txt')

