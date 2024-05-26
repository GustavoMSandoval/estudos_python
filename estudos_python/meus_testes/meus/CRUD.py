register = []
personal_data = {}
def menu():
  print("""
[1]-create
[2]-read
[3]-update
[4]-delete
[5]-stop program
""")
def create():
  
     personal_data["name"] = input("What is your name:")
     personal_data["code"] = input("Say your code:")
     register.append(personal_data.copy())
   
   
   

def read():
   for  data in register:
        print(data)
      
def update():
   change = int(input("What user do you want to change? "))
   del(register[change])
   personal_data["name"] = input("New name:")
   personal_data["code"] = input("New code:")
   register.insert(change,personal_data.copy())

def delete():
   choose = int(input("Choose an user to delete:"))
   del(register[choose])

   
  


while True:
    try:
       menu()
       op = int(input("What do you choose?"))
       print('')
       if op == 1:
          create()
       elif op == 2:
          read()
       elif op == 3:
          update()
       elif op == 4:
          delete()
       elif op == 5:
          break
       else:
          print("\033[31mERROR invalid number\033[m")
    except:
       print("\033[31mERROR Invalid option\033[m")
    

