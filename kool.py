import pickle
import colorama
import ascii_magic
ANKOR = ascii_magic.from_image_file("C:\\Users\\ankor\\Desktop\\python programs\\1.webp",columns=80,char="@")
ascii_magic.to_terminal(ANKOR)


from colorama import Fore, Back,Style,init
colorama.init()




#----------APPEND FUNCTION-------(to add patient info)-------------

def Append():
    try:
        f=open("ankurkanaujia.dat",'ab')
        record=[]
        while True:
            print=('\n---------------------------------------------------------------------------\n')
            bldgrptyp=input("Enter blood group type:")
            name=input("Enter donars name")
            dnrno=input("Enter donar number:")
            state=input("Enter state")
            city=input("Enter city")
            addres=input("Enter Address")
            phnno1=input("Enter phone number:")
            phnno2=input("Enter alternative phone number:")
            data=[name,bldgrptyp,dnrno,city,state,addres,phnno1,phnno2]
            record.append(data)
            ch=input("Do you want to enter more record (y\\n)")
            if ch=='n':
                break
        pickle.dump(record,f)
        f.close()
    except Exception :
        print("OUR PROGRAM GET CRASHED  DUE TO SOME REASON (next time we will try to fix it)")
    
          
    

    
#------------READ FUNCTION-----------
def read():
    try:
        f=open("ankurkanaujia.dat",'rb')
        print("THIS IS LIST FOR  EXISTING RECORDS OF BLOOD DONORS",end='\n==================================================\n')
        while True:
            try:
                s=pickle.load(f)
                
                for i in s:
                    
                    print("NAME=",i[0],end='\n---------------------------------------------------------------------------|\n')
                    print("BLOODGROUP TYPE=",i[1],end='\n---------------------------------------------------------------------------|\n')
                    print("DONOR NUMBER=",i[2],end='\n---------------------------------------------------------------------------|\n')
                    print("CITY=",i[3],end='\n---------------------------------------------------------------------------|\n')
                    print("STATE=",i[4],end='\n---------------------------------------------------------------------------|\n')
                    print("ADDRESS=",i[5],end='\n---------------------------------------------------------------------------|\n')
                    print("PHONE NO.=",i[6],end='\n---------------------------------------------------------------------------|\n')
                    print("ALTERNATIVE PHONE NO.=",i[7],end='\n===============================================================\n')
            except EOFError:
                break
        f.close()
        xx=input("SEEMS LIKE HERE IS NOT ENOUGH DONORS \n>>how bad it is, \n>>you know donating blood keeps donor healthy \n>>IF YOU WANT TO KNOW HEALTH BENEFITS THEN TYPE 'yes'  \n OR YOU CAN SIMPLY PRESS ENTER TO SKIP" )
        if xx=='yes':
            print("visit this link  ' https://www.indushealthplus.com/blood-donation-facts-benefits.html ' to know benefits")
        f.close()

    except Exception :
        print("OUR PROGRAM GET CRASHED  DUE TO SOME REASON (next time we will try to fix it)")
    



    
 #-----------SEARCH FUNCTION---------
