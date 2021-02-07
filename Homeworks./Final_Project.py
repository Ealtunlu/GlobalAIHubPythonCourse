# Final Project:
# Company Management System: Determine the names and ages of employees,
# company managers, and the languages they can speak. Then write a program that
# will print the languages that any of the employees can speak. In this project
# complete the project by creating two classes named employees and manager.
lang_list = []
employee_list = {}

class Employees():
    def __init__(self,name,age,languages_spoken):
        global spkn_lang
        self.name = name
        self.age = age
        self.languages_spoken = languages_spoken
        employee_list[name] = "Employee"
        def known_languages(self):
            lang_list.append(languages_spoken)
        known_languages(languages_spoken)
        spkn_lang = sorted(set([j for i in lang_list for j in i]))
    def is_employee(self):
        return True

class Manager(Employees):
    def __init__(self,name,age,languages_spoken):
        super().__init__(name,age,languages_spoken)
        employee_list[name] = "Manager"
    def is_manager(self):
        return True

mike = Employees("Mike",23,["English"])
ugur = Employees("Ugur",24,["Turkish","Japanese"])
rabia = Employees("Rabia",45,["Turkish","Polish"])
adam = Employees("Adam",50,["English","German","Swedish","Persian"])
ecem = Employees("Ecem",20,["Turkish","English","Spanish"])
emre = Manager("Emre",19,["English","Turkish","Russian"])
print(f"Employee's : {employee_list}\nSorted Languages Known : {spkn_lang}")
