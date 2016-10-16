class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName,lastName,idNumber)
        self.scores = scores

    def letter_grade(self, grade):

        if grade >= 90:
            return 'O'
        elif grade >= 80:
            return 'E'
        elif grade >= 70:
            return 'A'
        elif grade >= 55:
            return 'P'
        elif grade >= 40:
            return 'D'
        else:
            return 'T'

    def calculate(self):
        total = 0
        for score in self.scores:
            total += score
        grade = total / len(self.scores)
        return self.letter_grade(grade)


        # letter_grade = {
        #     90: 'O',
        #     80: 'E',
        #     70: 'A',
        #     55: 'P',
        #     40: 'D',
        #     0: 'T',
        # }
        # return letter_grade.get(grade)
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())