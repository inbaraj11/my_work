students_dict = {
    0:{'name': 'Nanda', 'roll_number': 12, 'class': 10, 'section': 'A'}
}
def accept(n):
    members = int(input("how many members want to add:"))
    for i in range(members):
        name = input('enter the name :')
        roll_number = int(input('enter the roll_number :'))
        class_stu = input('enter the class :')
        section = input('enter the section :')
        students_dict2 = {'name': name, 'roll_number': roll_number, 'class': class_stu, 'section': section}
        students_dict[i+1] = students_dict2
    print(students_dict)

def delete(n):
    for i in range(len(students_dict)):
        if(students_dict[i]['roll_number'] == n):
            del students_dict[i]

def update(n):
    for i in range(len(students_dict)):
        ch = input('which one u want to update?:')
        if(ch == 'name'):
            if(students_dict[i]['roll_number'] == n):
                cn = input('which name u want 2 enter:')
            students_dict[i]['name'] = cn
        elif(ch == 'section'):
            if(students_dict[i]['roll_number'] == n):
                cs = input('which section u want 2 enter:')
            students_dict[i]['section'] = cs
    print(students_dict)

print("enter the operation which u want:")  
print("1. insert \n2. display \n3. delete \n4.update")
x = 'y'
while(x == 'y'):
    ch = int(input("enter the choices (1/2/3/4):"))
    if(ch == 1):
        i = input("want to add(y/n):")
        a = accept(i)
        x = input('do u want to continue (n/y):')
    elif(ch == 2):
        print(len(students_dict))
        #for i in range(len(students_dict)):
        print(students_dict)
        x = input('do u want to continue (n/y):')
    elif(ch == 3):
        roll = int(input("enter the roll number to delete:"))
        delete(roll)
        print("After deletion:")
        print(students_dict)
    elif(ch == 4):
        roll = int(input("enter the roll number to update:"))
        update(roll)
    else:
        print("please enter the valid number!")
