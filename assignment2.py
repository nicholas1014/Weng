#WengChon Choi 500874095
class Person:

    def __init__(self,first_name,last_name,username,id_num):
        self.first_name=first_name
        self.last_name=last_name
        self.username=username
        self.id_num=id_num

    def __str__(self):
        strf=str(self.first_name[:-1])
        strl=str(self.last_name)
        stru=str(self.username)
        stri=self.id_num
        return "First Name: "+strf+"\n"+ "Last Name: "+strl+"\n"+ "Username: "+stru+"\n"+"ID: "+stri+"\n"


class Student(Person):
    pass


class Instructor(Person):
    pass

class TeacherAssistant(Person):
    pass

class Parser:
    
    def __init__(self):
        self.students=[]
        self.instructors=[]
        self.tas=[]
    
    def parse(self,filename):
        f=open(filename,"rt")
        content = f.readlines()

        for x in content:
            if len(x.split(" ")) == 5 :
                
                if len(str(x.split(" ")[4])) == 8:

                    self.students.append(Student(str(x.split(" ")[0]),str(x.split(' ')[1]),str(x.split(' ')[2]),str(x.split(' ')[3])))
                elif len(str(x.split(" ")[4])) == 3:
                   
                    self.tas+=[TeacherAssistant(str(x.split(" ")[0]),str(x.split(' ')[1]),str(x.split(' ')[2]),str(x.split(' ')[3]))]
                elif len(str(x.split(" ")[4])) ==11:
                    
                    self.instructors=[Instructor(str(x.split(" ")[0]),str(x.split(' ')[1]),str(x.split(' ')[2]),str(x.split(' ')[3]))]


        for stu in self.tas:
            print (stu) 

        f.close()

    def get_students(self):
        return self.students

    def get_instructors(self):
        return self.instructors
    
    def get_tas(self):
        return self.tas


class Main:

    def __init__(self): 
        self.parser=Parser()
    
    def parse_file(self,filename):
        self.parser.parse(filename)

    def get_students(self,str1):

        result=[]

        for i in self.parser.tas:
            
            print(str(i))
            j=str(i).split(" ")
            print(j)
            print (len(j))
            id= j[6]
            id=int(id[:-1])
            print (id)

            finder=0

            def findstr1(id,str1):
                while (id>0):
                    if (id % 10 ==str1):
                        break
                    id = id/10
                return (id>0) 

            for num in range(0,id):
                if (num == id or findstr1(id,str1)):
                    finder+=1

            if (finder>0):
                result.append(i)

    def write_to_file(self,person,filename):

        with open(filename,"wt") as wfile:
            
            for people in person:
                wfile.write(people)

