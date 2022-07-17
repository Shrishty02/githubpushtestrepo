class person:
    def age(self, curr_year, year_of_birth):
        self.curr_year= curr_year
        self.year_oF_birth=year_of_birth
        return curr_year-year_of_birth

    def email_id_input(self, email_id):
        print("take the email id and print it",email_id)
    
    def ask_name(self):
        name=input("tell your name")
        return name
    def ask_dob(self):
        dob =input("tell your date of birth")
        return dob

sudhh=person()
print(sudhh.age(1990,2022))
sudhh.email_id_input("sudha@gmail.com")