from RGBAPixel import RGBAPixel

class PNG:
  def __init__(self) -> None:
    self.width = 0
    self.height = 0
    self.image_data = None

  def __init__(self, width, height) -> None:
    self.width = width
    self.height = height
    self.image_data = [RGBAPixel() for _ in range(width * height)]

  def __eq__(self, __value: 'PNG') -> bool:
    if (self.width != __value.width or self.height != __value.height):
      return False
    for i in range(self.width * self.height):
      if (self.image_data[i] != __value.image_data[i]):
        return False
    return True
  
  def __ne__(self, __value: 'PNG') -> bool:
    return not self.__eq__(__value)
  
  def get_pixel(self, x, y):
    index = y * self.width + x
    return self.image_data[index]