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


# Methods that are used to prepare an object being instantiated are called constructors

class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self,diameter): #this is the constructor function we defined earlier, it will run no matter whatever happens inside other function
    print("New circle with diameter:" +str(diameter))
    
  
teaching_table = Circle(36)



# there is a global function in python called hasattr() that takes the variable and check if it has thatt attribute this function is called hasattr() function, it takes two parameter, one with the variable and other with the attribute that we want to test against..

# here is the quick implementation of the hasattr() function
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]
for element in can_we_count_it:
  if(hasattr(element,"count")):
    print(str(type(element)) + " has the count attribute!")
  else:
    print(str(type(element)) + " does not have the count attribute :(")

