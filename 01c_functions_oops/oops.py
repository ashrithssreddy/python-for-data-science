class employee:
    pass

emp_1 = employee()
emp_2 = employee()
    

print(emp_1)
emp_1.name = "ash red"
emp_1.email= "ashred@gmail.com"
print(emp_1)
print(emp_1.name)
print(emp_1.email)



############ Edit attributes of an instance ############ 
class employee:
    def __init__(self, name, pay): 
        self.name = name
        self.pay = pay        
        self.email = name + "@gmail.com"
        
    def print_name(self): # this is a method
        print(self.name)        
        
    def apply_new_year_bonus(self, bonus = 10):
        self.pay = self.pay + bonus
            
e1 = employee("him misra", 100) # e1 will be passed as self
e1
e1.name
e1.email # not brackets as email is an attribute of the class
e1.print_name() # need brackets since, print_name is a method
employee.print_name(e1) # works too. class_name.method_name(object_instance)
# e1.print_name_junk() # error since self if ommitted

e1.pay
e1.apply_new_year_bonus(bonus = 2)
e1.pay

e1.pay
employee.apply_new_year_bonus(e1, bonus = 2)
e1.pay



############ Class attributes ############ 
class employee:    
    new_year_bonus = 10
    
    def __init__(self, name, pay): 
        self.name = name
        self.pay = pay        
        self.email = name + "@gmail.com"
        
    def print_name(self): # this is a method
        print(self.name)        
        
    def apply_new_year_bonus(self):
        # self.pay = self.pay + new_year_bonus # error
        # self.pay = self.pay + employee.new_year_bonus # works
        self.pay = self.pay + self.new_year_bonus # works
                
e1 = employee("him misra", 100) # e1 will be passed as self
# getattr(e1) # fails
e1.__dict__
employee.__dict__

employee.new_year_bonus
e1.new_year_bonus

e1.pay
e1.apply_new_year_bonus() # bonus = 2
e1.pay

e1.whatever_attr = 999
e1.whatever_attr
e1.__dict__

e1.new_year_bonus = 999
e1.__dict__


e2 = employee("ash red", 766)
e2.whatever_attr
e2.__dict__
e2.new_year_bonus = 999
e1.__dict__


############ Update Class ############ 
class employee:    
    employee_count = 0
    new_year_bonus = 10
    
    def __init__(self, name, pay): 
        self.name = name
        self.pay = pay        
        self.email = name + "@gmail.com"
        employee.employee_count = employee.employee_count + 1
        
    @classmethod
    def from_string(cls, data_string):
        name, pay = data_string.split("-")
        return cls(name, int(pay))
        
    def print_name(self): # this is a method
        print(self.name)        
        
    def apply_new_year_bonus(self):
        # self.pay = self.pay + new_year_bonus # error
        # self.pay = self.pay + employee.new_year_bonus # works
        self.pay = self.pay + self.new_year_bonus # works
    
    @classmethod
    def set_new_year_bonus(cls, amt):
        cls.new_year_bonus = amt
        # cls.new_year_bonus = amt + cls.new_year_bonus # works too

# update an attribute in class and all instances                
employee.employee_count # 0

e1 = employee("ash red", 100)
employee.employee_count # 1
e1.employee_count

e2 = employee("what ever", 200)
employee.employee_count # 2
e2.employee_count # e1 and e2 employee count updates to 2

# classmethod - update new_year_bonus for class and all instances
e1 = employee("ash red", 100)
e1.new_year_bonus
e2 = employee("what ever", 200)
e2.new_year_bonus
employee.set_new_year_bonus(44)

employee.new_year_bonus
e1.new_year_bonus
e2.new_year_bonus

# classmethod - generate instances dynamically 
e3 = employee.from_string("ashrith reddy-100")
e3.name
e3.pay
e3.__dict__
e3.new_year_bonus
e3.apply_new_year_bonus(); e3.pay


############ Inheritence ############ 
class developer(employee): # Developer inherits from employee
    
    new_year_bonus = 200
    
    pass

print(help(developer))

dev_1 = developer("apple", 400)
dev_1.email
dev_1.pay


dev_1.apply_new_year_bonus()
dev_1.pay

    