#------------ALL done (working)-----------------------------------------------------------------------
def search():
    try:
        f=open("ankurkanaujia.dat",'rb')                          #variable (s,f,i,n,p,and m )are in use please use another one
        s=pickle.load(f)
        print('---------------------------------------------------------------------------|\n')
        print("if you want to search from donar's name then press n ")
        print('---------------------------------------------------------------------------|\n')
        print("if you want to search from donars number then press m")
        print('---------------------------------------------------------------------------|\n')
        print("if you want to search from donars phone number then press p")
        print('---------------------------------------------------------------------------|\n')
        print("if you want to search from donars alternative phone number then press ap")
        print('---------------------------------------------------------------------------|\n')
        xx1=input()
        
        if xx1=='n':
            xx10=input("ENTER NAME  TO SEARCH :")
            found=0
            for i in s:
                
                if xx10==i[0]:
                    
                    print('\n---------------------------------------------------------------------------|\n')
                    print("NAME=",i[0],end='\n---------------------------------------------------------------------------|\n')
                    print("BLOODGROUP TYPE=",i[1],end='\n---------------------------------------------------------------------------|\n')
                    print("DONOR NUMBER=",i[2],end='\n---------------------------------------------------------------------------|\n')
                    print("CITY=",i[3],end='\n---------------------------------------------------------------------------|\n')
                    print("STATE=",i[4],end='\n---------------------------------------------------------------------------|\n')
                    print("ADDRESS=",i[5],end='\n---------------------------------------------------------------------------|\n')
                    print("PHONE NO.=",i[6],end='\n---------------------------------------------------------------------------|\n')
                    print("ALTERNATIVE PHONE NO.=",i[7],end='\n---------------------------------------------------------------------------|\n')
                    found=1
                else:
                    print()
                    
            if found==0:
                print("RECORD NOT FOUND..")
                #----------------------

        elif xx1=='m':
            xx11=input("ENTER DONOR'S NUMBER  TO SEARCH:")
            found=0
            for i in s:
            
                if xx11==i[2]:
                    print('\n---------------------------------------------------------------------------|\n')
                    print("NAME=",i[0],end='\n---------------------------------------------------------------------------|\n')
                    print("BLOODGROUP TYPE=",i[1],end='\n---------------------------------------------------------------------------|\n')
                    print("DONOR NUMBER=",i[2],end='\n---------------------------------------------------------------------------|\n')
                    print("CITY=",i[3],end='\n---------------------------------------------------------------------------|\n')
                    print("STATE=",i[4],end='\n---------------------------------------------------------------------------|\n')
                    print("ADDRESS=",i[5],end='\n---------------------------------------------------------------------------|\n')
                    print("PHONE NO.=",i[6],end='\n---------------------------------------------------------------------------|\n')
                    print("ALTERNATIVE PHONE NO.=",i[7],end='\n---------------------------------------------------------------------------|\n')
                    found=1
                else :
                    print()
            if found==0:
                print("RECORD NOT FOUND")
                    
                
        elif xx1 =='p':
            xx12=str(input("ENTER DONOR'S PHONE NUMBER TO SEARCH:"))
            found=0
            for i in s:
                if xx12==i[6]:
                    print('\n---------------------------------------------------------------------------|\n')
                    print("NAME=",i[0],end='\n---------------------------------------------------------------------------|\n')
                    print("BLOODGROUP TYPE=",i[1],end='\n---------------------------------------------------------------------------|\n')
                    print("DONOR NUMBER=",i[2],end='\n---------------------------------------------------------------------------|\n')
                    print("CITY=",i[3],end='\n---------------------------------------------------------------------------|\n')
                    print("STATE=",i[4],end='\n---------------------------------------------------------------------------|\n')
                    print("ADDRESS=",i[5],end='\n---------------------------------------------------------------------------|\n')
                    print("PHONE NO.=",i[6],end='\n---------------------------------------------------------------------------|\n')
                    print("ALTERNATIVE PHONE NO.=",i[7],end='\n---------------------------------------------------------------------------|\n')
                    
                    found=1
                else:
                    print()
            if found==0:
                print("record not found..")
            else:
                print( )
        elif xx1=='ap':
            xx13=str(input("ENTER DONOR'S ALTERNATIVE PHONE NUMBER TO SEARCH :"))
            found=0
            for i in s:
                if xx13==i[7]:
                    print('\n---------------------------------------------------------------------------|\n')
                    print("NAME=",i[0],end='\n---------------------------------------------------------------------------|\n')
                    print("BLOODGROUP TYPE=",i[1],end='\n---------------------------------------------------------------------------|\n')
                    print("DONOR NUMBER=",i[2],end='\n---------------------------------------------------------------------------|\n')
                    print("CITY=",i[3],end='\n---------------------------------------------------------------------------|\n')
                    print("STATE=",i[4],end='\n---------------------------------------------------------------------------|\n')
                    print("ADDRESS=",i[5],end='\n---------------------------------------------------------------------------|\n')
                    print("PHONE NO.=",i[6],end='\n---------------------------------------------------------------------------|\n')
                    print("ALTERNATIVE PHONE NO.=",i[7],end='\n---------------------------------------------------------------------------|\n')
                    found=1
                else:
                    print()
            if found==0:
                print("record not found..")
                
        else:
            print("hey dear may be you press wrong key please check it ")
            xx2=input("if you want above menu again then PRESS 'x")
            if xx2.lower()=='x':
                search()
        f.close()


    except Exception :
        print("OUR PROGRAM GET CRASHED  DUE TO SOME REASON (next time we will try to fix it)")
    

