import os,datetime,random,time

# INTRO OF COMPANY
#pk=os.chdir("E:\class 12 project PIYUSH KUMAR")
f=open("welcome.txt",'r')
p=f.read()
print(p)
f.close()

cos_car_menu=0

#STAFF MENU
#--------------------------------------------------------------------------------------------------------------
def main_menu():
    print("="*134)
    print(" "*43,"  ________________________________________________  ")
    print(" "*43," /\______________________________________________/\ ")
    print(" "*43," \/______________________________________________\/ ")
    print(" "*43," /\|SR.NO.|           MAIN INTERFACE            |/\ ")
    print(" "*43," \/|______|_____________________________________|\/ ")
    print(" "*43," /\|   1. | PRESS 1 IF YOU ARE CUSTOMER         |/\ ")
    print(" "*43," \/|   2. | PRESS 2 IF YOU ARE STAFF MEMBER     |\/ ")
    print(" "*43," /\|   3. | EXIT                                |/\ ")
    print(" "*43," \/|______|_____________________________________|\/ ")
    print(" "*43,"  \/____________________________________________\/ ","\n")
    print("="*134)

# STAFF MENU
#---------------------------------------------------------------------------------------------------------------
def staff_menu():
    print("="*134)
    print(" "*43,"   ________________________________________________   ")
    print(" "*43,"  /\______________________________________________/\  ")
    print(" "*43," /\/______________________________________________\/\ ")
    print(" "*43," \/\|SR.NO.|   MAIN INTERFACE FOR STAFF MEMEBER  |/\/ ")
    print(" "*43," /\/|______|_____________________________________|\/\ ")
    print(" "*43," \/\|   1. | VIEW ALL CARS AVALIABLE IN SHOWROOM |/\/ ")
    print(" "*43," /\/|   2. | SEARCH SPECIFIC CAR BY MODEL NAME   |\/\ ")
    print(" "*43," \/\|   3. | IMPORTING NEW CARS TO SHOWROOM      |/\/ ")
    print(" "*43," /\/|   4. | UPDATE ANY EXISTING CAR INFORMATION |\/\ ")
    print(" "*43," \/\|   5. | LIST OF ALL SELLED CAR              |/\/ ")
    print(" "*43," \/\|   6. | EXIT                                |/\/ ")
    print(" "*43,"  \/|______|_____________________________________|\/  ")
    print(" "*43,"   \/____________________________________________\/   ","\n")
    print("="*134,"\n")


# CREATING MAIN MENU
#------------------------------------------------------------------------------------------------------------
def customer_menu():
    print("="*134)
    print(" "*43,"   ________________________________________________   ")
    print(" "*43,"  /\______________________________________________/\  ")
    print(" "*43," /\/ ____________________________________________ \/\ ")
    print(" "*43," \/\|SR.NO.|     MAIN INTERFACE FOR CUSTOMER     |/\/ ")
    print(" "*43," /\/|______|_____________________________________|\/\ ")
    print(" "*43," \/\|   1. | VIEW ALL CARS AVALIABLE IN SHOWROOM |/\/ ")
    print(" "*43," /\/|   2. | SEARCH SPECIFIC CAR                 |\/\ ")
    print(" "*43," \/\|   3. | BUY A CAR                           |/\/ ")
    print(" "*43," \/\|   4. | EXIT                                |/\/ ")
    print(" "*43,"  \/|______|_____________________________________|\/  ")
    print(" "*43,"   \/____________________________________________\/   ","\n")
    print("="*134)
    
#------------------------------------------------------------------------------------------------------------
# FUNCTIONS OF THE MANAGEMENT SYSTEMS

