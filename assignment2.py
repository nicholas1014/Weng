#WengChon Choi 500874095
class Person:

    #initialization of firstname,lastname,username,idnum
    def __init__(self,first_name,last_name,username,id_num):
        self.first_name=first_name
        self.last_name=last_name
        self.username=username
        self.id_num=id_num
    #setting the return of each element as string
    def __str__(self):
        #[:-1] is used to get rid of the "," when taking the firstnames from the text file
        strf=str(self.first_name[:-1])
        strl=str(self.last_name)
        stru=str(self.username)
        stri=self.id_num
        #\n is used to make each entry to appear in a new line
        return "First Name: "+strf+"\n"+ "Last Name: "+strl+"\n"+ "Username: "+stru+"\n"+"ID: "+stri+"\n"

#creating Student class with Person as ancestor
class Student(Person):
    pass
#creating the Instructor class with Person as ancestor
class Instructor(Person):
    pass
#creating the TeacherAssistant class with Person as ancestor
class TeacherAssistant(Person):
    pass

#creating the Parser class
class Parser:
    
    def __init__(self):
        #initializing the list for students,instructors and TA
        self.students=[]
        self.instructors=[]
        self.tas=[]
    
    def parse(self,filename):
        #open a file with the given name as read text file
        f=open(filename,"rt")
        content = f.readlines()

        for x in content:
            #this is to check each line of the document and prevent it grabing the header of the file
            if len(x.split(" ")) == 5 :
                #checking to see the role of each entry \n is included in the comparison because the split function grabs the end of the sentence as well
                if str(x.split(" ")[4]) == "Student\n":
                    #sorting the correct role into the correct list as well as grabbing their first name, last name, username and ID
                    self.students.append(Student(str(x.split(" ")[0]),str(x.split(' ')[1]),str(x.split(' ')[2]),str(x.split(' ')[3])))

                elif str(x.split(" ")[4]) == "TA\n":
                   #sorting the correct role into the correct list as well as grabbing their first name, last name, username and ID
                    self.tas+=[TeacherAssistant(str(x.split(" ")[0]),str(x.split(' ')[1]),str(x.split(' ')[2]),str(x.split(' ')[3]))]

                elif str(x.split(" ")[4]) =="Instructor\n":
                    #sorting the correct role into the correct list as well as grabbing their first name, last name, username and ID
                    self.instructors=[Instructor(str(x.split(" ")[0]),str(x.split(' ')[1]),str(x.split(' ')[2]),str(x.split(' ')[3]))]

        f.close()

    #return the list of students
    def get_students(self):
        return self.students
    #return the list of instructors
    def get_instructors(self):
        return self.instructors
    #return the list of TA
    def get_tas(self):
        return self.tas

#creating the main class
class Main:
    #instance variable of the class Parser
    def __init__(self): 
        self.parser=Parser()
    #using the parse method in parser to open the file
    def parse_file(self,filename):
        self.parser.parse(filename)


    #seaching for a specific list of students 
    def get_students(self,str1):
        #initializing the list of students that meets the criteria
        result=[]
        for i in self.parser.students:
            
            #to find the exact ID number of each student from the Person format
            j=str(i).split(" ")
            id= j[6]
            id=id[:-1]
            id=int(id)

            #search algorithm that compares the given str1 with the ID numbers
            def search(num,str1):
    
                while (num>0):
        
                    snum=str(num)
                    #this algorithm searches by comparing the list n number of digits of the ID number
                    #the n mentioned above is determined by the size of the str1
                    n = snum[len(snum)-1-len(str(str1)):len(snum)-1]
                    #after each comparison, the ID number is divided by 10 which is removing the last digit of the ID number and then it compares again
                    num= num//10
                    #if n is equal to the str1 the loop ends
                    if n==str(str1):
                       
                        return True
            #if the cireteria is met for this ID number, the information taged along this ID will be added into the new list
            if (search(id,str1) ==True):
                result.append(i)

        return result
    #creating a new text file and writing in it
    def write_to_file(self,person,filename):
        #opening a file or creating a new file with a given name
        with open(filename,"w") as wfile:
            #writing each entry of the list of person into the text file
            for people in person:
                #creates the format and creates an empty line between each entry
                wfile.write(str(people)+'\n')

