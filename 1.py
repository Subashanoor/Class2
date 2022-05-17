student_details={}

# def course(sub):
#     sub=input("Enter the Course code")

def add():
    name=input("Enter your name")
    grade= input("Enter your grade in course")
    student_details[name]=grade
    if len(student_details)==1:
        print("\nEnter another name")
        add()
    else:
        print(student_details)

def search():
    if len(student_details)==0:
        print("There is no details present!")
        
    elif len(student_details)!=0:
        output=input("Enter the name to be searched")
        if output in student_details.keys():
            print("---------------------------------")
            print(" Name: " +output+ "\n Grade: "+ student_details[output])
            print("---------------------------------")
            
        else:
            print( "Student name does not exists!")
def update_delete():
    if len(student_details)!=0:
        select=input("Select 1.Update or 2.Delete: ")
        if select=="1":
            
            name1=input("Enter student name: ")
            grade1=input("Enter grade")
            if name1 in student_details.keys():
                student_details[name1]= grade1
                print(student_details)
                
        elif select=="2":
            name3=input("Enter student name: ")
            if name3 in student_details.keys():
                student_details.pop(name3)
                print(student_details)
        else:
            print("Wrong selection made!\n\n")
            print("********************************")
            update_delete()
        

add()
search()
update_delete()
#def add_student():


# for option=input(" Want to add your more course, press Y or want to search, press N"):
#     if option ==Y:
#        course(sub)
#        name.append(sub)
#        score(grade)
#        name.append(grade)
#    else:
#        search(name)
#        print(name)