#VIEW CAR RECORDS
def car_1():
    with open("car_managment.txt","r") as car:
        d=car.readlines()     
        if len(d)!=0:
            print()
            print("+------------------------------+")
            print("| DATA IS LOADING FROM RECORDS |")
            print("+------------------------------+")
            print()
            t=0.14
            ij=random.random()
            time.sleep(0.8)
            for i in range(133):
                print("█",end="")
                time.sleep(t)
                if i==7:
                    t=3*ij
                elif i==8:
                    t=0
                elif i==80:
                    t=0.9
                elif i>=80:
                    t=0
            print("█")
            print()
            if cos_car_menu==0:
                print(" "*3,"+----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+")
                print(" "*3,"|  COMPANY NAME  |   MODEL NAME    |    MODEL NO.    | MANUFATURE YEAR |    PRICE (₹)    |   SEATER TYPE   |  DATE OF ADDING |")
                print(" "*3,"+----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+")
                print(" "*3,"|",end="")
                for m in d:
                    p=m.split()
                    for k in p:
                        print('%15s'% k,"|",end=" ")
                    print()
                    print(" "*3,"|",end='')

                print("----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------|","\n")
            elif cos_car_menu==1:
                print("   "*3,"+----------------+-----------------+-----------------+-----------------+-----------------+-----------------+")
                print("   "*3,"|  COMPANY NAME  |   MODEL NAME    |    MODEL NO.    | MANUFATURE YEAR |    PRICE (₹)    |   SEATER TYPE   |")
                print("   "*3,"+----------------+-----------------+-----------------+-----------------+-----------------+-----------------+")
                print("   "*3,"|",end="")
                for m in d:
                    p=m.split()
                    for k in p:
                        if p[-1]!=k:
                            print('%15s'% k,"|",end=" ")
                    print()
                    print("   "*3,"|",end='')

                print("----------------+-----------------+-----------------+-----------------+-----------------+-----------------|","\n")
        else:
            print()
            print(">"*10,"RECORD IS EMPTY","<"*10,"\n")
    h=input(" "*43+">>>>>>>>>>PRESS ENTER TO CONTINUE<<<<<<<<<<")
    while True:
        if len(h)!=0:
            h=input(" "*43+">>>>>>>>>>PRESS ENTER TO CONTINUE<<<<<<<<<<")
        else:
            break
    print()
        
#------------------------------------------------------------------------------------------------------------

#SEARCH CAR RECORDS
def car_2():
        a=open("car_managment.txt","r")
        flag=0
        search=input("ENTER CAR MODEL NAME    :-->")
        while True:
            if len(search)==0:
                print("THIS IS A REQUIRED FIELD!!!\n")
                mod=input("ENTER MODEL NO.         :-->")
            else:
                break
        mod=input("ENTER MODEL NO.         :-->")
        while True:
            if len(mod)==0:
                print("MODEL NO. CANNOT BE EMPTY!!!\n")
                mod=input("ENTER MODEL NO.         :-->")
            elif len(mod)!=5:
                print("PLEASE ENTER ONLY 5 DIGITS MODEL NO.!!!\n")
                mod=input("ENTER MODEL NO.         :-->")
            else:
                break
        while True:
            d=a.readline()
            if len(d)==0:
                break
            g=d.split()
            if g[1]==search.upper() and g[2]==mod:
                print()
                print("+------------------------------+")
                print("| DATA IS LOADING FROM RECORDS |")
                print("+------------------------------+")
                print()
                for i in range(133):
                    print("█",end="")
                print("█")
                print()
                print(" "*45,"+-----------------------------------------------+")
                print(" "*45,"| CAR MODEL NUMBER IS          :-->",'%10s'%g[2], " |")
                print(" "*45,"| CAR NAME IS                  :-->",'%10s'%g[1]," |")
                print(" "*45,"| CAR COMPANY NAME IS          :-->",'%10s'%g[0], " |")
                print(" "*45,"| CAR MANUFATURING YEAR IS     :-->",'%10s'%g[3], " |")
                print(" "*45,"| CAR PRICE IS                 :-->","₹",'%8s'%g[4], " |")
                print(" "*45,"| CAR SEATER TYPE IS           :-->",g[5],'%8s'%"SEATER", " |")
                print(" "*45,"+-----------------------------------------------+\n")
                print()
                flag=1
                break
        a.close()    
        if flag==0:
            print()
            print(">"*10,"RECORD NOT FOUND OR RECORD IS EMPTY","<"*10,"\n")
        h=input(" "*48+">>>>>>>>>>PRESS ENTER TO CONTINUE<<<<<<<<<<")
        while True:
            if len(h)!=0:
                h=input(" "*48+">>>>>>>>>>PRESS ENTER TO CONTINUE<<<<<<<<<<")
            else:
                break
        print()
        
