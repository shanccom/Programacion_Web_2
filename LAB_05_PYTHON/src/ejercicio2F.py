from interpreter import draw
from chessPictures import *

bloque = square.join(square.negative())
filaUno = bloque.horizontalRepeat(4)
filaDos = filaUno.negative()
union = filaUno.under(filaDos)
final = union.verticalRepeat(2)

draw(final)