class Students:
    def __init__(self,name,ID,gender,major):
        self.__name=name
        self.__ID=ID
        self.__gender=gender
        self.__major=major
        self.__course_number=0
        self.__courses_list=[]

    def get_name(self):
        return self.__name

    def get_ID(self):
        return self.__ID

    def get_gender(self):
        return self.__gender

    def get_major(self):
        return self.__major

    def get_course_number(self):
        return self.__course_number

    def get_courses_list(self):
        return self.__courses_list

    def set_name(self,name):
        self.__name = name

    def set_ID(self,ID):
        self.__ID = ID

    def set_gender(self,gender):
        self.__gender = gender

    def set_major(self,major):
        self.__major = major

    def set_course_number(self,course_number):
        self.__course_number = course_number

    def set_courses_list(self,courses_list):
        self.set_course_number(len(courses_list))
        self.__courses_list=courses_list

    def __str__(self):
        string="studet_name: "+self.__name+'\n'
        string+="student_ID: "+self.__ID+'\n'
        string+="gender: "+self.__gender+'\n'
        string+="major: "+self.__major+'\n'
        string+="The Number of courses: "+str(self.__course_number)+'\n'
        for item in self.__courses_list:
            string+="    "+item+'\n'
        return string
    
    def is_added(self, course):
        found=False
        for item in self.__courses_list:
            if course==item:
                found=True
        return found

    def add_courses(self,course):
        if not self.is_added(course):
            self.__courses_list.append(course)
            self.__course_number+=1
            return True
        else:
            return False

    def enroll_course(self,course):
        self.__course_number+=1
        self.__courses_list.append(course)

    def drop_course(self,course_id):
        if self.is_added(course_id):
        	self.__course_number-=1
        	self.__courses_list.remove(course_id)
    
