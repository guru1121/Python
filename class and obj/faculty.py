
# class Faculty:
#     def __init__(self):
#         self.id = int(input("Enter Id :"))
#         self.name = input("Enter name:")
#         self.salary = float(input("Enter salary:"))
        
#     def display(self):
#         print("faculty Id:", self.id) 
#         print("faculty Name:", self.name) 
#         print("faculty salary:", self.salary) 
        
# f1 = Faculty()
# f1.display()

class Student:
    def __init__(self, a, b, c):
        self.S_id = a
        self.name = b
        self.roll_no = c
    
    def display_data(self):
        print(self.S_id, self.name, self.roll_no)
        
a = Student(1, "varun", 121)
a.display_data()

b = Student(2, "Guru", 122)
b.display_data()