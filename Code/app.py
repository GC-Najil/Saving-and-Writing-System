print('***********************************')
print('Information')
print('***********************************')
print()
print('***********************************')
print("Remember, you cannot change this!!")
print('***********************************')

print()

filename = input("Database Name: ")
name = input("Your Name: ")
age = input("Your Age: ")
keyid = input("Key ID: ")
password = input("Your Password: ")

text_file = open(f"{filename}.txt", "w")
read_file = open(f"{filename}.txt", 'r')

text_file.write(f'Name : {name}, \nAge : {age}, \nKey ID : {keyid}, \nPassword : {password}')

print('Do you want to preview the details')

a = input("Yes / No : ")

if a == 'yes':
    checkpass = input("Your Password: ")

    if checkpass != password:
        print()
        print('Incorrect, Try Again')
        checkpass
    if checkpass == password:
        print()
        print("Ok, good to go")
        print()
        print(read_file.readlines())
    exit()

text_file.close()