
from assignment2 import *


def test():
    in_file = "class_list"
    out_file = "new_list"
    
    main = Main()
    main.parse_file(in_file )
    students = main.get_students("91")
    main.write_to_file(students, out_file)
    
    
if __name__ == "__main__":
    test()
