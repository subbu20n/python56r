# #--------------------practice Task on loops--------------------------

# from abc import ABC, abstractmethod


# class Person(ABC): 
#     def __init__(self,name,age): 
#         self.name = name 
#         self.age = age 

#     @abstractmethod 
#     def get_role(self): 
#         pass 

# class Student(Person): 
#     def __init__(self,student_id,name,age): 
#         super().__init__(name,age) 
#         self.student_id = student_id
#         self.enrolled_courses = [] 

#     def get_role(self): 
#         return 'student' 

#     def get_enrolled_courses(self):
#         print(self.enrolled_courses) 

#     def add_a_course(self,course_name):
#         self.enrolled_courses.append(course_name) 

# class Course: 
#     def __init__(self,course_name,course_code): 
#         self.course_name = course_name 
#         self.course_code = course_code  
#         self.teacher = None  
#         self.enrolled_students = [] #n no . of courses we can add 

#     def set_teacher(self,teacher_name): 
#         self.teacher_name = teacher_name  

#     def add_students(self,students_name): 
#         self.enrolled_students.append(students_name)  

#     def show_details(self): 
#         print(self.course_name) 
#         print(self.course_code) 
#         print(self.enrolled_students) 
#         print(self.teacher) 

# stu1 = Student(2,'subbu',21) 
# print(stu1.name)         #subbu                          

# stu1.get_enrolled_courses() #[] empty list  

# stu1.add_a_course('dbms') 
# stu1.add_a_course('oops') 
# stu1.add_a_course('os') 

# stu1.get_enrolled_courses() #['dbms', 'oops', 'os']




#----------------------------DUNDER METHOD--------------------------------------

class Point: 
    def __init__(self,x_pos,y_pos,z_pos): 
        self.x_pos = x_pos 
        self.y_pos = y_pos 
        self.z_pos = z_pos 

    def __add__(self,other): 
        new_x_pos = self.x_pos + other.x_pos 
        new_y_pos = self.x_pos + other.y_pos 
        new_z_pos = self.z_pos + other.z_pos  
        return new_x_pos , new_y_pos , new_z_pos 

    def __gt__(self,other): 
        return self.x_pos , self.y_pos , self.z_pos 

p1 = Point(1,2,3) # this order we have to corressponding values x+x ,y+y, z+z 
p2 = Point(3,4,5) 

# print(p1 + p2)  
# print(p1 > p2) #it consider as o/p as tuple type "bool" # (1,2,3) 


#---------------------------------DUCK TYPING------------------------------------ 
# duck typing: it does not care about function type it wants attributes has defined or not thats the matter 
class GameCordinates: 
    def __init__(self,player_name,x_pos,y_pos,z_pos): 
        self.player_name = player_name 
        self.x_pos = x_pos 
        self.y_pos  = y_pos 
        self.z_pos  = z_pos  

gc1 = GameCordinates('subbu',2,4,5)  

# print(p1 + p2) 
print(p1 + gc1) #(3, 5, 8)    
#p1.__add__(gc1) --->DUCK TYPING p1=x_pos + gc1=x_pos = duck typing  

#gc1.__add__(p1) ---> this wont works (duck typing always sees position attributes) --> ok 