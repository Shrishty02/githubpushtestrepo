#multi label code
class bank:   
    def transaction(self):
        print("total transatio value")
    def accout_opening(self):
        print("this will show yor acc open stayus")
    def deposite(self):
        print("this is to deposite")

class HDFC_bank(bank):
    def hdfc_to_icici(self):
        print("this will show your all transaction happened btw hdfc to icici")

class icici(HDFC_bank):
    pass
i =icici()
i.hdfc_to_icici()
i.deposite()
i.accout_opening()
i.accout_opening()


