students = []

def load_student():
    
    student_key_search = {}

    try:

        with open("SMS.txt","r") as file:
            
            for student in file:
                
                if student == "\n":
                    
                    stud = student_key_search

                    stud_copy = stud.copy()

                    students.append(stud_copy)

                    student_key_search.clear()
                    
                    
                else:
                    
                    student_li = student.strip().split(":")  # Here Strip Removes The \n & Also Space
                    
                    key = student_li[0] 
                    
                    value = student_li[1]
                    
                    student_key_search[key] = value

    except:
        
        print("Add Student First")

        return

    print(students)

load_student()

def main_menu():

    print("===========================")

    print("STUDENT MANAGEMENT SYSTEM")

    print("===========================")

    print()

    print("1. Add Student")

    print("2. View Student")

    print("3. Search Student")

    print("4. Update Student")

    print("5. Delete Student")

    print("6. Exit")

    print("7. Delete All Students")

    print()

def add_student():

    students_key = {}

    with open("SMS.txt","a") as file:

        try:
            
            student_id = int(input("Enter Student ID : "))

        except ValueError:

            print("Enter Number's Only")

            return
        
        for student in students:

            if int(student["id"]) == student_id:

                print("Create a New ID Already Exist")

                return

        students_key["id"] = student_id

        student_name = input("Enter Student Name : ")

        students_key["Name"]=student_name

        try:
            
            student_roll = int(input("Enter Student Roll Number : "))

        except ValueError:

            print("Enter Number's Only")

            return

        students_key["Roll No"] = student_roll

        student_depart = input("Enter Student Department : ")

        students_key["Department"] = student_depart

        student_year = input("Enter Student Year : ")

        students_key["Year"]= student_year

        try:
            
            student_marks = int(input("Enter Student Mark : "))

            if student_marks < 0 or student_marks > 100:

                print("Invalid Mark. Enter Correct Mark.")

                return
        
        except ValueError:

            print("Enter Number's only")

            return

        students_key["Mark"] = student_marks

        students.append(students_key)

        print(students_key)

        print(students)

        for key,value in students_key.items():

            if type(value) == int:

                value = str(value)
            
            file.writelines(key +":" + value + "\n")
            
        file.write("\n")

def view_student():

    try:

        with open("SMS.txt","r") as file:

            read_data = file.read()

            print(read_data)

    except FileNotFoundError:

        print("Add Student First then View Student.")

        return

def search_student():

    try:

        enter_id = int(input("Enter Student Id To Find Student : "))

    except ValueError:

        print("Enter Numbers Only")

        return

    for student in students:

        ID_Stud = student["id"]
            
        if int(ID_Stud) == enter_id:

            print(student)

            break

    else:

        print("Student ID not Found Enter Correct Student ID.")

def update_student():

    print()

    print("1. Update Student ID")

    print("2. Update Student Name")

    print("3. Update Student Roll Number")

    print("4. Update Student Department")

    print("5. Update Student Year")

    print("6. Update Student Marks")

    print()

    try:

        update_student_value = int(input("Enter Student ID to Update : "))

    except:

        print("Enter Number's Only")

        return
    
    for student in students:

        if update_student_value == int(student["id"]):

            try:

                update_value = int(input("Enter a number based on menu what you have to update : "))

            except ValueError:

                print("Enter Number's Only")

                return

            if update_value == 1:

                update_id = input("Update New ID : ")

                for other in students:
                    
                    if int(other["id"]) == int(update_id):
                        
                        print("ID Exit Already Create a New ID")
                        
                        return
                    
                else:
                        
                    student["id"] = update_id

        

            elif update_value == 2:

                update_name = input("Update New Name : ")

                student["Name"] = update_name

            elif update_value == 3:

                update_roll = input("Update New Roll Number : ")

                student["Roll No"] = update_roll

            elif update_value == 4:

                update_department = input("Update New Departmet : ")

                student["Department"] = update_department

            elif update_value == 5:

                update_year = input("Update the Year Of Student : ")

                student["Year"] = update_year

            elif update_value == 6:

                update_mark = input("Update New Mark : ")

                student["Mark"] = update_mark

            else:

                print("Enter Number Between 1 - 6")

    else:

        print("ID not found")

    print(students)

    with open("SMS.txt","w") as file:

        for student in students:

            for key,value in student.items():

                if type(value) == int:

                    value = str(value)

                file.write(key + ":" + value + "\n")

            file.write("\n")

def delete_student():

    try:

        del_student = int(input("Enter a Student ID to Delete Student : "))

    except ValueError:

        print("Enter Number's Only")

        return
    
   
    for i in range(len(students)):

        if del_student == int(students[i]["id"]):
                
            deleted_data = students.pop(i)

            break
    else:

        print("Before Delete Add Student then Delete it")

        return

    try:

        with open("SMS.txt","w") as file:

            for student in students:

                for key,value in student.items():

                    if type(value) == int:

                        value = str(value)

                    file.write(key + ":" + value + "\n")
                    
                file.write("\n")

    except FileNotFoundError:

        print("First Add a Student to Delete")

        return
 
def delete_all():

    with open("SMS.txt","w") as file:

        file.write("")

    students.clear()

while True:

    main_menu()

    try:

        User_choice = int(input("Enter Your Choice : "))

    except ValueError:

        print("Enter Numbers Only")

        continue

    if User_choice == 1:

        add_student()

    elif User_choice == 2:

        view_student()

    elif User_choice == 3:

        search_student()

    elif User_choice == 4:

        update_student()

    elif User_choice == 5:

        delete_student()    

    elif User_choice == 6:

        print("Thank You For Coming Have A Great Day :)")

        break

    elif User_choice == 7:

        print("All student records deleted successfully.")

        delete_all()

    else:

        print("Enter Numbers Between 1 - 7")