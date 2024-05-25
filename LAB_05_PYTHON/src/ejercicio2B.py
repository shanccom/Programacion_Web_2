from interpreter import draw
from chessPictures import *

filaPrimera = knight.join(knight.negative())
filaSegunda = knight.negative().horizontalMirror().join(knight.horizontalMirror())

final = filaPrimera.under(filaSegunda)

draw(final)