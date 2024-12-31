#Chapter7 : Review
#2024.12.31
#Jiyun Nam
#@codecademy

# 1. Define a class named Student
# Add constructor for Student
# Add 2 parameters: a name, and year 

class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    
    # 5. In the body of the constructor for Student, declare self.grades as empty list 
    self.grades = []

# 6. add_grade() method to Student and takes grade as parameter. 
# should verify that grade is of type Grade
  # If so, add it to the Student's grade
  # If not, nothing
  def add_grade(self, grade) :
   if type(grade) is Grade:
    self.grades.append(grade)
  
  def get_average(self):
    if not self.grades:
        return 0  # Return 0 if there are no grades
    total_score = sum(grade.score for grade in self.grades)  # Sum all scores
    return total_score / len(self.grades)  # Divide by the number of grades

  
  def add_attendance(self, date, attended):
     """Add attendance record for a specific date."""
     self.attendance[date] = attended


class Grade:
  # 3. Create a Grade class with minimum_passing as attribute set to 65
  minimum_passing = 65

  # 4. Give grade a constructor.
  # Take score parameter and assign it to self.score
  def __init__(self, score):
    self.score = score
  
  def is_passing(self):
    return self.score >= self.minimum_passing


# Check is_passing
print("Check: is_passing()")
grade2 = Grade(80)
print(grade2.is_passing()) 
  


# 2. Create 3 instances of the Student class
# ex) cool_object = CoolClass(cool_arg1, cool_arg2)
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

# 7. Create a new Grade with a score 100 and add it to pieter's grade attribute using add_grade()
pieter.add_grade(Grade(100))


pieter_scores = list(map(lambda grade: grade.score, pieter.grades))
print(pieter.name, pieter.year, pieter_scores)
#Pieter -> Student object
          # name : Peiter Bruegal the Elder
          # year : 8 

          # grade : []
          # By applying Grade(100) thorugh add_grade, grade : 100 


