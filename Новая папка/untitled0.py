import csv
s=""
myData = [["first_name", "second_name"]]
print("Введите картину и год её написания, когда все данные будут введины напишите 0")
while s!="0":
    s=str(input("Введите данные "))
    if s=="0":
        break
    myData.append(s.split())
myFile = open('example2.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
print("Writing complete")
myFile.close()
with open('example2.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['first_name'], row['second_name'])