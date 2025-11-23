class Student:
    def __init__(self, name, phone, age, email):
        self.name = name
        self.phone = phone
        self.age = age
        self.email = email


class Group:
    def __init__(self, title, profession):
        self.title = title
        self.profession = profession
        self.students = []

    def add_student(self):
        name = input("name: ")
        phone = input("phone: ")
        age = input("age: ")
        email = input("email: ")
        student = Student(name, phone, age, email)
        self.students.append(student)
    def view_students(self):
        count = 0
        for item in self.students:
            count+=1
            print(f'{count}. name:{item.name}, age:{item.age}')


class OTM:
    def __init__(self, title):
        self.title = title
        self.groups = []

    def add_group(self):
        title = input("title:")
        profession = input("profession:")
        group = Group(title, profession)
        self.groups.append(group)

    def view_groups(self):
        count = 0
        for item in self.groups:
            count += 1
            print(f'{count}. title:{item.title} profession:{item.profession}')



class ERP:
    def __init__(self):
        self.title = 'ERP'
        self.otms = []

    def add_otm(self):
        title = input('title:')
        otm = OTM(title)
        self.otms.append(otm)

    def view_otms(self):
        count = 0
        for item in self.otms:
            count += 1
            print(f'{count}. title:{item.title}')
    def edit_otm(otm: OTM):
        new_title = input("New title: ")
        otm.title = new_title
        print("Title changed!")


erp = ERP()

def group_manager(group: Group):
    while True:
        kod = input(" 1. Add Student \n 2. View Srudents \n 3. Break")
        if kod == '1':
            print("============")
            group.view_students()
            print("------------")
        elif kod == '2':
            print("===========")
            group.view_students()
            print("------------")
        else:
            break

def otm_manager(otm: OTM):
    while True:
        kod = input(" 1. Add group \n 2. View groups \n 3. Break")
        if kod == '1':
            print("===========")
            otm.add_group()
            print("------------")
        elif kod == '2':
            print("===========")
            otm.view_groups()
            print("------------")
        else:
            break



def student_manager(group: Group):
    while True:
        kod = input(' 1. view students \n 2. delete student \n 3. break :')
        if kod=="1":
            print("==========")
            group.view_students()
            print("--------------")
        elif kod=="2":
            print('===========')
            group.view_students()
            print('------------')
            index = int(input("student_id (o'chirish uchun): "))
            if 0<index<=len(group.students):
                deleted = group.students[index-1].delete()
                print("Student deleted!")
            else:
                print("Student not found!")
        else:
            break





def edit_otm_name(otm: OTM):
    new_title = input("New title: ")
    otm.title = new_title
    print("Title changed!")

def student_manager(group: Group):
    while True:
        kod = input(" 1. view students \n 2. delete student \n 3. break")
        if kod=="1":
            print("===========")
            group.view_students()
            print("-----------")
        elif kod == "2":
            print('===========')
            group.view_students()
            print('-----------')
            if len(group.students)>0:
                index = int(input("student_id (o'chirish uchun): "))
                if 0<index<=len(group.students):
                    deleted = group.students[index-1].delete()
                    print("Student deleted!")
                else:
                    print("Student not found!")
            else:
                print("Student not found!")
            print("----------")
        else:
            break

def edit_group(group: Group):
    print("1. title o'zgartirish")
    print("2. profession o'zgartirish")
    choice = input("Tanlov: ")
    if choice == '1':
        group.title = input("Yangi title: ")
        print("Title o'zgartirildi!")
    elif choice == '2':
        group.profession = input("Yangi profession: ")
        print("Profession o'zgartirildi!")


def group_edit_manager(otm: OTM):
    print('===========')
    otm.view_groups()
    print('------------')
    if len(otm.groups) > 0:
        index = int(input("guruh_id (tahrirlash uchun): "))
        if 0 < index <= len(otm.groups):
            group = otm.groups[index - 1]
            edit_group(group)
        else:
            print("Noto'g'ri ID!")
    else:
        print("OTM da guruhlar yo'q!")


def edit_otm_manager(erp: ERP):
    print('===========')
    erp.view_otms()
    print('------------')
    if len(erp.otms) > 0:
        index = int(input("otm_id (tahrirlash uchun): "))
        if 0 < index <= len(erp.otms):
            otm = erp.otms[index - 1]
            edit_otm_name(otm)
        else:
            print("Noto'g'ri ID!")
    else:
        print("ERP da OTMlar yo'q!")


def erp_manager(ep: ERP):
    while True:
        print("\n========== MENU ==========")
        kod = input(' 1. add otm \n 2. view otms \n 3. group_section \n 4. edit otm \n 5. edit group \n 6. student section \n 7. break :')
        if kod == '1':
            print('===========')
            ep.add_otm()
            print('------------')
        elif kod == '2':
            print('===========')
            ep.view_otms()
            print('------------')
        elif kod == '3':
            print('===========')
            ep.view_otms()
            print('------------')
            if len(ep.otms) > 0:
                index = int(input("otm_id :"))
                if 0 < index <= len(ep.otms):
                    otm = ep.otms[index - 1]
                    otm_manager(otm)
                else:
                    print("Noto'g'ri ID!")
            else:
                print("ERP da OTMlar yo'q!")
        elif kod == '4':
            edit_otm_manager(ep)
        elif kod == '5':
            print('===========')
            ep.view_otms()
            print('------------')
            if len(ep.otms) > 0:
                otm_index = int(input("otm_id: "))
                if 0 < otm_index <= len(ep.otms):
                    otm = ep.otms[otm_index - 1]
                    group_edit_manager(otm)
                else:
                    print("Noto'g'ri ID!")
            else:
                print("ERP da OTMlar yo'q!")
        elif kod == '6':
            print('===========')
            ep.view_otms()
            print('------------')
            if len(ep.otms) > 0:
                otm_index = int(input("otm_id: "))
                if 0 < otm_index <= len(ep.otms):
                    otm = ep.otms[otm_index - 1]
                    print('===========')
                    otm.view_groups()
                    print('------------')
                    if len(otm.groups) > 0:
                        group_index = int(input("guruh_id: "))
                        if 0 < group_index <= len(otm.groups):
                            group = otm.groups[group_index - 1]
                            student_manager(group)
                        else:
                            print("Noto'g'ri ID!")
                    else:
                        print("OTM da guruhlar yo'q!")
                else:
                    print("Noto'g'ri ID!")
            else:
                print("ERP da OTMlar yo'q!")
        elif kod == '7':
            print("Dastur yakunlandi!")
            break
        else:
            print("Noto'g'ri tanlov!")

erp_manager(erp);