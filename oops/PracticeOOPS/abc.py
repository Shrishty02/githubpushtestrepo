class student: #outer class
    def __init__(self, name, rollno):
        self.name= name
        self.rollno= rollno
        self.lap =self.laptop()

    def show(self):
        print(self.name, self.rollno)

    class laptop: #inner class
        def __init__(self):
            self.brand="hp"
            self.cpu="i5"
            self.ram =8

            
s1= student("navin", 34)
s2 = student("reena",87)
s1.show()
print(s1.lap.brand)