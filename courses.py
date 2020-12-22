class Course:
    def __init__ (self,course_name,course_ID,credit,teacher,classroom,information):
        self.__course_name = course_name
        self.__course_ID = course_ID
        self.__credit = credit
        self.__teacher = teacher
        self.__classroom = classroom
        self.__information = information

    def set_course_name(self,course_name):
        self.__course_name = course_name

    def set_course_ID(self,course_ID):
        self.__course_ID = course_ID

    def set_credit(self,credit):
        self.__credit = credit

    def set_teacher(self,teacher):
        self.__teacher = teacher

    def set_classroom(self,classroom):
        self.__classroom = classroom

    def set_information(self,information):
        self.__information = information

    def get_course_name(self):
        return self.__course_name

    def get_course_ID(self):
        return self.__course_ID

    def get_credit(self):
        return self.__credit

    def get_teacher(self):
        return self.__teacher

    def get_classroom(self):
        return self.__classroom

    def get_information(self):
        return self.__information

    def __str__(self):
        string='Course Name:'+self.__course_name+'\n'
        string+='Course ID|Credits:'+self.__course_ID+'|'+self.__credit+'\n'
        string+='Instructor Name:'+self.__teacher+'\n'
        string+='Address:'+self.__classroom+'\n'
        string+='Description:'+self.__information
        return string


   
