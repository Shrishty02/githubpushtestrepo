class person:
    def age(self, curr_year, year_of_birth):
        return curr_year-year_of_birth

    def email_id_input(self, email_id):
        print("take the email id and print it",email_id)
    
    def ask_name(self):
        name=input("tell your name")
        return name
    def ask_dob(self):
        dob =input("tell your date of birth")
        return dob

sudh=person()
anuj=person()
gargi=person()
sudh.email_id_input("sudhanshu@ineuron.ai")
gargi.ask_name()
print(anuj.age(2022,1994))
sudh.ask_dob()
    