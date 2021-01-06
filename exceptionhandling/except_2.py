no1=int(input("enter value for no1"))
no2=int(input("enter value for no2"))

try:
    res=no1/no2  #10/2
    print(res)#5
except:
    no2=int(input("enter new value for no2"))
    try:
        res=no1/no2
        print(res)
    except:
        no2=int(input("enter new value for  no2"))
        res=no1/no2
        print(res)
finally:
    print("i have one database transaction")
    print("i have one file transaction")

#try:abnormal code
#except:exception handling
#finally:cleanup processing

#python to  mysql
#import package
#establish connection
#create cursor object
#execute queries -exception occur
#close connection