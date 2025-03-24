# Class `Human`
class Human():
    """`Human` Class (Parent/Super Class)"""
    
    def __init__(self): 
        """`init` method with `self` parameter"""
        
        super(Human, self).__init__() # Inherits from Superclass by 
                                    # the`super` function
        print("I'm a human!")

# Class `Student`
class Student(Human): # Inheriting the Parent Class `Human`
    
    """Student Class (Child/Sub Class)"""
    def __init__(self, grade): 
        """`init`` method with `self` and `grade` parameters"""
        
        super(Student, self).__init__() # Inherits from Superclass by 
                                        # the`super` function
        print(f"My grade is {grade}!")
        
if __name__ == "__main__": # runs only if its being run from the 
                        # same script and not any other
    Student_1 = Student(7)
