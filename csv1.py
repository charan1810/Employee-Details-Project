import csv
import os
if not os.path.exists("employee detail.csv"):
    with open ("employee detail.csv",'w') as f1:
        '''Taking employee data employee number, name, contact,dept., salary, address'''
        '''Header details of table i.e., header'''
        header = ["Employee Number", "Employee Name", "Employee Contact",
                  "Employee Department", "Employee Salary", "Employee Address"]
        filewrite = csv.writer(f1)
        filewrite.writerow(header)
while(True):
    try:
        print("Enter employee number:")
        n=int(input())
        print("Enter employee name: ")
        s=input()
        print("Enter employee contact(Ph.No/G-mail): ")
        c=input()
        print("Employee Department:")
        d=input()
        print("Employee Salary(in terms of k): ")
        sal=int(input())
        print("Employee address:")
        ad=input()
        '''Creating a table of employee details of employee number,
         name, contact,dept., salary, address'''
        record,records=[],[]
        record.extend([n,s,c,d,sal,ad])
        records.append(record)
        with open("employee detail.csv", 'a', newline='') as f1:
            filewrite = csv.writer(f1)
            filewrite.writerow(record)
        print("="*50)
        print("If you want to continue press y/n :")
        des=input()
        if des=='n':
            break
    except FileNotFoundError:
        print("File doesnt exist")
    except ValueError:
        print("Enter only numbers not number with 'k' ")
    except:
        print("OOoops!, Something went wrong")

