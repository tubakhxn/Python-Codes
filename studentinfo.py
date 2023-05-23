import csv
def write_into_csv(info_list):
    with open('student_ino.csv', 'a', newline='')as csv_file:
        writer=csv.writer(csv_file)

if __name__== '__main__':
     condition= True

while(condition):
     student_info= input("Enter the information of the student(name, contact, email_Id):")
     print("Entered information" + student_info)

#slpiting the info
student_info_list.split('')
print("Ented information is: \nName: {}, \n Conatch_number: {}, \n email ID: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
choice_check=input("Is the netered informantion correct?(yes/no):")
if choice_check=="yes":
        write_into_csv(student_info_list)
           
condition_check=input("Enter yes/no if you want to enter the information of the other student as well:")
if condition_check=="yes":
             condition= True
             student_num= student_num + 1
elif condition_check=="no":
             condition=False
elif  choice_check == "no":
    print("\nPlease re-enter the values")
