from colors import *
class Picture:
  def __init__(self, img):
    self.img = img

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter: 
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    imgVertical = [line for line in reversed(self.img)]
    return Picture(imgVertical)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    return Picture(imgHorizontal)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    return Picture(None)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    ayuda = []
    for x in range(len(self.img)):
      ayuda.append(self.img[x] + p.img[x])
    return Picture(ayuda)

  def up(self, p):
    superposicion = []
    for i in range(max(len(self.img), len(p.img))):
      if i < len(p.img):
        if i < len(self.img):
          superposicion.append(''.join([self.img[i][j] if self.img[i][j] != ' ' else p.img[i][j] for j in range(max(len(self.img[i]), len(p.img[i]))) ]))
        else:
          superposicion.append(p.img[i])
      else:
        superposicion.append(self.img[i])
    return Picture(superposicion)
  
  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    ayuda = []
    ayuda = self.img + p.img
    return Picture(ayuda)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    return Picture(None)

  def verticalRepeat(self, n):
    return Picture(None)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)