#------------work is DONE-----------------------------------------

#-------------------UPDATE FUNCTION ---------------------------

def update():
    found=0#------------------------------------to update name
    g= open("ankurkanaujia.dat",'rb+')
    s=pickle.load(g)
    xx3=input("ENTER DONOR NO. OF PATIENT TO UPDATE NAME")
    for i in s:
        if xx3==i[2]:
            print("CURRENT NAME OF THIS GUY:",i[0])
            i[0]=str(input("ENTER NEW NAME ="))
            found=1
            break
    if found==0:
        print("record not found .")
        xx30=input("want to update name of another patient press 'z'")
        if xx30=='z':
            update()
        else:
            print("you press wrong key call 'update()' func. manually to do so")
    else:
        g.seek(0)
        pickle.dump(s,g)
    g.close()
    print("RECORD UPDATED SUCCESFULLY \nNOW YOU'RE REDIRECTED TO MAIN MENU")
    menu()





def update1():
    found=0#to update bloodgroup type
    g= open("ankurkanaujia.dat",'rb+')
    s=pickle.load(g)
    xx3=str(input("ENTER DONOR NO. OF PATIENT TO UPDATE BLOOD GROUP TYPE"))
    for i in s:
        if xx3==i[2]:
            print("CURRENT NAME OF THIS GUY:",i[0])
            i[1]=str(input("ENTER NEW BLOOD GROUP TYPE ="))
            found=1
            break
    if found==0:
        print("record not found .")
        xx30=input("want to update blood group of another patient press 'z'")
        if xx30=='z':
            update1()
        else:
            print("you press wrong key call 'update1()' func. manually to do so")
    else:
        g.seek(0)
        pickle.dump(s,g)
    g.close()
    print("RECORD UPDATED SUCCESFULLY \nNOW YOU'RE REDIRECTED TO MAIN MENU")
    menu()



def update2():
    found=0#to update donar number
    g= open("ankurkanaujia.dat",'rb+')
    s=pickle.load(g)
    xx3=str(input("ENTER OLDER DONOR NO. OF PATIENT TO UPDATE NEW ONE"))
    for i in s:
        if xx3==i[2]:
            print("CURRENT NAME OF THIS GUY:",i[0])
            i[2]=str(input("ENTER NEW DONAR NUMBER ="))
            found=1
            break
    if found==0:
        print("record not found .")
        xx301=input("want to update donor no. of another patient press 'q")
        if xx301=='q':
            update2()
        else:
            print("you press wrong key call 'update2()' func. manually to do so")
    else:
        g.seek(0)
        pickle.dump(s,g)
    g.close()
    print("RECORD UPDATED SUCCESFULLY \nNOW YOU'RE REDIRECTED TO MAIN MENU")
    menu()




