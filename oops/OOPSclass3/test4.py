#data abstraction restricting the user to access directly(data hiding)
class ineuron:
    __students= "data science"
    def students(self):
        print("print the class of stidents", ineuron.__students)
i= ineuron()
i.students()
print(i._ineuron__students)

