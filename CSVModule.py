import csv

with open('C:\\Users\\GHarsh\\Desktop\\def.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    print(csv_reader)  # <_csv.reader object at 0x00000251A9D529E8>
    with open('new.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file)
        for line in csv_reader:
            csv_writer.writerow(line)
    # next(csv_reader)
    # for line in csv_reader:
    #     print(line[1])

######## DictReader ############
# with DictReader, if name is header of csv, then it will return ('name', 'John') for all the entries
with open('new.csv') as f:
    csv_reader1 = csv.DictReader(f)

    for line in f:
        print(line)