def update3():
    found=0#to update PHONE NUMBER
    g= open("ankurkanaujia.dat",'rb+')
    s=pickle.load(g)
    xx3=str(input("ENTER DONOR NO. OF PATIENT TO UPDATE PHONE NO."))
    for i in s:
        if xx3==i[2]:
            print("CURRENT NAME OF THIS GUY:",i[0])
            i[6]=str(input("ENTER NEW PHONE NUMBER ="))
            found=1
            break
    if found==0:
        print("record not found .")
        xx30=input("want to update phone no. of another patient press 'z'")
        if xx30=='z':
            update3()
        else:
            print("you press wrong key call 'update3()' func. manually to do so")
    else:
        g.seek(0)
        pickle.dump(s,g)
    g.close()
    print("RECORD UPDATED SUCCESFULLY \nNOW YOU'RE REDIRECTED TO MAIN MENU")
    menu()



#---------------------menu function__________________________________

def menu():
    print()
    print(Fore.RED + "TO MAINTAIN BLOOD BANK DATA THIS PROGRAM OFFERS VARIETY OF FEATURES LISTED BELOW.")
    print()
    print(Fore.YELLOW + "==============================================================================")
    print(Fore.GREEN+ "TO ADD PATIENT INFORMATION TYPE 'info'    or   '1'                            | ")
    print(Fore.CYAN + '------------------------------------------------------------------------------|')
    print(Fore.MAGENTA + "TO SEARCH PATIENT INFORMATION TYPE 'search'  or  '2'                          | ")
    print(Fore.CYAN + '------------------------------------------------------------------------------|')
    print(Fore.YELLOW + "TO  UPDATE EXISTING INFORMATION TYPE 'update' or  '3'                         |")
    print(Fore.CYAN + '------------------------------------------------------------------------------|')

    print(Fore.GREEN + "IF YOU WANT TO READ EXSISTING RECORD TYPE 'rr' or '4'                         |")
    print(Fore.CYAN + '------------------------------------------------------------------------------|')
    print(Fore.RED + "IF YOU WANT TO GO THROUGH ALL ABOVE FUNCTIONS THEN TYPE 'all' or '5'          |")
    print(Fore.CYAN + '------------------------------------------------------------------------------|')
    print(Fore.YELLOW + "IF YOU WANT ABOVE MENU AGAIN THEN TYPE  'menu()' ANYWHERE                     |"                )

    print(Fore.CYAN + '------------------------------------------------------------------------------|')
    print(Fore.CYAN + "TIP:- You can update patient records by using donor number only.              |")
    print(Fore.CYAN + "TIP:- You need to add patient info before trying search or update function.   |")
    print(Fore.CYAN + "TIP:- Delete old records by  typing 'delete' if you want to start Fresh with. |")
    
    print(Fore.CYAN + '______________________________________________________________________________|')
    xux=input()
    print(Fore.CYAN + '------------------------------------------------------------------------------|')

    if xux=='info' or xux=='1' :
        print(Fore.YELLOW + "==============================================================================")
        Append()
        print(Fore.RED + "DATA WAS WRITTEN SUCCESFULLY \nNOW YOU'RE REDIRECTED TO MENU AGAIN")
        print(Fore.YELLOW + "==============================================================================")
        menu()
        print(Fore.YELLOW + "==============================================================================")

    elif xux=='delete' or xux=='DELETE' :
            delete()
    elif xux=='search' or xux=='2' :
        print(Fore.YELLOW + "==============================================================================")
        search()
        print(Fore.YELLOW + "==============================================================================")
        print(Fore.RED + "HOPE YOU FIND NEEDED RESULT \nNOW YOU'RE REDIRECTED TO MENU AGAIN")
        menu()
        print(Fore.YELLOW + "==============================================================================")
    elif xux=='all' or xux=='5' :
        print(Fore.YELLOW + "==============================================================================")
        print(Fore.RED + "NOW YOU ARE REDIRECTED TO ADD INFO FUNCTION ")
        print(Fore.YELLOW + "==============================================================================")
        Append()
        print(Fore.YELLOW + "==============================================================================")
        print(Fore.RED + "RECORD WRITTEN SUCCESFULLY [ NEW RECORDS ARE GIVEN BELOW OF THE LIST ] ")
        print(Fore.YELLOW + "==============================================================================")
        read()
        print(Fore.YELLOW + "==============================================================================")
        print(Fore.RED + "NOW YOU'RE REDIRRECTED TO SEARCH FUNCTION")
        print(Fore.YELLOW + "==============================================================================")
        search()
        print(Fore.YELLOW + "==============================================================================")
        print(Fore.YELLOW + "==============================================================================")
        print(Fore.RED + "NOW YOU'RE REDIRRECTED TO UPDATE FUNCTION")
        print(Fore.YELLOW + "==============================================================================")
        print(Fore.YELLOW + "THIS IS LAST FUNCTION OF THE PROGRAM BUT NOT THE LEAST ")
        print(Fore.YELLOW + "==============================================================================")
        print(Fore.YELLOW + "==============================================================================")
        print(Fore.YELLOW + "==============================================================================")
        needed()
        
        
        print(Fore.YELLOW + "==============================================================================")
        print(Fore.YELLOW + "==============================================================================")
        print(Fore.YELLOW + "==============================================================================")
        print("NOW YOU ARE REDIRECTED TO MENU")
        menu()

    elif xux=='rr' or xux=='4' :
        read()
        print(Fore.RED + "NOW YOU'RE REDIRECTED TO MENU AGAIN")
        menu()
    elif xux=='menu':
        menu()                                                                                                                                      
    elif xux=='update' or xux=='3' :
        print(Fore.YELLOW + "==============================================================================")
        print(Fore.YELLOW + "==============================================================================")
        print(Fore.YELLOW + "IF YOU WANT TO UPDATE NAME TYPE 'nn'")
        print(Fore.RED + "IF YOU WANT TO UPDATE BLOOD GROUP TYPE 'mm'")
        print(Fore.CYAN + "IF YOU WANT TO UPDATE DONOR NUMBER TYPE 'dn'")
        print(Fore.MAGENTA + "IF YOU WANT TO UPDATE PHONE NUMBER TYPE 'pp'")
        print(Fore.YELLOW + "==============================================================================")
        print(Fore.YELLOW + "==============================================================================")
        
        
        xuy=input()
        if xuy=='nn':
            update()
            
        elif xuy=='mm':
            update1()
        elif xuy=='dn':
            update2()
        elif xuy=='pp':
            update3()
        

        else:
            print(Fore.YELLOW + "==============================================================================")
            xuz=input(Fore.RED + "oh dear may be you press wrong key \n iF you want above menu again then press ' 9'")
            print(Fore.YELLOW + "==============================================================================")
            if xuz=="9":
                update()
            else :
                print("AGAIN YOU PRESS WRONG KEY ")

