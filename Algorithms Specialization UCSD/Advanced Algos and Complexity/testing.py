import os

code_file = './airline_crews.py'
for i in range(1,32):
    scmd = '(python3 {} < ./tests/{:02}) > ./ans/{}'.format(code_file,i,i)
    os.system(scmd)

    path = './ans/{}'.format(i)
    ans = open(path, 'r').readline()[:-1]
    cpath = './tests/{:02}.a'.format(i)
    cans = open(cpath, 'r').readline()[:-1]
    print(cans == ans)


