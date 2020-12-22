import students
import courses
def read_student_file(file_name,students_list):
    fi=open(file_name, "r")           #只读模式打开
    line1=fi.readline().strip()     
    while line1!="":
        tem_list=line1.split(sep=",")                 #拆分成独立字符串的列表
        item=students.Students(tem_list[0], tem_list[1], tem_list[2], tem_list[3])   #调用类对象
        line2=fi.readline().strip()                                         
        for i in range(int(line2)):
            tempLine=fi.readline().strip()                 
            item.add_courses(tempLine)
        students_list.append(item)
        line1=fi.readline().strip()
    fi.close()

def read_course_file(file_name,courses_list):
    fi = open(file_name, "r")
    line1 = fi.readline().strip()   #只读模式读取文件数据
    while line1!="":
        tem_list=line1.split(sep=",")    #拆成独立字符串的列表
        line2=fi.readline().strip()
        item=courses.Course(tem_list[0], tem_list[1],tem_list[2],tem_list[3],tem_list[4],line2)
        courses_list.append(item)
        line1=fi.readline().strip()
    fi.close()
    
def write_student_file(file_name, students_list):     #写入students数据
    fo=open(file_name, "w")
    for i in range(len(students_list)):      
        item=students_list[i]               
        str_result=""
        str_result+=item.get_name()+","+item.get_ID()+","+item.get_gender()+","+item.get_major()+"\n"
        str_result+=str(item.get_course_number())+"\n"
        for one in item.get_courses_list():
            str_result+=one+"\n"
        fo.write(str_result)
    fo.flush()
    fo.close()

def write_courses_file(file_name,courses_list):    #写入courses数据
    fo=open(file_name,"w")
    for i in range(len(courses_list)):
        item = courses_list[i]
        str_result=""
        str_result+=item.get_course_name()+","+item.get_course_ID()+","+item.get_credit()+","+item.get_teacher()+","+item.get_classroom()+"\n"
        str_result2=item.get_information()+"\n"
        fo.write(str_result)
        fo.write(str_result2)
    fo.flush()
    fo.close()

def search(courses_list):
    course_id=input("Please enter Course_ID: ")
    not_found=True
    i=0
    while i <len(courses_list) and not_found:
        if course_id==courses_list[i].get_course_ID():     #遍历整个列表判断是否存在
            not_found=False
        else:
            i+=1
    if not_found:
        print("\nCourse (ID=%s) is not found in the courses list." %(course_id))
    else:
        item=courses_list[i]
        print(item)

def show(courses_list):     #打印，注意一下格式
    print("========================================")
    print("All Courses Information")
    print("========================================")
    for i in courses_list:
        print("------------------------------")
        print(i)
    print()

def add(courses_list):
    course_id=input("Please enter Course ID: ")
    not_found=True
    i=0
    while i <len(courses_list) and not_found:
        if course_id==courses_list[i].get_course_ID():    #先判断是否已经存在
            not_found=False
        else:
            i+=1
    if not_found:                                            #若不存在，列表append方法增加，调用对象改值
        course_name=input("Please input course name: ")
        course_ID=course_id
        credit=input("Please input course credits: ")
        teacher=input("Please input course instructor: ")
        classroom=input("Please input course address: ")
        information=input("Please input course description: ")
        item=courses.Course(course_name,course_ID,credit,teacher,classroom,information)
        courses_list.append(item)
        print("Successfully added the Course(ID=%s)to the courses list." %(course_id))
    else:
        print("Course(ID=%s)already exists in the courses list."%(course_id))

def remove(courses_list,students_list):
    course_id=input("Please enter course ID: ")
    not_found=True
    i=0
    while i <len(courses_list) and not_found:
        if course_id==courses_list[i].get_course_ID():                 #先判断是否存在
            not_found=False
        else:
            i+=1
    if not_found:
        print("Course (ID=%s) is not found in the courses list." %(course_id))
    else:
        for a in range (len(students_list)):                            #删除课程同时遍历students列表删除学生选的这门课（调用drop方法）
            item = students_list[a]
            item.drop_course(course_id)
        del courses_list[i]
        print("Successfully deleted the Course (ID=%s) from the courses list." %(course_id))
    return courses_list

