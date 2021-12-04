from main import *

test_cases = [['Vaishnavi 67 Rathod', 'rathod',"vrathod24@gmail.com", "rathodV@247",'03-03-03','12-12-27',832944932873, "Manager", "Besa Street", "Nagpur", "Maharashtra", "445507"],
              ['Vaishnavi Rathod', 'rathod@',"vrathod24@gmail.com", "rathodV@247",'03-03-03','2001-08-09','832944932873', "Manager", "Besa Street", "Nagpur", "Maharashtra", "445507"],
              ['1234', 'rathod 21',"vrathod24@gmail.com", "rathodV@247",'2019-03-03','2001-02-02',8329932873, "Manager", "Besa Street", "Nagpur", "Maharashtra", "44550734"],
              ['Vaishnavi Rathod', 'Vrathod',"vrathod24@gmail.com", "rathodV@247",'03-03-03','12-12-27',832944932873, "X", "Besa Street", "Nagpur", "Maharashtra", "445507"],
              ['Vaishnavi  Rathod', 'Vrathod',"vrathod24@gmail.com", "rathodV@247",'2019-03-03','2001-03-07',8329932873, "Manager", "Besa Street", "Nagpur", "Maharashtra", "4455007"]]

dict = [{'name':False,'username':True,"email":True,'password':True,'jod':False,'dob':False,'number':False,'designation':True,'address':True},
{'name':True,'username':False,"email":True,'password':True,'jod':False,'dob':True,'number':False,'designation':True,'address':True},
{'name':False,'username':False,"email":True,'password':True,'jod':True,'dob':True,'number':True,'designation':True,'address':False},
{'name':True,'username':True,"email":True,'password':True,'jod':False,'dob':False,'number':False,'designation':False,'address':True},
{'name':True,'username':True,"email":True,'password':True,'jod':True,'dob':True,'number':True,'designation':True,'address':False}
]
class TestEmployee(): #name ,username,email,password,jod,dob,number,designation,street,city,state,zip

    def __init__(self,emp):
        self.emp = emp

    def test_name(self,i):
       if self.emp.validate_name() == dict[i]['name']:
           return True
       else:
           return False

    def test_email(self,i):
        if self.emp.validate_email() == dict[i]['email']:
            return True
        else:
            return False

    def test_address(self,i):
        if self.emp.validate_address() == dict[i]['address']:
            return True
        else:
            return False

    def test_username(self,i):
        if self.emp.validate_user() == dict[i]['username']:
            return True
        else:
            return False

    def test_number(self,i):
        if self.emp.validate_number() == dict[i]['number']:
            return True
        else:
            return False

    def test_password(self,i):
        if self.emp.validate_password() == dict[i]['password']:
            return True
        else:
            return False

    def test_jod(self,i):
        if self.emp.validate_jod_date() == dict[i]['jod']:
            return True
        else:
            return False

    def test_dob(self,i):
        if self.emp.validate_dob_date() == dict[i]['dob']:
            return True
        else:
            return False

    def test_designation(self,i):
        if self.emp.validate_designation() == dict[i]['designation']:
            return True
        else:
            return False


def run(emp,i):
    x = TestEmployee(emp=emp)
    n = x.test_name(i)
    u = x.test_username(i)
    e = x.test_email(i)
    p = x.test_password(i)
    nu = x.test_number(i)
    j = x.test_jod(i)
    b = x.test_dob(i)
    a = x.test_address(i)
    d = x.test_designation(i)
    return n,u,e,p,nu,j,b,a,d


def test(): #name ,username,email,password,jod,dob,number,designation,street,city,state,zip
    name = 0
    email = 0
    password = 0
    username = 0
    number = 0
    address = 0
    dob = 0
    jod = 0
    desig = 0

    i=0
    for a in test_cases:
        emp = Employee(a)
        n,u,e,p,nu,j,b,a,ds = run(emp,i)
        i += 1

        if not n:
            name += 1
        if not u:
            username +=1
        if not e:
            email += 1
        if not p:
            password += 1
        if not nu:
            number += 1
        if not  j:
            jod += 1
        if not  b:
            dob += 1
        if not  a:
            address += 1
        if not ds:
            desig += 1

    Total = name+username+email+password+number+jod+dob+address
    print(f'{name} no of test cases failed for name')
    print(f'{username} no of test cases failed for username')
    print(f'{email} no of test cases failed for email')
    print(f'{password} no of test cases failed for password')
    print(f'{number} no of test cases failed for number')
    print(f'{jod} no of test cases failed for joining date')
    print(f'{dob} no of test cases failed for birth date')
    print(f'{address} no of test cases failed for adress')
    print(f'{desig} no of test cases failed for designation')
    print(f'{Total} no of test cases failed')
    print('-----------------------------------------------------\n')
test()




