import datetime
import re
from datetime import *
import csv

class Employee:

    path = "Details.csv"
    Designation_list = ["Manager","Employee","Intern","Student"]
    minlen = 5


    def __init__(self, x):

        self.name = x[0]
        self.username = x[1]
        self.email = x[2]
        self.password = x[3]
        self.jod = x[4]
        self.dob = x[5]
        self.number = x[6]
        self.Designation = x[7]
        self.street = x[8]
        self.city = x[9]
        self.State = x[10]
        self.zip = x[11]

    def validate_name(self):
        """Validates name for given condition"""

        #checks if the name is string or not
        if (type(self.name)) != str:
            raise TypeError('Name must be a string')

        # #checks if the name contains only alphabets or not
        # if not self.name.replace(" ","").isalpha():
        #     print('Name must contain alphabet only')
        #     return False
        return True


    def validate_user(self):
        """validates username for given conditions"""
        if type(self.username) != str:
            raise TypeError("username must be a string")

       # self.usernames can't be shorter than minlen
        if len(self.username) < self.minlen:
            print(f'username should be greater than {self.minlen}')
            return False

        # self.usernames can only use letters, numbers, dots and underscores
        if not re.match('^[a-zA-Z0-9._]*$', self.username):
            print('usernames can only use letters, numbers, dots and underscores')
            return False

        #self.usernames can't begin with a number
        if self.username[0].isnumeric():
            print('usernames can not begin with a number')
            return False
        return True

    def validate_email(self):
        """validates email for given conditions"""
        reg_ex = r'\b[A-Za-z0-9]+@+[a-z]+\.[A-Z|a-z]{2,}\b'

        # checks if email is a string or not
        if not type(self.email) == str:
            print('Email must be a string')
            return False

        #maps the regular expression with the password
        if not re.match(reg_ex, self.email):
            print("Invalid Email Address")
            return False
        return True

    def validate_password(self):
        """validates password for given conditions"""
        #checks if length of the password is greater than 8 or not and if the pasword is ap=lphabets only
        if len(self.password) < 8 or self.password.isalpha():
            print("Invalid Password")
            return False

        #maps the regular expression with the  # #Trupti98
        if not ((re.search("[A-Za-z]",self.password) and re.search("[0-9]",self.password) and re.search("[_@$]",self.password))):
            print("Invalid Paassword")
            return False
        return True

    def validate_number(self):
        """validates number for given conditions"""

        #checks if number is integer or not
        # if not (type(self.number) == int):
        #     print('Number should be integer')
        #     return False

        #checks if number is 10 digit or not
        # if not len(str(self.number)) == 10:
        #     print('Number should be 10 digits')
        #     return False

        #checks if number is only digit or not
        if not (str(self.number).isdigit()):
            print('Number should consist only digits')
            return False
        return True

    def validate_designation(self):
        """validates designation for given conditions"""

        #checks if designation is present in the given list
        if self.Designation not in self.Designation_list:
            print(f"choose a designation from {self.Designation_list}")
            return False

        #checks if the designation is string or not
        if type(self.Designation) != str:
            print('Designation must be string')
            return False
        return True

    def validate_address(self):
        """validates address for given conditions"""

        #checks if given address attributes are string or not
        if type(self.street) and type(self.city) and type(self.State) and type(self.zip) == str and len(self.zip) == 6:
            return True
        else:
            return False

    def validate_jod_date(self):
        """validates joining date for given conditions"""

        #checks the format of the given date
        try:
            datetime.strptime(self.jod, '%Y-%m-%d')
            return True
        except:
            return False

    def validate_dob_date(self):
        """validates date of birth for given conditions"""

        # checks if the format of the given date
        try:
            datetime.strptime(self.dob, '%Y-%m-%d')
            return True
        except:
            return False


    def create_file(self):
        '''Creates File and writes appropriate attributes if the validations are fullfilled'''
        FIELDS = ['NAME','USER','EMAIL','PASSWORD','STREET','CITY','STATE','ZIP','NUMBER','DESIGNATION','JOD','DOB']
        y = []
        f = open(self.path,'a')
        csvwriter = csv.writer(f)
        try:
            if self.validate_name():
                y.append({self.name})
            else:
                y.append("None")
            if self.validate_user():
                y.append(self.username)
            else:
                y.append("None")
            if self.validate_email():
                y.append(self.email)
            else:
                y.append("None")
            if self.validate_password():
                y.append(self.password)
            else:
                y.append("None")
            if self.validate_address():
                y.extend([self.street,self.city,self.State,self.zip])
            else:
                y.extend(["None","None","None","None"])
            if self.validate_number():
                y.append(self.number)
            else:
                y.append("None")
            if self.validate_designation():
                y.append(self.Designation)
            else:
                y.append("None")
            if self.validate_jod_date() and self.validate_dob_date():
                y.extend([self.jod,self.dob])
            else:
                y.extend(["None","None"])
            print(f'This is y: {y}')
            csvwriter.writerow(y)
            f.close()
        except:
            raise FileNotFoundError


def main():
    test_cases = [
        ['Vaishnavi 67 Rathod', 'rathod', "vrathod24@gmail.com", "rathodV@247", '03-03-03', '12-12-27', 832944932873,
         "Manager", "Besa Street", "Nagpur", "Maharashtra", "445507"],
        ['Vaishnavi Rathod', 'rathod@', "vrathod24@gmail.com", "rathodV@247", '03-03-03', '2001-08-09', '832944932873',
         "Manager", "Besa Street", "Nagpur", "Maharashtra", "445507"],
        ['1234', 'rathod 21', "vrathod24@gmail.com", "rathodV@247", '2019-03-03', '2001-02-02', 8329932873, "Manager",
         "Besa Street", "Nagpur", "Maharashtra", "44550734"],
        ['Vaishnavi Rathod', 'Vrathod', "vrathod24@gmail.com", "rathodV@247", '03-03-03', '12-12-27', 832944932873, "X",
         "Besa Street", "Nagpur", "Maharashtra", "445507"],
        ['Vaishnavi  Rathod', 'Vrathod', "vrathod24@gmail.com", "rathodV@247", '2019-03-03', '2001-03-07', 8329932873,
         "Manager", "Besa Street", "Nagpur", "Maharashtra", "4455007"]]

    for x in test_cases:
        emp = Employee(x)
        emp.create_file()


if __name__ == '__main__':
    main()