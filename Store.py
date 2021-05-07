import mysql.connect
import json as js
import pandas as pd
import random
my_db = mysql.connector.connect(host='localhost',user='root',password='password')
my_cursor = my_db.cursor()

my_cursor.execute('create database Storedb')
my_db =

mysql.connector.connect(host='localhost',user='root',password='password',database='Storedb')

my_cursor = my_db.cursor()


my_cursor.execute('create table Sales(id int primary key AUTO_INCREMENT,name varchar(30),Product Brand varchar(30),Product Model varchar(30),Total int,Quantity int))

class Start:

    def start(self):

        print("Welcome to NationalOnline Electronics")
        obj = input("Enter B to Buy,C to cancel")
        return obj
class ops:
    def ops(self):

        ans=input("close counter?Y/N")
        if ans=='N':

            run.runner()
        else:
		my_cursor.execute('select* from Sales')
            	result=my_cursor.fetchall()

		    for i in result:

			    print(i)





class Gadgets:
    def __init__(self):

        self.seg_no=0

    def info(self):
        print("Which segment would you like to buy today?")
        print("~~~~~~~~~~Segment~~~~~~~~~~")
        print("    1. Smart Phones        ")
        print("    2. Televisions         ")
        print("    3. Laptops             ")
        seg_no = int(input('Enter your choice'))
        return seg_no

class Mobiles:


    def Mobiles(self):
        end='N'

        k=0
        bill=0
        mdchoice=0
        csquant=0
        selectmobbrand=[]
        Apple = ('iphone 12 max pro', 'iphone 11 pro max', 'iphone XR', 'iphone SE')
        Oneplus = ('Oneplus7', 'Oneplus 7T', 'Onepuls 8', 'Oneplus Nord')
        xiaomi = ('Redmi Note 7', 'Redmi Note 10')
        Realme = ('Realme 3', 'Realme 7')
        Samsung = ['Galaxy Note 10', 'Galaxy Duos', 'Galaxy F62']
        All_Mob = {"Apple": {1: 'iphone 12 max pro', 2: 'iphone 11 pro max', 3: 'iphone XR', 4: 'iphone SE'},
                   "Oneplus": {1: 'Oneplus7', 2: 'Oneplus 7T', 3: 'Onepuls 8', 4: 'Oneplus Nord'},
                   "xiaomi": {1: 'Redmi Note 7', 2: 'Redmi Note 10'}, 'Realme': {1: 'Realme 3', 2: 'Realme 7'},
                   "Samsung": {1: 'Galaxy Note 10', 2: 'Galaxy Duos', 3: 'Galaxy F62'}}
        Mob_Brand = {1: 'Apple', 2: 'Samsung', 3: 'Oneplus', 4: 'xiaomi', 5: 'Realme'}
        Apple_quant = {'iphone 12 max pro': 10, 'iphone 11 pro max': 10, 'iphone XR': 10, 'iphone SE': 10}
        Samsung_quant = {'Galaxy Note 10': 10, 'Galaxy Duos': 10, 'Galaxy F62': 10}
        Realme_quant = {'Realme 3': 10, 'Ralme 7': 10}
        Oneplus_quant = {'Oneplus7': 10, 'Oneplus 7T': 10, 'Onepuls 8': 10, 'Oneplus Nord': 10}
        xiaomi_quant = {'Redmi Note 7': 10, 'Redmi Note 10': 10}
        Apple_pr = {'iphone 12 max pro': 150000, 'iphone 11 pro max': 117100, 'iphone XR': 48000, 'iphone SE': 29590}
        Sam_pr = {'Galaxy Note 10': 117000, 'Galaxy Duos': 9000, 'Galaxy F62': 29000}
        one_pr = {'Oneplus7': 42000, 'Oneplus 7T': 48000, 'Onepuls 8': 54000, 'Oneplus Nord': 29000}
        xiaomi_pr = {'Redmi Note 7': 21000, 'Redmi Note 10': 28000}
        Realme_pr = {'Realme 3': 14000, 'Ralme 7': 21000}

        print("Select Mobile Brands you want to see products in..")
        print("    1. Apple")
        print("    2. Samsung")
        print("    3. Oneplus")
        print("    4. xiaomi")
        print("    5. Realme")
        while end == 'N':
            mobbrand = int(input("Enter your choice"))
            selectmobbrand.append(Mob_Brand[mobbrand])
            end = input("End brand Selection?Y/N")
        print("Enter Price range ")
        uppermob = input("Upper range")
        lowermob = input("Lower range")
        for i in selectmobbrand:
            for model in locals()[i]:
                if i == 'Apple':
                    if Apple_pr[model] >= int(lowermob) and Apple_pr[model] <= int(uppermob):
                        k = k + 1
                        print(k, ". Apple ", model, "     ", "Rs. ", Apple_pr[model], "\n")
                elif i == 'Samsung':
                    if Sam_pr[model] >= int(lowermob) and Sam_pr[model] <= int(uppermob):
                        k = k + 1
                        print(k, ". Samsung ", model, "     ", "Rs. ", Sam_pr[model], "\n")
                elif i == 'Oneplus':
                    if one_pr[model] >= int(lowermob) and one_pr[model] <= int(uppermob):
                        k = k + 1
                        print(k, ". Oneplus ", model, "     ", "Rs. ", one_pr[model], "\n")
                elif i == 'xiaomi':
                    if xiaomi_pr[model] >= int(lowermob) and xiaomi_pr[model] <= int(uppermob):
                        k = k + 1
                        print(k, ". Xiaomi ", model, "     ", "Rs. ", xiaomi_pr[model], "\n")
                elif i == 'Realme':
                    if Realme_pr[model] >= int(lowermob) and Realme_pr[model] <= int(uppermob):
                        k = k + 1
                        print(k, ". Realme ", model, "     ", "Rs. ", Realme_pr[model], "\n")
                    else:
                        continue
        if k == 0:
            print("No choices")
            run.runner()

        print("Enter your Selected final Brand")
        print("    1. Apple")
        print("    2. Samsung")
        print("    3. Oneplus")
        print("    4. Xiaomi")
        print("    5. Realme")
        bdChoice = int(input("Enter your choice as written above.Brand Number"))
        if bdChoice == 1:
            print("Enter your Selected final Model")
            print("    1. iphone 12 max pro")
            print("    2. iphone 11 pro max")
            print("    3. iphone XR")
            print("    4. iphone SE")
            mdchoice = int(input("Enter your choice as written above  .Model Number"))
            csquant = int(input("Enter Quantity"))
            if Apple_quant[Apple[mdchoice - 1]] < csquant or Apple_quant[Apple[mdchoice - 1]] == 0:
                print("Stock not available")
            else:
                Apple_quant[Apple[mdchoice - 1]] = Apple_quant[Apple[mdchoice - 1]] - csquant
                bill = csquant * (Apple_pr[Apple[mdchoice - 1]])
        elif bdChoice == 2:
            print("Enter your Selected final Model")
            print("    1. Galaxy Note 10")
            print("    2. Galaxy Duos")
            print("    3. Galaxy F62")
            mdchoice = int(input("Enter your choice as written above  .Model Number"))
            csquant = int(input("Enter Quantity"))
            if Samsung_quant[Samsung[mdchoice - 1]] < csquant or Samsung_quant[Samsung[mdchoice - 1]] == 0:
                print("Adicuite Stock not available")
            else:
                Samsung_quant[Samsung[mdchoice - 1]] = Samsung_quant[Samsung[mdchoice - 1]] - csquant
            bill =  csquant * (Sam_pr[Samsung[mdchoice - 1]])
        elif bdChoice == 3:
            print("Enter your Selected final Model")
            print("    1. Oneplus7")
            print("    2. Oneplus 7T")
            print("    3. Onepuls 8")
            print("    4. Oneplus Nord")
            mdchoice = int(input("Enter your choice as written above  .Model Number"))
            csquant = int(input("Enter Quantity"))
            if Oneplus_quant[Oneplus[mdchoice - 1]] < csquant or Oneplus_quant[Oneplus[mdchoice - 1]] == 0:
                print("Adicuite Stock not available")
            else:
                Oneplus_quant[Oneplus[mdchoice - 1]] = Oneplus_quant[Oneplus[mdchoice - 1]] - csquant
            bill =  csquant * (one_pr[Oneplus[mdchoice - 1]])
        elif bdChoice == 4:
            print("Enter your Selected final Model")
            print("    1. Redmi Note 7")
            print("    2. Redmi Note 10")
            mdchoice = int(input("Enter your choice as written above  .Model Number"))
            csquant = int(input("Enter Quantity"))
            if xiaomi_quant[xiaomi[mdchoice - 1]] < csquant or xiaomi_quant[xiaomi[mdchoice - 1]] == 0:
                print("Adicuite Stock not available")
            else:
                xiaomi_quant[xiaomi[mdchoice - 1]] = xiaomi_quant[xiaomi[mdchoice - 1]] - csquant
            bill =  csquant * (xiaomi_pr[xiaomi[mdchoice - 1]])
        elif bdChoice == 5:
            print("Enter your Selected final Model")
            print("    1. Realme 3")
            print("    2. Realme 7")
            mdchoice = int(input("Enter your choice as written above  .Model Number"))
            csquant = int(input("Enter Quantity"))
            if Realme_quant[Realme[mdchoice - 1]] < csquant or Realme_quant[Realme[mdchoice - 1]] == 0:
                print("Adicuite Stock not available")
            else:
                Realme_quant[Realme[mdchoice - 1]] = Realme_quant[Realme[mdchoice - 1]] - csquant
            bill =  csquant * (Realme_pr[Realme[mdchoice - 1]])
        else:
            print("Wrong choice")


        return bill, Mob_Brand[bdChoice], All_Mob[Mob_Brand[bdChoice]][mdchoice],csquant


class TVs:


    def TVs(self):
        selecttvbrand=[]
        end='N'
        k=0
        csquant=0
        bill=0
        mdchoice=0
        LG = ('Model L1', 'Model L2', 'Model L3')
        Sony = ('Model So1', 'Model So2', 'Model So3')
        Samsung = ('Model Sa1', 'Model Sa2', 'Model Sa3')
        All_TV = {'LG': {1: 'Model L1', 2: 'Model L2', 3: 'Model L3'},
                  'Sony': {1: 'Model So1', 2: 'Model So2', 3: 'Model So3'},
                  'Samsung': {1: 'Model Sa1', 2: 'Model Sa2', 3: 'Model Sa3'}}
        TV_Brand = {1: 'LG', 2: 'Sony', 3: 'Samsung'}
        LG_quant = {'Model L1': 10, 'Model L2': 10, 'Model L3': 10}
        Sony_quant = {'Model So1': 10, 'Model So2': 10, 'Model So3': 10}
        Sam_quant = {'Model Sa1': 10, 'Model Sa2': 10, 'Model Sa3': 10}

        LG_pr = {'Model L1': 150000, 'Model L2': 117100, 'Model L3': 48000}
        Sony_pr = {'Model So1': 42000, 'Model So2': 48000, 'Model So3': 54000}
        Sam_pr = {'Model Sa1': 117000, 'Model Sa2': 9000, 'Model Sa3': 29000}

        print("Select Mobile Brands you want to see products in..")
        print("    1. LG")
        print("    2. Sony")
        print("    3. Samsung")
        while end == 'N':
            tvbrand = int(input("Enter your choice"))
            selecttvbrand.append(TV_Brand[tvbrand])
            end = input("End brand Selection?Y/N")
        print("Enter Price range ")
        uppermob = input("Upper range")
        lowermob = input("Lower range")
        for i in selecttvbrand:
            for model in locals()[i]:
                if i == 'LG':
                    if LG_pr[model] >= int(lowermob) and LG_pr[model] <= int(uppermob):
                        k = k + 1
                        print(k, ". LG ", model, "     ", "Rs. ", LG_pr[model], "\n")
                elif i == 'Sony':
                    if Sony_pr[model] >= int(lowermob) and Sony_pr[model] <= int(uppermob):
                        k = k + 1
                        print(k, ". Sony ", model, "     ", "Rs. ", Sony_pr[model], "\n")
                elif i == 'Samsung':
                    if Sam_pr[model] >= int(lowermob) and Sam_pr[model] <= int(uppermob):
                        k = k + 1
                        print(k, ". Samsung ", model, "     ", "Rs. ", Sam_pr[model], "\n")
                    else:
                        continue
        if k == 0:
            print("No choices")
            run.runner()

        print("Enter your Selected final Brand")
        print("    1. LG")
        print("    2. Sony")
        print("    3. Samsung")

        bdChoice = int(input("Enter your choice as written above.Brand Number"))
        if bdChoice == 1:
            print("Enter your Selected final Model")
            print("    1. Model L1")
            print("    2. Model L2")
            print("    3. Model L3")

            mdchoice = int(input("Enter your choice as written above  .Model Number"))
            csquant = int(input("Enter Quantity"))
            if LG_quant[LG[mdchoice - 1]] < csquant or LG_quant[LG[mdchoice - 1]] == 0:
                print("Stock not available")
            else:
                LG_quant[LG[mdchoice - 1]] = LG_quant[LG[mdchoice - 1]] - csquant
                bill = csquant * (LG_pr[LG[mdchoice - 1]])
        elif bdChoice == 2:
            print("Enter your Selected final Model")
            print("    1. Model So1")
            print("    2. Model So2")
            print("    3. Model So3")
            mdchoice = int(input("Enter your choice as written above  .Model Number"))
            csquant = int(input("Enter Quantity"))
            if Sony_quant[Sony[mdchoice - 1]] < csquant or Sony_quant[Sony[mdchoice - 1]] == 0:
                print("Adicuite Stock not available")
            else:
                Sony_quant[Sony[mdchoice - 1]] = Sony_quant[Sony[mdchoice - 1]] - csquant
            bill = csquant * (Sony_pr[Sony[mdchoice - 1]])
        elif bdChoice == 3:
            print("Enter your Selected final Model")
            print("    1. Model Sa1")
            print("    2. Model Sa2")
            print("    3. Model Sa3")
            mdchoice = int(input("Enter your choice as written above  .Model Number"))
            csquant = int(input("Enter Quantity"))
            if Sam_quant[Samsung[mdchoice - 1]] < csquant or Sam_quant[Samsung[mdchoice - 1]] == 0:
                print("Adicuite Stock not available")
            else:
                Sam_quant[Samsung[mdchoice - 1]] = Sam_quant[Samsung[mdchoice - 1]] - csquant
            bill = csquant * (Sam_pr[Samsung[mdchoice - 1]])

        else:
            print("Wrong choice")


        return bill, TV_Brand[bdChoice], All_TV[TV_Brand[bdChoice]][mdchoice], csquant

class Billing:
    def __init__(self,uID,Brand,Model,quantity):
        self.uID=uID

        self.Brand=Brand
        self.Model=Model
        self.quantity=quantity

    def total_bill(self,uID, bill, Brand, Model,quantity):
        total = bill

        print('~~~~~~~Voice Memo~~~~~~')
        print("Customer name:",uID)
        print("Item:  ", Brand, Model)
        print("Quantity  :  ", quantity)
        print("Price  :  Rs.", bill)
        print("Total :  Rs.", total)
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        query=insert into Sales(id,name,Product Brand,Product Model,Total,Quantity) values(%s,%s,%s,%s,%s,%s)
        val=(1,uID,Brand,Model,bill,quantity)
        my_cursor.execute(query,val)
        my_db.commit()
        








class cancell:
    def cancell(self,d):

        Apple_quant = {'iphone 12 max pro': 10, 'iphone 11 pro max': 10, 'iphone XR': 10, 'iphone SE': 10}
        Samsung_quant = {'Galaxy Note 10': 10, 'Galaxy Duos': 10, 'Galaxy F62': 10}
        Realme_quant = {'Realme 3': 10, 'Ralme 7': 10}
        Oneplus_quant = {'Oneplus7': 10, 'Oneplus 7T': 10, 'Onepuls 8': 10, 'Oneplus Nord': 10}
        xiaomi_quant = {'Redmi Note 7': 10, 'Redmi Note 10': 10}
        LG_quant = {'Model L1': 10, 'Model L2': 10, 'Model L3': 10}
        Sony_quant = {'Model So1': 10, 'Model So2': 10, 'Model So3': 10}
        Sam_quant = {'Model Sa1': 10, 'Model Sa2': 10, 'Model Sa3': 10}
        HP_quant = {'Model H1': 10, 'Model H2': 10, 'Model H3': 10}
        Dell_quant = {'Model D1': 10, 'Model D2': 10, 'Model D3': 10}
        Leno_quant = {'Model L1': 10, 'Model L2': 10, 'Model L3': 10}
        brand_to_quant={'Apple':'Apple_quant','Samsung':'Samsung_quant','Realme':'Realme_quant','xiaomi':'xiaomi_quant','HP':'HP_quant','Dell':'Dell_quant','Lenovo':'Leno_quant','LG':'LG_quant','Sam':'Sam_quant','Sony':'Sony_quant'}


        uID=input("Enter User name")
        if uID in Sales.name :
                 g=my_cursor.execute('select Sales.product Brand where name=uID')
                 h=my_cursor.execute('select Sales.product Model where name=uID')
                 i=my_cursor.execute('select Sales.Quantity where name=uID')
                 j=my_cursor.execute('select Sales.Total where name=uID')
                print("~~~~~~~~~~~~~~~~~~~~Your Order~~~~~~~~~~~~~~~~~~~~~")
                print("Prodact name           ", g,h )
                print("Quantity               ", i)
                print("Refund bill        Rs. ", j)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                canin = input("DO YOU REALLY WANT TO CANCEL THE BOOKING?Y/N")
                if (canin == 'Y'):
                    genotp = (random.randint(1000, 9999))
                    nonchane = genotp
                    print(nonchane)
                    cusotp = input("Enter OTP:")
                    if int(cusotp) == nonchane:

                        a=eval(brand_to_quant[g]).get(h)
                        a+=eval(brand_to_quant[i]).get(h)+i

                        my_cursor.execute('delete from Sales where name=uID')
                        print("#######Cancellation Confirmed########")
                else:
                    run.runner()
        else:
                print("No such customer available")

class Laptops:

    def laptops(self):
        end='N'
        k=0
        selectLpbrand=[]
        mdchoice=0
        bill=0
        csquant=0
        HP = ('Model H1', 'Model H2', 'Model H3')
        Dell = ('Model D1', 'Model D2', 'Model D3')
        Lenovo = ('Model L1', 'Model L2', 'Model L3')
        All_LP = {'HP': {1: 'Model H1', 2: 'Model H2', 3: 'Model H3'},
                  'Dell': {1: 'Model D1', 2: 'Model D2', 3: 'Model D3'},
                  'Lenovo': {1: 'Model L1', 2: 'Model L2', 3: 'Model L3'}}
        LP_Brand = {1: 'HP', 2: 'Dell', 3: 'Lenovo'}
        HP_quant = {'Model H1': 10, 'Model H2': 10, 'Model H3': 10}
        Dell_quant = {'Model D1': 10, 'Model D2': 10, 'Model D3': 10}
        Leno_quant = {'Model L1': 10, 'Model L2': 10, 'Model L3': 10}

        HP_pr = {'Model H1': 150000, 'Model H2': 117100, 'Model H3': 48000}
        Dell_pr = {'Model D1': 42000, 'Model D2': 48000, 'Model D3': 54000}
        Leno_pr = {'Model L1': 117000, 'Model L2': 9000, 'Model L3': 29000}

        print("Select Mobile Brands you want to see products in..")
        print("    1. HP")
        print("    2. Dell")
        print("    3. Lenovo")

        while end == 'N':
            LPbrand = int(input("Enter your choice"))
            selectLpbrand.append(LP_Brand[LPbrand])
            end = input("End brand Selection?Y/N")
        print("Enter Price range ")
        uppermob = input("Upper range")
        lowermob = input("Lower range")
        for i in selectLpbrand:
            for model in locals()[i]:
                if i == 'HP':
                    if HP_pr[model] >= int(lowermob) and HP_pr[model] <= int(uppermob):
                        k = k + 1
                        print(k, ". HP ", model, "     ", "Rs. ", HP_pr[model], "\n")
                elif i == 'Dell':
                    if Dell_pr[model] >= int(lowermob) and Dell_pr[model] <= int(uppermob):
                        k = k + 1
                        print(k, ". Delll ", model, "     ", "Rs. ", Dell_pr[model], "\n")
                elif i == 'Lenovo':
                    if Leno_pr[model] >= int(lowermob) and Leno_pr[model] <= int(uppermob):
                        k = k + 1
                        print(k, ". Lenovo ", model, "     ", "Rs. ", Leno_pr[model], "\n")
                    else:
                        continue
        if k == 0:
            print("No choices")
            run.runner()

        print("Enter your Selected final Brand")
        print("    1. HP")
        print("    2. Dell")
        print("    3. Lenovo")

        bdChoice = int(input("Enter your choice as written above.Brand Number"))
        if bdChoice == 1:
            print("Enter your Selected final Model")
            print("    1. Model H1")
            print("    2. Model H2")
            print("    3. Model H3")

            mdchoice = int(input("Enter your choice as written above  .Model Number"))
            csquant = int(input("Enter Quantity"))
            if HP_quant[HP[mdchoice - 1]] < csquant or HP_quant[HP[mdchoice - 1]] == 0:
                print("Stock not available")
            else:
                HP_quant[HP[mdchoice - 1]] = HP_quant[HP[mdchoice - 1]] - csquant
                bill = csquant * (HP_pr[HP[mdchoice - 1]])
        elif bdChoice == 2:
            print("Enter your Selected final Model")
            print("    1. Model D1")
            print("    2. Model D2")
            print("    3. Model D3")
            mdchoice = int(input("Enter your choice as written above  .Model Number"))
            csquant = int(input("Enter Quantity"))
            if Dell_quant[Dell[mdchoice - 1]] < csquant or Dell_quant[Dell[mdchoice - 1]] == 0:
                print("Adicuite Stock not available")
            else:
                Dell_quant[Dell[mdchoice - 1]] = Dell_quant[Dell[mdchoice - 1]] - csquant
            bill =  csquant * (Dell_pr[Dell[mdchoice - 1]])
        elif bdChoice == 3:
            print("Enter your Selected final Model")
            print("    1. Model L1")
            print("    2. Model L2")
            print("    3. Model L3")
            mdchoice = int(input("Enter your choice as written above  .Model Number"))
            csquant = int(input("Enter Quantity"))
            if Leno_quant[Lenovo[mdchoice - 1]] < csquant or Leno_quant[Lenovo[mdchoice - 1]] == 0:
                print("Adicuite Stock not available")
            else:
                Leno_quant[Lenovo[mdchoice - 1]] = Leno_quant[Lenovo[mdchoice - 1]] - csquant
            bill = csquant * (Leno_pr[Lenovo[mdchoice - 1]])

        else:
            print("Wrong choice")
            #d.update({uID: {'Product Brand': LP_Brand[bdChoice], 'Product Model': All_LP[LP_Brand[bdChoice]][mdchoice], 'Total': bill, 'Quantity': csquant}})

        return bill, LP_Brand[bdChoice], All_LP[LP_Brand[bdChoice]][mdchoice], csquant

class Store(Start,Gadgets,Mobiles,Billing,TVs,Laptops,ops,cancell):
    def runner(self):


        uID=""
        obj=super().start()

        if obj == 'B':
            uID = input("Enter Your UserName")
            Users.append(uID)
            seg_no=super().info()
            if seg_no == 1:
                bill,Brand,Model,quantity=super().Mobiles()
                d[uID]= {'Product Brand': Brand,'Product Model': Model, 'Total': bill,'Quantity': quantity}
                super().total_bill(uID,bill,Brand,Model,quantity)
                obj=super().ops()


            elif seg_no==2:
                bill,Brand,Model,quantity=super().TVs()
                d[uID]= {'Product Brand': Brand,'Product Model': Model, 'Total': bill,'Quantity': quantity}
                super().total_bill(uID,bill, Brand, Model, quantity)
                obj = super().ops()

            elif seg_no==3:
                bill,Brand,Model,quantity=super().laptops()
                d[uID] = {'Product Brand': Brand,'Product Model': Model, 'Total': bill,'Quantity': quantity}
                super().total_bill(,uIDbill, Brand, Model, quantity)
                obj = super().ops()

        elif obj == 'C':
                super().cancell(d)
        return uID,Users




d={}
Users=[]
run=Store()
run.runner()






