import psycopg

#Opening a connection to the database so queries can be made
with psycopg.connect("dbname=students user=postgres password=postgres") as conn:
    
    with conn.cursor() as cur:
        
        #getting all students from db and then printing them out
        def getAllStudents():
            cur.execute("SELECT * FROM students")
            for record in cur:
                print(record)
        #adding the student, and then committing the changes to the database
        def addStudent(first_name, last_name, email, enrollment_date):
            cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES(%s, %s, %s, %s);", (first_name, last_name, email, enrollment_date))
            conn.commit()
        #updating the students email, and then committing the changes to the database
        def updateStudentEmail(student_id, new_email):
            cur.execute("UPDATE students SET email = %s WHERE student_id = %s;", (new_email, student_id))
            conn.commit()
        #deleting the student, and committing the changes
        def deleteStudent(student_id):
            cur.execute("DELETE FROM students WHERE student_id = "+student_id+";")
            conn.commit()
            
        #Allowing the user to choose which function to run until they quit
        print("Select an option:\n1. View all students\n2. Add a student\n3. Update a student's email\n4. Delete a Student\nQ: Quit")
        choice = input()
        while choice != "Q" and choice != "q":
            if choice == "1":
                getAllStudents()
            elif choice == "2":
                print("Enter the student's first name:")
                first_name = input()
                print("Enter the student's last name:")
                last_name = input()
                print("Enter the student's email address:")
                email = input()
                print("Enter the student's enrollment date:")
                enrollment_date = input()
                addStudent(first_name, last_name, email, enrollment_date)
            elif choice == "3":
                print("Enter the student's id:")
                student_id = input()
                print("Enter the student's new email address:")
                new_email = input()
                updateStudentEmail(student_id, new_email)
            elif choice == "4":
                print("Enter the id of the student to be deleted:")
                student_id = input()
                deleteStudent(student_id)
            else: print("Invalid choice - select a number, or enter Q to quit.")

            print("Select an option:\n1. View all students\n2. Add a student\n3. Update a student's email\n4. Delete a Student\nQ: Quit")
            choice = input()
            


        