from PNG import PNG
import mosaic
from util.random_string import create_random_string

def create_mosaic_file(filename, coordinates, pattern):
  loc = create_random_string()
  loc = './temp/' + loc + '.png'
  png_file = PNG()
  png_file.read_from_file(filename)
  mosaic.create_mosaic(png_file, coordinates, pattern)
  png_file.write_to_file(loc)
  return loc