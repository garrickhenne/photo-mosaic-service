from PNG import PNG
from RGBAPixel import RGBAPixel

def color_to_pixel(color):
  """Converts a string representation of a color to an RGBAPixel object."""
  if (color == 'R' or color == 'r'):
    return RGBAPixel(255, 0, 0)
  elif (color == 'G' or color == 'g'):
    return RGBAPixel(0, 255, 0)
  elif (color == 'B' or color == 'b'):
    return RGBAPixel(0, 0, 255)
  elif (color == 'O' or color == 'o'):
    return RGBAPixel(255, 165, 0)
  elif (color == 'Y' or color == 'y'):
    return RGBAPixel(255, 255, 0)
  elif (color == 'I' or color == 'i'):
    return RGBAPixel(75, 0, 130)
  elif (color == 'V' or color == 'v'):
    return RGBAPixel(238, 130, 238)
  else:
    ERROR_bad_gaps(color)

def ERROR_bad_gaps(sgc):
  print('ERROR: unable to parse string specifying gaps and colors: \ {sgv} \ ')
  exit(1)

def parse_gaps(sgc):
  """
    Transform a sequence of number then letter pairs to a list of tuples containing the number and the RGBA 
    representation of the letter.
    An example representation: '0r10g7b'.
    Only supports ROYGBIV colors.
  """

  # Validate first input is a number at the very least.
  try:
    int(sgc[0])
  except:
    ERROR_bad_gaps(sgc)
  
  gap_sequence = []
  i = 0
  curr_number_str = ''
  while (i < len(sgc)):
    try:
      int(sgc[i])
      curr_number_str += sgc[i]
    except:
      number = int(curr_number_str)
      gap_sequence.append((number, color_to_pixel(sgc[i])))
      curr_number_str = ''
    i += 1
  
  return gap_sequence

def close_enough(color1: RGBAPixel, color2: RGBAPixel) -> bool:
  dist = (color1.r - color2.r)**2 + (color1.g - color2.g)**2 + (color1.b - color2.b)**2
  return dist < 80

def good(image: PNG, D, curr: tuple, next: tuple) -> bool:
  """
    Returns true iff a neighbor "next" of a pixel "curr" is:
    1. within the image,
    2. unvisited, and
    3. close in color to "curr".
    An entry in distance table D is -1 only if the pixel has not been visited.
  """
  return next[0] >= 0 and next[0] < image.width and next[1] >= 0 and next[1] < image.height and D[next[1]][next[0]] == -1 and close_enough(image.get_pixel(curr[0], curr[1]), image.get_pixel(next[0], next[1]))

def neighbours(curr: tuple):
  n = []

  n.append((curr[0] - 1, curr[1]))
  n.append((curr[0], curr[1] + 1))
  n.append((curr[0] + 1, curr[1]))
  n.append((curr[0], curr[1] - 1))

  return n

def create_mosaic(picture: PNG, start: tuple, sgc):
  queue = []
  domain = [[-1 for _ in range(picture.width)] for _ in range(picture.height)]
  gaps: tuple = parse_gaps(sgc)

  # Map of modulos to colours
  modulo_to_color = {}

  total = 0

  for gap in gaps:
    modulo_to_color[gap[0] + total] = gap[1]
    total += gap[0] + 1

  curr = start
  queue.append(curr)
  domain[curr[1]][curr[0]] = 0

  while (len(queue) > 0):
    curr = queue.pop(0)

    for neighbour in neighbours(curr):
      if (good(picture, domain, curr, neighbour)):
        queue.append(neighbour)
        domain[neighbour[1]][neighbour[0]] = domain[curr[1]][curr[0]] + 1
    
    if domain[curr[1]][curr[0]] % total in modulo_to_color:
      picture.set_pixel(curr[0], curr[1], modulo_to_color[domain[curr[1]][curr[0]] % total])
