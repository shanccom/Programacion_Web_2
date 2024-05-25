from interpreter import draw
from chessPictures import *

filaPrimera = knight.join(knight.negative())
filaSegunda = knight.negative().join(knight)

final = filaPrimera.under(filaSegunda)

draw(final)