def update(courses_list):
    course_id = input("please enter course ID: ")
    not_found=True
    i=0
    while i <len(courses_list) and not_found:
        if course_id==courses_list[i].get_course_ID():                  #先判断要更新的课程是否存在
            not_found=False
        else:
            i+=1
    if not_found:
        print("\nCourse (ID=%s) is not found in the courses list." %(course_id))
    else:
        print("Before updating,the course information:")
        print("---------------------------------")
        item=courses_list[i]
        print(item)
        print("---------------------------------")               #接收用户输入再改
        del courses_list[i]
        course_name=input("Please enter course name: ")
        course_ID=course_id
        credit=input("Please enter course credits: ")
        teacher=input("Please enter course instructor: ")
        classroom=input("Please enter course address: ")
        information=input("Please enter course description: ")
        item=courses.Course(course_name,course_ID,credit,teacher,classroom,information)
        courses_list.append(item)
    return courses_list

def get_course_name(courses_list,course_id):
    for i in range (len(courses_list)):
        if course_id==courses_list[i].get_course_ID():        #遍历列表，把courseid转换成coursename的小函数
            return courses_list[i].get_course_name()
        
def retrieve(students_list,courses_list):
    student_id=input("Please enter Student ID: ")
    not_found=True
    i=0
    while i <len(students_list) and not_found:            #先判断是否存在
        if student_id==students_list[i].get_ID():
            not_found=False
        else:
            i+=1
    if not_found:
        print("\nStudent (ID=%s) is not found in the students list." %(student_id))
    else:
        item=students_list[i]
        print()
        print("Student Name: "+item.get_name())                         #打印修改后的值
        print("Student ID (Gender): "+item.get_ID()+" ("+item.get_gender()+")")
        print("Major: "+item.get_major())
        print("Selected Courses ("+str(item.get_course_number())+") :")
        for one in item.get_courses_list():
            name=get_course_name(courses_list, one)
            print("    "+one+": "+name)

def modify(students_list, courses_list):
    student_id=input("Please enter student ID: ")
    not_found=True
    i=0
    while i <len(students_list) and not_found:
        if student_id==students_list[i].get_ID():     #改学生的课程信息，先判断是否存在
            not_found=False
        else:
            i+=1
    if not_found:
        print("\nStudent (ID=%s) is not found in the students list." %(student_id))
    else:
        item=students_list[i]
        selection=input("Modify student (ID=%s) [major|enroll|drop]: ")
        if selection=="major":                                    #改专业，调用set方法
            major=input("Please enter student major: ")
            item.set_major(major)
            print()
            print("\nModified the major of Student (ID=%s)." %(student_id))
            print("----------------------------------------")
            print("Student Name: "+item.get_name())
            print("Student ID (Gender): "+item.get_ID()+" ("+item.get_gender()+")")
            print("Major: "+item.get_major())
            print("Selected Courses ("+str(item.get_course_number())+") :")
            for one in item.get_courses_list():
                name=get_course_name(courses_list,one)
                print("    "+one+": "+name)
                
        elif selection=="enroll":   #改课程，先看是否在里面，再调用enroll方法
            course_id=input("Please enter ID of course to be enrolled in: ")
            not_found_course=True
            index=0
            while index <len(courses_list) and not_found_course:
                if course_id==courses_list[index].get_course_ID():
                    not_found_course=False
                else:
                    index+=1
            if not_found_course:
                print("\nCourse (ID=%s) is not found in the courses list." %(course_id))
            else:
                courses_selected=item.get_courses_list()
                not_selected=True
                inx_selected=0
                while inx_selected<item.get_course_number() and not_selected:
                    if course_id==courses_selected[inx_selected]:
                        not_selected=False
                    else:
                        inx_selected+=1
                if not_selected:
                    item.enroll_course(course_id)
                    print()
                    print("\nModified the major of Student (ID=%s)." %(student_id))
                    print("----------------------------------------")
                    print("Student Name: "+item.get_name())
                    print("Student ID (Gender): "+item.get_ID()+" ("+item.get_gender()+")")
                    print("Major: "+item.get_major())
                    print("Selected Courses ("+str(item.get_course_number())+") :")
                    for one in item.get_courses_list():
                        name=get_course_name(courses_list, one)
                        print("    "+one+": "+name)
                else:
                    print("\nCourse (ID=%s) is already in the enrolled courses list." %(course_id))
            
        elif selection=="drop":     #删除学生选的课程，调用drop方法
            course_id=input("Please enter ID of course to be dropped: ")
            not_found_course=True
            index=0
            while index <len(courses_list) and not_found_course:
                if course_id==courses_list[index].get_course_ID():
                    not_found_course=False
                else:
                    index+=1
            if not_found_course:
                print("\nCourse (ID=%s) is not found in the courses list." %(course_id))
            else:
                courses_selected=item.get_courses_list()
                not_selected=True
                inx_selected=0
                while inx_selected<item.get_course_number() and not_selected:
                    if course_id==courses_selected[inx_selected]:
                        not_selected=False
                    else:
                        inx_selected+=1
                if not_selected:
                    print("\nCourse (ID=%s) is not in the enrolled courses list." %(course_id))
                else:
                    item.drop_course(course_id)
                    print()
                    print("\nModified the major of Student (ID=%s)." %(student_id))
                    print("----------------------------------------")
                    print("Student Name: "+item.get_name())
                    print("Student ID (Gender): "+item.get_ID()+" ("+item.get_gender()+")")
                    print("Major: "+item.get_major())
                    print("Selected Courses ("+str(item.get_course_number())+") :")
                    for one in item.get_courses_list():
                        name=get_course_name(courses_list,one)
                        print("    "+one+": "+name)                        
        else:
            print("\nNot a valid command - returning to main menu.")
        
