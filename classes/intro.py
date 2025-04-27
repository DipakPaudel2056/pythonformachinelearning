# what exactly is class?
# class is a template for the data type

# how to create a class in pythn?

class Facade:
    pass #we use pass keyword here so that we dont get indentation error so we have left the blank space intentionally

# creating a class was just creating a blue print but to be able to use the class we  must instantiate it 
# let's instantiate a class and store it in variable, it is same as using function
facade_1 = Facade()

# we can also have the functions as a part of the class those functions are called method of the class and we create them in this way
class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."
# one thing to rememember here is self, self is the variable that is accessible within the class and it describes the object that it is contained in, in this case it is washing_brushes itself
class Circle:
  pi =3.14
  def area(self,radius):
    area = self.pi * radius ** 2
    return area


class Circle:
  pi =3.14
  def area(self,radius):
    area = self.pi * radius ** 2
    return area

circle = Circle()
pizza_area = circle.area(6)
teaching_table_area = circle.area(18)
round_room_area = circle.area(5730)