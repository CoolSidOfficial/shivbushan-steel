from os import system
from click import option
from datetime import  date
import time
#######################################################################

title= '''








 ____   _   _  ___ __     __ ____   _   _  _   _  ____   _   _     _      _   _   ____  _____  _____  _____  _     
/ ___| | | | ||_ _|\ \   / /| __ ) | | | || | | |/ ___| | | | |   / \   | \ | |  / ___||_   _|| ____|| ____|| |    
\___ \ | |_| | | |  \ \ / / |  _ \ | |_| || | | |\___ \ | |_| |  / _ \  |  \| | \___ \  | |  |  _|  |  _|  | |    
 ___) ||  _  | | |   \ V /  | |_) ||  _  || |_| | ___) ||  _  | / ___ \ | |\  |  ___) | | |  | |___ | |___ | |___ 
|____/ |_| |_||___|   \_/   |____/ |_| |_| \___/ |____/ |_| |_|/_/   \_\|_| \_| |____/  |_|  |_____||_____||_____|
                                                By CoolSid  Version 0.1                                                                                                                
'''


vehicles=["1985","2624","1353","3372","3374","8344","8256","9490","0199"]
whole_data=list()
#############################################################################
def option_checker(ch):
    if ch=="":
        print("Data cannot be empty")
        time.sleep(3)
        main()
    elif ch=="exit":
        exit()
################################ ####################################
def create_data():
    print("Please enter the data like this:~ ")
    today_data=input("bus-no,balance,diesel ,inital reading\n)>>")
    new_data=today_data.split(",")
    confirm_data=input(f"Please type again to confirm this::\n bus_no-{new_data[0]},balance-{new_data[1]} rupees, diesel-{new_data[2]} litres,intial reading-{new_data[3]}\n)>>")
    if not today_data==confirm_data:
        print("Data is not same try again :( ".center(50) )
        time.sleep(4)
        create_data()
    print("Data successfully saved".center(80))

    create_log(confirm_data)    
    
########################################################

def create_log(descri):
  with open("reports.log","a+") as file:
      current=date.today().strftime("%d-%m-%Y") # store date in the format of 10-02-2022
      file.write(current+","+ descri+"\n")
########################################################



def extract_data(date_n,vehicle_number):
    with open("reports.log","r") as file:
            for each in file:
                whole_data.append(each.rstrip())
    for each_da in whole_data:
        if date_n+","+vehicle_number in each_da:
            text=each_da.split(",")
            return text
            

##########################################################
def view_data():
   print("Please Enter the date to view the data like '10-08-2003'")
   date_name=input("#>>")
   option_checker(date_name)
   print("Choose any vehicle number from below")
   print(vehicles)
   vehicle_number=input("#>>>")
   option_checker(vehicle_number)
   return  extract_data(date_name,vehicle_number)

###############################################################   
def main():
    system("cls")
    print(title)
    print("CHOOSE ANY OPTION FROM BELOW::-\n\n [1])>>ENTER NEW DATA\n [2])>>VIEW ALL DATA")
    choice=input("#>>")
    option_checker(choice)      
    if choice=="1":   # to enter new data
        system("cls")
        print(title) 
        create_data()
        time.sleep(3)
        main() 
    elif choice=="2": #to view the data
         system("cls")
         print(title) 
         final =view_data()
        #  system("cls")
         print(title) 
            
         print(f" Date:: {final[0]} \n\n Bus number:: {final[1]}\n\n Balance::{final[2]} rupees\n\n diesel::{final[3]} litres \n\n intial reading ::{final[4]} ")
    else:
        print("Wrong input ,you can only choose  1 or 2")
        time.sleep(5)
        main()
##################################################################
if __name__=="__main__":
    main()
    input("press any key to exit".center(80))
#advance,final ,total