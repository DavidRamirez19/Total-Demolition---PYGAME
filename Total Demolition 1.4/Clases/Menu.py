import pygame

# Colores
#NEGRO   = (   0,   0,   0)
#BLANCO    = ( 255, 255, 255)
#AZUL     = (   0,   0, 255)
#ROJO      = ( 255,   0,   0)
#VERDE    = (   0, 255,   0)

# Dimensiones pantalla
#ANCHO  = 300
#ALTO = 300

class Menu():
	
	#fondo=NEGRO
	#color=BLANCO
	espacio=50
	titulo_x, titulo_y=100,100
	pos_titulo=(titulo_x, titulo_y)
	opciones=[]
	opciones2=[]
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

	def draw(self, pantalla, cursor):
		nombreM=pygame.image.load(self.nombreMenu)
		pantalla.blit(nombreM, self.pos_titulo)
		self.cursor = cursor
		select = pygame.image.load(self.cursor)
		i=1
		
		for op in self.opciones:
			imagenCargar = pygame.image.load(op)
			pantalla.blit(imagenCargar, [self.titulo_x, self.titulo_y+(self.espacio*i)])
			#pygame.display.flip()
			if self.nop==i:
				pos=[self.titulo_x-30, self.titulo_y+12+(self.espacio*i)]
				pantalla.blit(select, (pos))
				imagenCargar2 = pygame.image.load(op+".png")
				pantalla.blit(imagenCargar2, [self.titulo_x, self.titulo_y+(self.espacio*i)])
				pygame.display.flip()
				
			i+=1
