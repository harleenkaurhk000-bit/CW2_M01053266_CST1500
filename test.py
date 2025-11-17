print("Hello World version 2!")
print("what is your name?")


def menu():
  print ("*" *30)
  print("***Welcome to my system***")
  print("Chose from the following options: ")
  print("1. Register")
  print("2. Login")
  print("3. EXIT")
  print("*" * 30)

def main():
  while True:
    menu()
     choice = input(">")
    if choice == "1":
      register_user()
    elif choice == "2"
     if login_user():
       print("You have logged in!!")
    else: 
      print("Incorrect login!!")
    elif choice == "3":
    print("Goodbye!!")
    break

if__name__=="__":
  main()