#____________________this is needed one ________________




def needed():
    
    print(Fore.CYAN + '------------------------------------------------------------------------------|')
    print(Fore.CYAN + '------------------------------------------------------------------------------|')
    print("WANNA UPDATE NAME OF DONOR PRESS '1'")
    print(Fore.CYAN + '------------------------------------------------------------------------------|')
    print("FOR BLOOD GRP. PRESS                                '2'")
    print(Fore.CYAN + '------------------------------------------------------------------------------|')
    print("FOR DONOR NO. PRESS                                  '3'")
    print(Fore.CYAN + '------------------------------------------------------------------------------|')
    print("FOR PHN. NO. PRESS                                       '4'")
    print(Fore.CYAN + '------------------------------------------------------------------------------|')
    print(Fore.CYAN + '------------------------------------------------------------------------------|')
    x=input()
    if x=='1':
        update()

    elif x=='2':
        update1()

    elif x=='3':
        update2()

    elif x=='4':
        update3()
        

    else:
        y=input("CHECK , MAYBE YOU PRESS WRONG KEY\nIF YOU WANT ABOVE MENU AGAIN PRESS '5'")
        if y.lower()=='5':
            needed()
    print(Fore.YELLOW + "==============================================================================")
    print(Fore.YELLOW + "==============================================================================")
    print("ALL THINGS ARE DONE ")
    print(Fore.YELLOW + "==============================================================================")
    print(Fore.YELLOW + "==============================================================================")
    print("records updated")

    