def display(students_list,courses_list):          #打印，注意格式
    print("========================================")
    print("All Students Information")
    print("========================================")
    print("========================================")
    print("----------------------------------------")
    for item in students_list:
        print("Student Name: "+item.get_name())
        print("Student ID (Gender): "+item.get_ID()+" ("+item.get_gender()+")")
        print("Major: "+item.get_major())
        print("Selected Courses ("+str(item.get_course_number())+") :")
        for one in item.get_courses_list():
            name=get_course_name(courses_list, one)
            print("    "+one+": "+name)
        print("----------------------------------------")
        print()
    print("========================================")

def insert(students_list):                   #增加学生信息
    student_id=input("Please enter student ID: ")
    is_duplicated=False
    i=0
    while i <len(students_list) and is_duplicated==False:
        if student_id==students_list[i].get_ID():
            is_duplicated=True
        else:
            i+=1
    if is_duplicated:
        print("Student (ID=%s) already exists in the students list." %(student_id))
    else:
        student_name=input("Please enter student name: ")
        gender=input("Please enter student gender(m/f): ")
        major=input("Please enter student major: ")
        item=students.Students(student_name, student_id, gender, major)
        students_list.append(item)
        print("Successfully inserted the Student (ID=%s) into the students list." %(student_id))

def delete(students_list):       #删除学生信息
    student_id=input("Please enter student ID: ")
    not_found=True
    i=0
    while i <len(students_list) and not_found:
        if student_id==students_list[i].get_ID():
            not_found=False
        else:
            i+=1
    if not_found:
        print("Student (ID=%s) is not found in the students list." %(student_id))
    else:
        del students_list[i]
        print("Successfully deleted the Student (ID=%s) from the students list." %(student_id))
    return students_list

def main():               #主函数
    students_list = []
    courses_list = []
    read_student_file("students.txt",students_list)
    read_course_file("courses.txt",courses_list)
    to_be_continued = True
    while to_be_continued == True:
        print()
        print()
        print()
        print("------------------------------------------------------------")
        print("The choice to maintain COURSEs information[add|remove|update|search|show]")
        print("The choice to maintain STUDENTs information[insert|delete|modify|retrieve|display]")
        print("The choice quit means to finish the program.[quit]")
        print()
        print()
        print()
        choice=input("Please enter choice: ")
        if choice=="retrieve":
            retrieve(students_list,courses_list)
        elif choice=="delete":
            delete(students_list)
        elif choice=="modify":
            modify(students_list,courses_list)
        elif choice=="insert":
            insert(students_list)
        elif choice=="display":
            display(students_list,courses_list)
        elif choice=="search":
            search(courses_list)
        elif choice=="remove":
            remove(courses_list,students_list)
        elif choice=="update":
            update(courses_list)
        elif choice=="add":
            add(courses_list)
        elif choice=="show":
            show(courses_list)
        elif choice=="quit":
            print("Quit")
            to_be_continued=False
            write_student_file('new_students.txt',students_list)
            write_courses_file('new_courses.txt',courses_list)
        else:
            print('command not found,please enter again.')

main()

