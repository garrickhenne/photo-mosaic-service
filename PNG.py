from RGBAPixel import RGBAPixel
import png

class PNG:
  def __init__(self, width=0, height=0) -> None:
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
  
  def read_from_file(self, filename):
    with open(filename, 'rb') as file:
      reader = png.Reader(file=file)
      width, height, pixels, _ = reader.asRGBA()
      self.width = width
      self.height = height
      self.image_data = [RGBAPixel() for _ in range(width * height)]
      for j, row in enumerate(pixels):
        for i in range(0, len(row), 4):
          new_pixel = RGBAPixel(row[i], row[i+1], row[i+2], row[i+3] / 255)
          self.image_data[j*width + i//4] = new_pixel

  def write_to_file(self, filename):
    with open(filename, 'wb') as file:
      writer = png.Writer(self.width, self.height, greyscale=False, alpha=True)
      pixels = []
      for j in range(self.height):
          row = []
          for i in range(self.width):
              pixel = self.image_data[j*self.width + i]
              row.extend([pixel.r, pixel.g, pixel.b, int(pixel.a * 255)])
          pixels.append(row)
      writer.write(file, pixels)
  
  
      

pngDude = PNG()
pngDude.read_from_file('./images/test10x10.png')
pngDude.write_to_file('./images/test10x10_copy.png')
