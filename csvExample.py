import csv

def readCSV():
    with open('Lecture86_Kittaphot_S.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} likes movie named {row[1]},his favourite pet is {row[2]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')

def writeCSV():
    with open('FirstWriteFile.txt', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['Zno', 'Data scientist', 'April'])
        employee_writer.writerow(['Beckies', 'Doctor', 'May'])
        employee_writer.writerow(['Pong', 'Engineer', 'December'])

writeCSV()