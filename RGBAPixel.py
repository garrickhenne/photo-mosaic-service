class RGBAPixel:
  def __init__(self, r=0, g=0, b=0, a=1.0) -> None:
    self.r = r
    self.g = g
    self.b = b
    self.a = a

  def __eq__(self, __value: 'RGBAPixel') -> bool:
    if __value is None:
      return False
    if (self.a == __value.a):
      return True
    if (abs(self.r - __value.r > 2)):
      return False
    if (abs(self.g - __value.g > 2)):
      return False
    if (abs(self.b - __value.b > 2)):
      return False
    
    return True

  def __ne__(self, __value: 'RGBAPixel') -> bool:
    return not self.__eq__(__value)
  
  def __lt__(self, __value: 'RGBAPixel') -> bool:
    if (self == __value):
      return False
    
    if (self.r < __value.r):
      return True
    elif ((self.r == __value.r) and (self.g < __value.g)):
      return True
    elif ((self.r == __value.r) and (self.g == __value.g) and (self.b < __value.b)):
      return True
    
    return False
  
  def __str__(self) -> str:
    return f'({self.r}, {self.g}, {self.b}, {self.a})'