#------------------------------------------------------------------------------------------------------------

# ADD CARS TO SHOWROOM
def car_3():
    cr_com =input("ENTER CAR COMPANY NAME        :-->")
    while True:
        if len(cr_com)==0:
            print()
            print(">"*10,"PLEASE ENTER CAR COMPANY NAME","<"*10,"\n")
            cr_com =input("ENTER CAR COMPANY NAME        :-->")
        else:
            break
        
    cr_name=input("ENTER CAR MODEL NAME          :-->")
    while True:
        if len(cr_name)==0:
            print()
            print(">"*10,"PLEASE ENTER CAR MODEL NAME","<"*10,"\n")
            cr_name=input("ENTER CAR MODEL NAME          :-->")
        else:
            break

    lst=[]    
    mod_no =input("ENTER CAR MODEL NO.           :-->")
    k=open("car_managment.txt",'r')
    while True:
        d=k.readline()
        if len(d)==0:
            break
        g=d.split()
        lst.append(g[2])
    while True:
        if mod_no in lst:
            print()
            print(">"*10,"CAR HAVING THIS MODEL NO. IS ALREADY EXISTS","<"*10,"\n")
            mod_no=input("PLEASE ENTER CAR\'s UNIQUE MODEL NO. :-->")
        if len(mod_no)!=5 :
            print()
            print(">"*10,"PLEASE ENTER 5 DIGIT MODEL NO.","<"*10,"\n")
            mod_no=input("ENTER CAR MODEL NO.           :-->")
        else:
            break
    k.close()
    
    cr_man =(input("ENTER CAR MANUFACTURING YEAR:-->"))
    while True:
        if not cr_man.isdigit():
            print()
            print("PLEASE ENTER A VALID YEAR OF MANUFACTURE!!!\n")
            cr_man =input("ENTER CAR MANUFACTURING YEAR:-->")
        else:
            break
    while True:
        if ((int(cr_man)>2022) or (int(cr_man)<1886)):
            print("PLEASE ENTER A VALID YEAR OF MANUFACTURE!!!\n")
            cr_man =(input("ENTER CAR MANUFACTURING YEAR:-->"))
        else:
            break

    cr_pr =input("ENTER PRICE OF THE CAR        :-->")
    while True:
        if len(cr_pr)<7 or len(cr_pr)>10:
            print()
            print(">"*10,"PLEASE ENTER VALID CAR PRICE","<"*10,"\n")
            cr_pr =input("ENTER PRICE OF THE CAR        :-->")
        if not cr_pr.isdigit():
            print()
            print(">"*10,"PLEASE ENTER ONLY NUMBERS","<"*10,"\n")
            cr_pr =input("ENTER PRICE OF THE CAR        :-->")
        else:
            break
    cr_st=int(input("ENTER NO. OF SEATS OF THE CAR (2 \ 5 \ 7):-->"))
    
    while True:
        if cr_st !=2 and cr_st !=5 and cr_st !=7:
            print()
            print(">"*10,"PLEASE ENTER FROM ABOVE OPTINS","<"*10,"\n")
            cr_st=int(input("ENTER NO. OF SEATS OF THE CAR (2 \ 5 \ 7):-->"))
        else:
            break
    add_ch=input(r"DO YOU WANT TO IMPORT THIS CAR TO SHOWROOM (Y\N):-->")
    while True:
        if add_ch.isdigit():
            print()
            print(">"*10,r"PLEASE ENTER ONLY CHOICE (Y\N)","<"*10,"\n")
            add_ch=input(r"DO YOU WANT TO IMPORT THIS CAR TO SHOWROOM (Y\N):-->")
        elif add_ch.lower()=="y" or add_ch.lower()=="yes":
            add=1
            break
        elif add_ch.lower()=="n" or add_ch.lower()=="no":
            add=0
            break
        else:
            print()
            print(">"*10,r"PLEASE ENTER ONLY CHOICE (Y\N)","<"*10,"\n")
            add_ch=input(r"DO YOU WANT TO IMPORT THIS CAR TO SHOWROOM (Y\N):-->")
    dt=datetime.datetime.now()
    dte=dt.date()
    f=0
    with open("car_managment.txt",'a') as a:
        if add==1:
            a.write(cr_com.upper()+"  "+cr_name.upper()+"  "+mod_no+"  "+str(cr_man)+"  "+str(cr_pr)+"  "+str(cr_st)+"  "+str(dte)+"\n")
            f=1
    if f==1:
        print()
        print(">"*10,"CAR WILL BE IMPORTING TO SHOWROOM AS SOON AS POSSIBLE ","<"*10)
    if f==0:
        print()
        print(">"*10,"CAR WILL NOT IMPORTING TO SHOWROOM","<"*10,"\n")
