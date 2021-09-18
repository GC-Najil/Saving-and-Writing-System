print("***********************")
print("Joojle")
print("***********************")
print()
print("***********************")
print("Do you want to see your data? ")
a = input("y/n : ")

if a == 'y': 
    data_name = input("Ok, type your database name: ")


    if data_name != data_name:
        print("No such database")
    if data_name == data_name:
        file = open(f'{data_name}.txt', 'r')
        print(file.readlines())
    


