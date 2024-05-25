from interpreter import draw
from chessPictures import *

bloque = square.join(square.negative())

final = bloque.horizontalRepeat(4)

draw(final)