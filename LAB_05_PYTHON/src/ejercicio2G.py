from interpreter import draw
from chessPictures import *

#Bloques

bloqueB = square
bloqueN = square.negative()

# Fila de Peones

bloquePeones = pawn.up(square).join(pawn.up(square.negative()))
filaPeonesBlancos = bloquePeones.horizontalRepeat(4)
filaPeonesNegros = filaPeonesBlancos.negative()

#Parte del medio (bloques solos)

bloque = square.join(square.negative())
filaUno = bloque.horizontalRepeat(4)
filaDos = filaUno.negative()
union = filaUno.under(filaDos)
finalCuadrados = union.verticalRepeat(2)

#Parte de Piezas importantes

torre = rock.up(bloqueN)
caballo = knight.up(bloqueB)
alfil = bishop.up(bloqueN)
reyna = queen.up(bloqueB)
rey = king.up(bloqueN)
alfil2 = bishop.up(bloqueB)
caballo2 = knight.up(bloqueN)
torre2 = rock.up(bloqueB)

filaPiezas = torre.join(caballo).join(alfil).join(reyna).join(rey).join(alfil2).join(caballo2).join(torre2) 
filaPiezasNegras = filaPiezas.negative()

#Combinacion

final = filaPiezasNegras.under(filaPeonesNegros).under(finalCuadrados).under(filaPeonesBlancos).under(filaPiezas)

draw(final)     