#------------------------------------------------------------------------------------------------------------

#TO PURCHASE CARS  FOR CUSTOMERS   
def car_4():
    while True:
        srch=input("ENTER NAME OF THE CAR TO BE PURCHASE  :-->")
        if len(srch)!=0:
            break
        else:
            print()
            print(">"*10,"PLEASE ENTER NAME OF THE CAR TO BE PURCHASE","<"*10,"\n")
    modn=input("ENTER MODEL NO. OF CAR             :-->")
    while True:
        if len(modn)!=0 or len(modn)==5:
            if modn.isdigit():
                break
            else:
                print()
                print(">"*10,"PLEASE ENTER ONLY DIGITS FOR MODEL NO.","<"*10,"\n")   
        else:
            print()
            print(">"*10,"PLEASE ENTER VALID MODEL NUMBER","<"*10,"\n")

    w=open("car_managment.txt",'r')
    tt=open("temp.txt","w")
    h=0
    df=0
    while True:
        dat=w.readline()
        #print(d)
        if len(dat)==0:
            break
        g=dat.split()
        if g[1]!=srch.upper() or g[2]!=modn:
            tt.write(dat)
        elif (g[1]==srch.upper() and g[2]==modn):
            print()
            print(">"*10,"CAR CREDENTIALS ARE MATCH WITH YOUR ENTERED DETAILS","<"*10,"\n")
            print("CAR MODEL NUMBER IS          :-->",'%10s'%g[2])
            print("CAR NAME IS                  :-->",'%10s'%g[1])
            print("CAR COMPANY NAME IS          :-->",'%10s'%g[0])
            print("CAR SEATER TYPE IS           :-->",'%3s'%g[5],"SEATER")
            print("CAR PRICE IS                 :-->","%10s"%g[4])
            print("--------------------------------------------\n")
            d=input(r"DO YOU REALLY WANT TO PURCHASE THIS CAR (Y\N) :-->")
            while True:
                if d=="y" or d=="yes" or d=="Y" or d=="YES":
                    h=1
                    print("---------------------------------------------------")
                    print(">"*10,"ENTER YOUR DETAILS TO CONTINUE","<"*10)
                    while True:
                        renter_name = input("ENTER YOUR NAME       :-->")
                        if len(renter_name)!=0:
                            break
                        else:
                            print()
                            print(">"*10,"PLEASE ENTER YOUR NAME","<"*10)
                        print()
                    while True:
                        renter_age = input("ENTER YOUR AGE       :-->")
                        if len(renter_age)!=0:
                            if renter_age.isnumeric():
                                break
                            else:
                                print()
                                print(">"*10,"PLEASE ENTER ONLY NUMBERS FOR AGE","<"*10)
                        else:
                            print()
                            print(">"*10,"PLEASE ENTER YOUR AGE","<"*10)
                            print()
                    while True:
                        renter_gen = input("ENTER YOUR GENDER       :-->")
                        if len(renter_gen)!=0:
                            if renter_gen.isalpha():
                                if renter_gen=="m" or renter_gen=="M" or renter_gen=="MALE" or  renter_gen=="male" or renter_gen=="FEMALE" or renter_gen=="female" or renter_gen=="F" or renter_gen=="f": 
                                    break
                                else:
                                    print()
                                    print(">"*10,"PLEASE ENTER M OR F FOR GENDER","<"*10)
                            else:
                                print()
                                print(">"*10,"PLEASE ENTER  M OR F FOR GENDER","<"*10)
                        else:
                            print()
                            print(">"*10,"PLEASE ENTER YOUR AGE","<"*10)
                        print()
                    while True:
                        renter_mob = input("ENTER YOUR MOBILE NO. :-->")
                        if len(renter_mob)!=0:
                            if renter_mob.isnumeric():
                                if len(renter_mob)==10:
                                    break
                                else:
                                    print()
                                    print(">"*10,"PLEASE ENTER ONLY 10 DIGIT MOBILE NO. ","<"*10)
                            else:
                                print()
                                print(">"*10,"PLEASE ENTER ONLY DIGITS FOR MOBILE NO. ","<"*10)
                        else:
                            print()
                            print(">"*10,"PLEASE ENTER YOUR MOBILE NO. ","<"*10)
                        print()
                    break
                if len(d)==0:
                    print()
                    print(">"*10,"PLEASE ENTER CHOICE","<"*10,"\n")
                    modn=input("ENTER  MODEL  NO.                  :-->")
                if d=="N" or d=="NO" or d=="n" or d=="no":
                    df=1
                    break
                else:
                    print()
                    print(">"*10,"PLEASE ENTER VALID CHOICE","<"*10,"\n")
                    d=input(r"DO YOU REALLY WANT TO PURCHASE THIS CAR (Y\N) :-->")
            if os.path.isfile("selled_car.txt"):
                with open("selled_car.txt","a") as rent:
                    rent.write(dat+"  "+renter_name.upper()+"  "+str(renter_age)+"  "+renter_gen.upper()+"  "+str(renter_mob)+"\n")
            else:
                with open("selled_car.txt","w") as rent:
                    rent.write(dat+"  "+renter_name.upper()+"  "+str(renter_age)+"  "+renter_gen.upper()+"  "+str(renter_mob)+"\n")
    tt.close()
    w.close()
    if h==1:
        print()
        print(">"*10,"CAR PURCHASED SUCCESFULLY","<"*10)
        print()
        os.remove("car_managment.txt")
        os.rename("temp.txt","car_managment.txt")
    elif h==0 and df==0:
        print(">"*10,"CAR NOT FOUND","<"*10)
    print()

