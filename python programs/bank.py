import pickle
def add():
    
    f=open("EMP.dat",'ab')
    d={}
    while True:
        print('\n---------------------------------------------------------\n')
        b= input("ENTER EMPLOYEE ID ")
        a=input("ENTER EMPLOYEE NAME")
        c=float(input("ENTER EMPLOYEE   SALARY"))
        d["EMPLOYEE_ID" ]=  b
        d["EMPLOYEE_NAME"]= a
        d["SALARY"]= c
        pickle.dump(d,f)
        ch=input("Do you want to enter more record (y\\n)")
        if ch.lower()=='n':
            break
    #pickle.dump(record,f)
def Read():
    f=open("EMP.dat",'rb')
    
    print("THIS IS EXISTING RECORDS OF EMPLOYEES",end='\n==============================\n')
    try:
        print("employee having salary less than 10000")

        while True:
            d=pickle.load(f)
            if float(d['SALARY'])<=10000:
                print("Employee Id:",d["EMPLOYEE_ID"])
                print("Employee Name:",d["EMPLOYEE_NAME"])
                print("Salary                  :",d["SALARY"])
                                

    except EOFError:
        f.close()
    



        
        

add()
Read()


