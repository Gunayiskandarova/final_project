birthdays={"fexri":"1 january","murad":"2 january","elvin":"3 january"}


while True:
    print('write a name ' +" " +"to quite blank")
    name=input()
    if name == "":
        break
    if name in birthdays:
       print(birthdays[name]+ "is birthday of" + name + "in") 
    else:
       print('i do not have any information for'+ name)
       print("what is their birthday?")
       bday=input()
       birthdays[name]=bday
       print('birthday database uptaded')






