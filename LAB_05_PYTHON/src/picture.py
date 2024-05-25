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
    imgVertical = [fila for fila in reversed(self.img)]
    return Picture(imgVertical)

  def horizontalMirror(self):
    imgHorizontal = [fila[::-1] for fila in self.img]
    return Picture(imgHorizontal)

  def negative(self):
    imgInvertida = []
    for fila in self.img:
        filaInvertida = ''.join([self._invColor(char) for char in fila])
        imgInvertida.append(filaInvertida)
    return Picture(imgInvertida)

  def join(self, p):
    imgNueva = []
    for x in range(len(self.img)):
      imgNueva.append(self.img[x] + p.img[x])
    return Picture(imgNueva)

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
    imgNueva = []
    imgNueva = self.img + p.img
    return Picture(imgNueva)
  
  def horizontalRepeat(self, n):
    if n <= 0:
        return Picture([])
    imgNueva = [row * n for row in self.img]
    return Picture(imgNueva)

  def verticalRepeat(self, n):
    if n <= 0:
        return Picture([]) 
    imgNueva = self.img * n 
    return Picture(imgNueva)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)