import pygame

# Colores
NEGRO   = (   0,   0,   0)
BLANCO    = ( 255, 255, 255)
AZUL     = (   0,   0, 255)
ROJO      = ( 255,   0,   0)
VERDE    = (   0, 255,   0)

# Dimensiones pantalla
ANCHO  = 300
ALTO = 300

class Menu():
	
	color=BLANCO
	fondo=NEGRO
	espacio=30
	titulo_x, titulo_y=40,40
	pos_titulo=(titulo_x, titulo_y)
	opciones=[]
	pos_op=1


	def __init__(self, nombreMenu):
		self.nombreMenu = nombreMenu
		self.fuente = pygame.font.Font(None, 32)
		self.nop=1
		self.seleccion=0

	def abajo(self):
		self.nop+=1
		if self.nop > len(self.opciones):
			self.nop=1

	def arriba(self):
		self.nop-=1
		if self.nop <= 0:
			self.nop=len(self.opciones)


	def draw(self, pantalla):
		self.texto=self.fuente.render(self.nombreMenu,True,self.color)
		pantalla.blit(self.texto, self.pos_titulo)
		i=1
		for op in self.opciones:
			self.texto=self.fuente.render(op,True,self.color)
			pantalla.blit(self.texto, [self.titulo_x, self.titulo_y+(self.espacio*i)])
			if self.nop==i:
				pos=[self.titulo_x-30, self.titulo_y+12+(self.espacio*i)]
				pygame.draw.circle(pantalla, self.color, pos, 5, 0)
			else:
				pos=[self.titulo_x-30, self.titulo_y+12+(self.espacio*i)]
				pygame.draw.circle(pantalla, self.fondo, pos, 5, 0)
			i+=1
