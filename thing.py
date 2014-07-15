class Person():
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
    
  def print_name(self):
    print ("%s" + " " + "%s") % (self.first_name, self.last_name)

  def special_message(self):
    print ("This is a special message")       

c = Person("Nazario", "Ayala")
c.print_name()
c.special_message()
