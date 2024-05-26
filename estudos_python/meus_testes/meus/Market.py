from random import randint
register = []
data = {}
wallet = 56.70
fo = 56
hy = 67
cl = 89
el = 30
pr = el+hy+fo+cl
def stock():
    print(f"""We have 
          {fo} foods
          {hy} hygienics
          {cl} clothes
          {el} electronics
          """)
    
def menu():
    print("Are you registered? [Y/N]")
    op = input(' ').strip()
    if op  in 'Yy':
        print("Pleasure to see you again")
    else:
        print("Being registered allows you to get discounts do you want to continue?")
        op = input(' ').strip().lower()
        if op == 'yes' or 'y' or 'yeah':
             data["name"] = input("name")
             data["code"] = print(randint(0,9))
             
             
    

def products():
    print("""What do you want to buy? 
   [1]-food
   [2]-hygiene
   [3]-clothes
   [4]-electronics
   [5]-exit     
               """)
    op = input(' ')
    qty = int(input("How many of these you want?"))
  
    try:
       match op:
          case '1':
            new_qty = pr - qty
            fo = fo - qty
            return new_qty,fo
            
          case '2':
            new_qty = pr - qty
            hy = hy - qty
            return new_qty
          case '3':
            new_qty = pr - qty
            el = el - qty
            return new_qty
          case '4':
            new_qty = pr - qty
            cl = cl - qty
            return new_qty
          case '5':
            exit()
    except:
        print("\033[31mERRO ao escolher opção\033[m")  
    else:
        print("\033[mERRO ao subtrair\033[m")
        
    
    





while True:
       
       stock()
       menu()
       products()
