class Polygon:

  def __init__(self, sides, name, area):
    self.sides = sides
    self.name = name
    self.area = area
  
  def get_sides(self):
    return self.sides
  
  def get_name(self):
    return self.name
  
  def get_area(self):
    return self.area
    
  def set_sides(self, sides):
    self.sides = sides
    
  def set_name(self, name):
    self.name = name
    
  def set_area(self, area):
    self.area = area
    
  def __str__(self):
    return f"Polygon name = {self.name}, sides = {self.sides}, area = {self.area}."
    
poly = Polygon(3, "Traiangle", 4.5)  
print(poly)