# Mosaic Service

An API that allows you to send a PNG file along with coordinates and a color sequence that will return a transformed PNG of a mosaic of the photo.

Mosaic logic was part of an old assignment I did in a past class in university but translated into Python from C++.

Mosaic logic works by doing a Breadth-First-Search starting from the given coordinates and compares 'like' pixels from each other.

## API
Endpoint is POST `/api/upload/?:x&:y&:pattern`
- x,y are desired coordinates to start from PNG where (0,0) is top left of the PNG.
- Pattern is a desired color sequence like '0r0o0y0g0b0i0v' which will create a rainbow color with 0 gaps between colors.
- A PNG should also be included as `file` key.

## Screenshots

### Original
Centered at (10,10), sequence '0r0o0y0g0b0i0v' where the each number corresponds to the gap 'between' pixels and each letter corresponds to a color in 'ROYGBIV'


![Original Pepe](.github/images/pepeOG.png)


### Transformed


![Transformed Image](.github/images/zulktlwz.png)

![Blank transformed image](.github/images/blank-mosaic.png)

## Intention
I wanted to translate a past project of mine that I enjoyed into a more modern language, ie Python.
This project was done to increase my familiarity with Python as well as get some more practice using flask for creating servers. In the future I'd like to have this as a service that could be directly accessible from my portfolio website.