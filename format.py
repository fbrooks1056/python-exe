import csv

user_file = open ('test.csv')
readerOrg = (user_file)

dump_file = open('dump.txt', 'w')

for row in readerOrg:
    print '"%s",  \n'  %  (row)
    dump_file.write('"%s",\n' % (row))