#------------------------------------------------------------------------------------------------------------        

# TO UPDATE RECORD OF CAR 
def car_5():
    src=input("ENTER NAME OF THE COMPANY WHOSE CAR IS TO BE UPDATED:-->")
    while True:
        if len(src)==0:
            print()
            print(">"*10,"PLEASE ENTER NAME OF THE COMPANY WHOSE CAR IS TO BE UPDATED","<"*10,"\n")
            src=input("ENTER NAME OF THE COMPANY WHOSE CAR IS TO BE UPDATED:-->")
        else:
            break
    k=open("car_managment.txt","r")
    t=open("temp.txt","w")
    h=0
    sp=0
    while True:
        d=k.readline()
        if len(d)==0:
            break
        g=d.split()
        if g[0]==src.upper():
            print("CURRENT CAR INFORMATION IS                    :-->","\n")
            print(" "*45,"+------------------------------------------------+")
            print(" "*45,"| CAR MODEL NUMBER IS          :-->",'%11s'%g[2], " |")
            print(" "*45,"| CAR NAME IS                  :-->",'%11s'%g[1]," |")
            print(" "*45,"| CAR COMPANY NAME IS          :-->",'%11s'%g[0], " |")
            print(" "*45,"| CAR MANUFATURING YEAR IS     :-->",'%11s'%g[3], " |")
            print(" "*45,"| CAR PRICE IS                 :-->","₹",'%9s'%g[4], " |")
            print(" "*45,"| CAR SEATER TYPE IS           :-->",'%4s'%g[5],"SEATER", " |")
            print(" "*45,"| DATE OF ADDING CAR TO RECORD :-->",'%11s'%g[6]," |")
            print(" "*45,"+------------------------------------------------+\n")
            p=input(r"DO YOU WANT TO UPDATE THIS CAR (Y\N):-->")
            print("---------------------------------------------\n")
            while True:
                if p=="y" or p=="Y" or p=="YES" or p=="yes":        
                    while True:
                        n=input(r"DO YOU WANT TO CHANGE CAR NAME (Y\N)          :-->")
                        if len(n)==0:
                            print()
                            print(">"*10,"PLEASE ENTER YOUR CHOICE HERE","<"*10,"\n")
                            n=input(r"DO YOU WANT TO CHANGE CAR NAME (Y\N)          :-->")
                        elif (n.upper()=="YES" or n.upper()=="Y"):
                            new_car=input("ENTER CAR\'S NEW NAME                         :-->")
                            break
                        elif (n.upper()=="N" or n.upper()=="NO"):
                            new_car=g[1]
                            break
                        else:
                            print()
                            print(">"*10,"ENTER  A VALID VALUE!!!","<"*10,"\n")

                    while True:
                        z=input(r"DO YOU WANT TO CHANGE MODEL NO. (Y\N)         :-->")
                        if len(z)==0:
                            print()
                            print(">"*10,"PLEASE ENTER YOUR CHOICE HERE","<"*10,"\n")
                            z=input(r"DO YOU WANT TO CHANGE MODEL NO. (Y\N)         :-->")                   
                        elif (z.upper()=="YES" or z.upper()=="Y"):
                            new_modn=input("ENTER NEW MODEL NO.                           :-->")
                            while True:
                                if  not new_modn.isdigit():
                                    print()
                                    print(">"*10,"PLEASE ENTER 5 DIGIT MODEL NO.","<"*10,"\n")
                                    new_modn=input("ENTER NEW MODEL NO.                           :-->")
                                else:
                                    break
                            break
                        elif (z.upper()=="N" or z.upper()=="NO"):
                            new_modn=g[2]
                            break
                        else:
                            print()
                            print(">"*10,"ENTER  A VALID VALUE!!!","<"*10,"\n")
                    
                    while True:    
                        o=input(r"DO YOU WANT TO CHANGE YEAR OF MANUFACTURE(Y\N):-->")
                        if o.upper()=="YES" or o.upper()=="Y":
                            new_date=input("ENTER NEW YEAR OF MANUFACTURE                 :-->")
                            while True:
                                if  not new_date.isdigit():
                                    print()
                                    print(">"*10,"PLEASE ENTER VALID YEAR","<"*10,"\n")
                                    new_date=input("ENTER NEW MODEL NO.                           :-->")
                                if len(o)==0:
                                    print()
                                    print(">"*10,"PLEASE ENTER YEAR OF MANUFACTURE","<"*10,"\n")
                                    new_date=input("ENTER NEW YEAR OF MANUFACTURE                 :-->")
                                else:
                                    break
                            while True:
                                if (int(new_date)>2022) or (int(new_date)<1886):
                                    print("PLEASE ENTER A VALID YEAR OF MANUFACTURE!!!\n")
                                    new_date=input("ENTER NEW YEAR OF MANUFACTURE                 :-->")
                                else:
                                    break
                                
                            break
                        elif (o.upper()=="N" or o.upper()=="NO"):
                            new_date=g[3]
                            break
                        else:
                            print()
                            print(">"*10,"ENTER  A VALID VALUE!!!","<"*10,"\n")   

                    while True:
                        i=input(r"DO YOU WANT TO CHANGE CAR PRICE (Y\N)         :-->")
                        if len(i)==0:
                            print()
                            print(">"*10,"PLEASE ENTER YOUR CHOICE HERE","<"*10,"\n")
                            i=input(r"DO YOU WANT TO CHANGE CAR PRICE (Y\N)         :-->")
                        elif i.upper()=="YES" or i.upper()=="Y":
                            np=input("ENTER NEW PRICE OF CAR (INR)                     :-->")
                            while True:
                                if len(np)<6 or len(np)>10:
                                    print()
                                    print(">"*10,"PLEASE ENTER VALID CAR PRICE","<"*10,"\n")
                                    np =input("ENTER PRICE OF THE CAR        :-->")
                                else:
                                    break
                            while True:
                                if not np.isdigit():
                                    print()
                                    print(">"*10,"PLEASE ENTER ONLY NUMBERS","<"*10,"\n")
                                    np =input("ENTER PRICE OF THE CAR        :-->")
                                else:
                                    break
                            break
                        elif (i.upper()=="N" or i.upper()=="NO"):
                            np=g[4]
                            break
                        else:
                            print(">"*10,"ENTER  A VALID VALUE!!!","<"*10,"\n")
                    
                    while True:
                        i=input(r"DO YOU WANT TO CHANGE CAR SEATER TYPE (Y\N)   :-->")
                        if len(i)==0:
                            print()
                            print(">"*10,"PLEASE ENTER YOUR CHOICE HERE","<"*10,"\n")
                            i=input(r"DO YOU WANT TO CHANGE CAR SEATER TYPE (Y\N)   :-->")
                        elif i.upper()=="YES" or i.upper()=="Y":
                            cr_st=(input("ENTER NO. OF SEATS OF THE CAR (2 \ 5 \ 7):-->"))
                            while True:
                                if not cr_st.isdigit():
                                    print()
                                    print(">"*10,"PLEASE ENTER ONLY NO. FOR SEATER TYPE","<"*10)
                                    cr_st=(input("ENTER NO. OF SEATS OF THE CAR (2 \ 5 \ 7):-->"))
                                else:
                                    break
                            while True:
                                if int(cr_st) !=2 and int(cr_st) !=5 and int(cr_st) !=7:
                                    print()
                                    print(">"*10,"PLEASE ENTER FROM ABOVE OPTINS","<"*10,"\n")
                                    cr_st= input("ENTER NO. OF SEATS OF THE CAR (2 \ 5 \ 7):-->")
                                else:
                                    break
                            break
                        elif (i.upper()=="N" or i.upper()=="NO"):
                            cr_st=g[5]
                            break
                        else:
                            print(">"*10,"ENTER  A VALID VALUE!!!","<"*10,"\n")
                            
                    while True:
                        b=input(r"DO YOU WANT TO CHANGE DATE OF ADDING (Y\N)    :-->")
                        if len(b)==0:
                            print()
                            print(">"*10,"PLEASE ENTER YOUR CHOICE HERE","<"*10,"\n")
                            b=input(r"DO YOU WANT TO CHANGE DATE OF ADDING (Y\N)    :-->")
                        elif b.upper()=="YES" or b.upper()=="Y":
                            new_dtj=input("ENTER NEW DATE OF ADDING IN [YYY-MM-DD] FORMAT:-->")
                            nk=new_dtj.split("-")
                            while True:
                                if len(nk)!=3:
                                    print()
                                    print(">"*10,"ENTER  A VALID DATE FORMAT","<"*10,"\n")
                                    new_dtj=input("ENTER NEW DATE OF ADDING IN [YYY-MM-DD] FORMAT:-->")
                                    nk=new_dtj.split("-")
                                if int(nk[0])>2022 or int(nk[0])<1886 or int(nk[1])>12 or int(nk[2])>31:
                                    print()
                                    print(">"*10,"ENTER  A VALID DATE","<"*10,"\n")
                                    new_dtj=input("ENTER NEW DATE OF ADDING IN [YYY-MM-DD] FORMAT:-->")
                                    nk=new_dtj.split("-")
                                else:
                                    break  
                            break
                        elif (b.upper()=="N" or b.upper()=="NO"):
                            new_dtj=g[6]
                            break
                        else:
                            print(">"*10,"ENTER  A VALID VALUE!!!","<"*10,"\n")        
                    t.write( src.upper()+"  " + new_car.upper()+"  " + new_modn+"  " + new_date +"  "+ str(np) +"  "+ str(cr_st)+"  " + str(new_dtj) +"\n" )
                    h=1
                    break
                elif p=="n" or p=="N" or p=="NO" or p=="no":
                    sp=1
                    break
                else:
                    print(">"*10,"ENTER  A VALID VALUE!!!","<"*10,"\n")
                    p=input(r"DO YOU WANT TO UPDATE THIS CAR (Y\N):-->")
                    print("---------------------------------------------\n")
        else:
            t.write(d)
    k.close()
    t.close()
    if h==1:
        print()
        print(">"*10,"CAR RECORD UPDATED SUCCESSFULLY","<"*10,"\n")

        os.remove("car_managment.txt")
        os.rename("temp.txt","car_managment.txt")
    else:
        if sp==0:
            print()
            print(">"*10,"NO SUCH CAR RECORD EXISTS!!!","<"*10,'\n')
    h=input(" "*43+">>>>>>>>>>PRESS ENTER TO CONTINUE<<<<<<<<<<")
    while True:
        if len(h)!=0:
            h=input(" "*43+">>>>>>>>>>PRESS ENTER TO CONTINUE<<<<<<<<<<")
        else:
            break
    print()       
