<<<<<<< HEAD
import csv

file1 = open("longlines.txt","w")

with open('quotes.csv', mode='r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    line_count=0
    longLines=0
    for row in reader:
        total = sum(len(i) for i in row)
        if total > 276:
            print(f'Line {line_count} is too long. It is {total} characters long.')
            longLines+=1
            realNumber=line_count+1
            file1.write(str(realNumber)+"\n")
            line_count+=1
        else:
            line_count+=1

print(f'Processed {line_count} lines. {longLines} lines were too long.')
   

=======
import csv

file1 = open("longlines.txt","w")

with open('quotes.csv', mode='r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    line_count=0
    longLines=0
    for row in reader:
        total = sum(len(i) for i in row)
        if total > 278:
            print(f'Line {line_count} is too long. It is {total} characters long.')
            longLines+=1
            file1.write(str(line_count)+"\n")
            line_count+=1
        else:
            line_count+=1

print(f'Processed {line_count} lines. {longLines} lines were too long.')
   

>>>>>>> 0ecbf307c247c3f0031891ba94d716ae0b2c34b7
