import csv 
import json
import os

#specifying and sorting the semester result folder:
sem_folder = r"./2021242020"
print(sem_folder)
filename = os.path.basename(sem_folder)
print(filename)
sorted_files = sorted(os.listdir(sem_folder))
print(sorted_files)

#function for reading a file:
def read_csvfile(file_name):
    data_list = []
    with open("./2021242020/"+file_name, mode='r') as file:
        csv_reader = csv.DictReader(file)
        next(csv_reader) 
        for row in csv_reader:
            data_list.append(row)
    return data_list

#calulating gpa:
def calculate_gpa(sem):
    total_credits = 0
    gpa = 0
    i = 1
    for file in os.listdir(sem_folder):
        if i == sem: 
            data_list = read_csvfile(file)
            for row in data_list:
                credits = int(row['credits'])
                grade = row['grade'].upper()

                if grade=='O':
                    gp = 10
                elif grade=='A+':
                    gp = 9
                elif grade=='A':
                    gp = 8
                elif grade=='B+':
                    gp = 7
                elif grade=='B':
                    gp = 6
                elif grade=='C':
                    gp = 5
                else:
                    gp = 0

                if grade in ['RA','SA','U']:
                    credits = 0
                total_credits = total_credits+credits
                gpa = gpa+(credits*gp)
            break

        i+=1

    total_gpa = gpa/total_credits
    return total_gpa

#calculating cgpa:
def calculate_cgpa(roll_number):
    if filename[:10]==roll_number:
        total_cgpa = 0
        total_credits = 0
        sem = 1
        for file in os.listdir(sem_folder):                
            data_list = read_csvfile(file)
            for row in data_list:
                credits = int(row['credits'])
                grade = row['grade'].upper()
                if grade == 'O':
                    gp = 10
                elif grade == 'A+':
                    gp = 9
                elif grade == 'A':
                    gp = 8
                elif grade == 'B+':
                    gp = 7
                elif grade == 'B':
                    gp = 6
                elif grade == 'C':
                    gp = 5
                else:
                    gp = 0

                if grade in ['RA', 'SA', 'U']:
                    credits = 0

                total_credits += credits
                total_cgpa += credits * gp

            sem += 1

        cgpa = total_cgpa / total_credits
        return cgpa
      
    else:
        return None


#getting user input:
roll_number = input("roll number:")
sem = int(input("enter semester:"))

sem_gpa = calculate_gpa(sem)
sem_cgpa = calculate_cgpa(roll_number)

display_data = {
    'Semester':sem,
    'GPA':sem_gpa,
    'CGPA':sem_cgpa    
}

print(json.dumps(display_data,indent=4))