#-----------------DELETE FUNCTION-----------------------------
def delete():
    s=open("ankurkanaujia.dat",'wb+')
    f=pickle.load(s)
    print(f.write())
    pickle.dump(f,s)
    print("ALL RECORDS WERE DELETED")
    menu()
    s.close()

        
    

#----------------------THIS IS FOR GUI--------------------------
    
'''print("TO MAINTAIN BLOOD BANK DATA THIS PROGRAMS OFFERS VARIETY OF FEATURES LISTED BELOW.")
print("==================================================================")
print("TO ADD PATIENT INFORMATION TYPE 'info'    or   '1'")
print('----------------------------------------------------------------------------------|')
print("TO SEARCH PATIENT INFORMATION TYPE 'search'  or  '2'")
print('----------------------------------------------------------------------------------|')

print("TO  UPDATE EXISTING INFORMATION TYPE 'update' or  '3'")
print('----------------------------------------------------------------------------------|')

print(" feel's like someone watching me  the man out side in the tree that's the reason i can't i see him lurkin in dream IF YOU WANT TO READ EXSISTING RECORD TYPE 'rr' or '4'")
print('----------------------------------------------------------------------------------|')
print("IF YOU WANT TO GO THROUGH ALL OF ABOVE FUNCTION THEN TYPE 'all' or '5'")
print('----------------------------------------------------------------------------------|')
print("IF YOU IF I ATW LITTLE WHILE HOW LONG YOU MAZKE ME ALONE AND OPEN HEATER FOR ME CUZ I'M COLDWANT ABOVE MENU AGAIN THEN TYPE  'menu()' ANYWHERE")

print('----------------------------------------------------------------------------------|')
print("TIP:- you can update patient records by using donor number only")
print('----------------------------------------------------------------------------------|')
xux=input()
print('----------------------------------------------------------------------------------|')

if xux=='info' or xux=='1' :
    Append()
elif xux=='search' or xux=='2' :
    search()
elif xux=='all' or xux=='5' :
    
    Append()
    print("RECORD WRITTEN SUCCESFULLY APPENDED RECORDS ARE GIVEN BELOW OF THE LIST ")
    read()
    print("NOW YOU'RE REDIRRECTED TO SEARCH FUNCTION")
    search()
    print("NOW YOU'RE REDIRRECTED TO UPDATE FUNCTION")
    update()
    print("records updated")
    print("THIS IS LAST FUNCTION OF THE PROGRAM BUT NOT THE LEAST ")
    print("IF YOU WANT ABOVE MENU AGAIN THEN TYPE  'menu()' ANYWHERE")

elif xux=='rr' or xux=='4' :
    read()
elif xux=='menu':
    menu()                                                                                                                                        #SUSPECT
elif xux=='update' or xux=='3' :
    print("IF YOU WANT TO UPDATE NAME TYPE 'nn'")
    print("IF YOU WANT TO UPDATE BLOOD GROUP TYPE 'mm'")
    print("IF YOU WANT TO UPDATE DONOR NUMBER TYPE 'dn'")
    print("IF YOU WANT TO UPDATE PHONE NUMBER TYPE 'pp'")
    
    
    xuy=input()
    if xuy=='nn':
        update()
    elif xuy=='mm':
        update1()
    elif xuy=='dn':
        update2()
    elif xuy=='pp':
        update3()

    else:
        xuz=input("oh dear may be you press wrong key \n iF you want above menu again then press ' 9'")
        if xuz=="9":
            update()

            '''

menu()

#===========================================+++++++++++++++++++++++++++++++++++++++++===============================================
'''
CODE WAS WRITTEN BY ((ANKUR KANAUJIA))
IDEA BY ((RAGHAV VERMA))
SUPPORTED BY ((UTTKARSH CHAWLA))  '''