#------------------------------------------------------------------------------------------------------------

def selled_cars():
    if not os.path.isfile("selled_car.txt"):
        aex=open("selled_car.txt","w")
        aex.close()
    with open("selled_car.txt","r") as sell:
        print()
        print("+------------------------------+")
        print("| DATA IS LOADING FROM RECORDS |")
        print("+------------------------------+")
        print()
        for i in range(133):
            print("█",end="")
        print("█")
        print()
        var=1
        while True:
            data=sell.readline()
            g_lst=data.split()
            if len(g_lst)==0:
                break
            
            for i in g_lst:
                print("%10s"%i,end="  ")
            if var%2==0:
                print()
            var+=1
            print()  


#-------------------------------------------------------------------------------------------------------------        
# MAIN FUNTIONING OF THE PROGRAM

while True :
    main_menu()
    while True:
        mn_ch =input("ENTER YOUR CHOICE       :-->")
        if len(mn_ch)!=0:
            if mn_ch.isdigit():
                break
            else:
                print()
                print(">"*10,"PLEASE ENTER ONLY NUMBERS","<"*10,"\n")
        else:
            print()
            print(">"*10,"PLEASE ENTER YOUR CHOICE","<"*10,"\n")
            
    if int(mn_ch)==1:
        while True:
            customer_menu()
            while True:
                cst_ch =input("ENTER YOUR CHOICE       :-->")
                if len(cst_ch)!=0:
                    if cst_ch.isdigit():
                        break
                    else:
                        print()
                        print(">"*10,"PLEASE ENTER ONLY NUMBERS","<"*10,"\n")
                else:
                    print()
                    print(">"*10,"PLEASE ENTER YOUR CHOICE","<"*10,"\n")    
            if int(cst_ch)==1:
                cos_car_menu=1
                car_1()
            elif int(cst_ch)==2:
                car_2()
            elif int(cst_ch)==3:
                car_4()
                while True:
                    print()
                    i=input("DO YOU WANT TO BUY MORE CARS (Y/N):-->")
                    if i.upper()=="YES" or i.upper()=="Y":
                        car_4()
                    elif (i.upper()=="N" or i.upper()=="NO"):
                        print()
                        gh=input(" "*43+">>>>>>>>>>PRESS ENTER TO CONTINUE<<<<<<<<<<")
                        print()
                        break
                    else:
                        print()
                        print(">"*10,"ENTER  A VALID VALUE!!!","<"*10,"\n")      
            elif int(cst_ch)==4:
                break
            else:
                print()
                print(">"*10,"ENTER YOUR CHOICE BETWEEN 1 AND 7","<"*10,"\n")


                
    elif int(mn_ch)==2:
        while True:
            staff_menu()
            while True:
                st_ch =input("ENTER YOUR CHOICE       :-->")
                if len(st_ch)!=0:
                    if st_ch.isdigit():
                        break
                    else:
                        print()
                        print(">"*10,"PLEASE ENTER ONLY NUMBERS","<"*10,"\n")
                else:
                    print()
                    print(">"*10,"PLEASE ENTER YOUR CHOICE","<"*10,"\n")
            if int(st_ch)==1:
                cos_car_menu=0
                car_1()
            elif int(st_ch)==2:
                car_2()
            elif int(st_ch)==3:
                car_3()
                while True:
                    print()
                    i=input("DO YOU WANT TO IMPORT MORE CARS (Y/N):-->")
                    if i.upper()=="YES" or i.upper()=="Y":
                        car_3()
                    elif (i.upper()=="N" or i.upper()=="NO"):
                        print()
                        gh=input(" "*43+">>>>>>>>>>PRESS ENTER TO CONTINUE<<<<<<<<<<")
                        print()
                        break
                    else:
                        print()
                        print(">"*10,"ENTER  A VALID VALUE!!!","<"*10,"\n")
            elif int(st_ch)==4:
                car_5()
            elif int(st_ch)==5:
                selled_cars()
            elif int(st_ch)==6:
                break            
    elif int(mn_ch)==3:
        break
        
# ENDING OF PROGRAM        
with open("thanks.txt",'r') as f:
    p=f.readlines()
    for i in p:
        for j in i:
            print(j,end="")
