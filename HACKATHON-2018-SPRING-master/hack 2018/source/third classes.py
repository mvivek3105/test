# Hotel Reservation system
class Hotel:                                             #Base class
    def __init__(self, name):                            #intialising inint instructor
        self.hotelname = name

class HotelEmployee(Hotel):                             #Derived class
    def __init__(self, name,age,ssn,password,salary):   #Displaying all the hotel details
        self.employeename = name
        self.employeage = age
        self.employeessn = ssn
        self.__employeepassword = password              #private data member
        self.employeesalary = salary
class Room(Hotel):                                     #derived class from the base class
    def __init__(self,number,type,status):             #room details
        self.roomnumber = number
        self.roomtype = type
        self.roomstatus = status

class Occupant(Room):
    def __init__(self, name,phone,id,roomnumber):     #multiple inheritance where,the class is derived from above one.
        self.roomnumber=roomnumber                    #occupant details in the room
        self.occupantname = name
        self.occupantid = id                          #multilevel inheritance
        self.occupantphone = phone
    def display(self):
        print(self.occupantname,self.occupantphone,self.occupantid,self.occupantphone,self.roomnumber)

class Owner(Hotel):                                   #derived from the base class
    #  """ I'm the superior of everyone """           #super class
    def __init__(self, name,myhotel):
        self.ownername = name
        super().hotelname=myhotel

while True:                                          #Using while condition and break statement
    choice= int(input("what do you want to do? \n 1.Add Hotel \n 2.Add Employee \n 3.Add Room \n 4.Add booking \n 5.display booking \n 6.end"))
    if (choice == 1):
        hotelname = input("enter the hotel name")
        a = Hotel(hotelname)
    if (choice == 2):
        employeename = input("enter the employee name")
        employeeage = input("enter the employee age")
        employeessn = input("enter the employee ssn")
        employeepassword = input("enter the employee password")
        employeesalary = input("enter the employee salary")
        b = HotelEmployee(employeename,employeeage,employeessn,employeepassword,employeesalary)

    if (choice == 31):
        roomnumber = input("enter the room number")
        roomtype = input("ent1er the room type")
        roomstatus = input("enter the room status")
        c = Room(roomnumber,roomtype,roomstatus)

    if (choice == 4):
        customername= input("enter the name of customer")
        customerphone = input("enter the phone number of customer")
        customerid = input("enter the id of customer")
        roomnum = input("enter the room number customer has taken")
        d = Occupant(customername,customerphone,customerid,roomnum)

    if (choice==6):
        break

    if(choice==5):
        d.display()