import pygame

FPS = 60

class Video():

	def __init__(self, nombreVideo, nombreSonido, nombreSuperficie):
		self.nombreVideo = nombreVideo
		self.nombreSonido = nombreSonido
		self.nombreSuperficie = nombreSuperficie
	
	def reproducir(self):

		#pygame.init()
		pygame.mixer.music.load(self.nombreSonido)
		pygame.mixer.music.play()
		self.clock = pygame.time.Clock()
		self.movie = pygame.movie.Movie(self.nombreVideo)
		self.nombreSuperficie = pygame.display.set_mode(movie.get_size())
		self.movie_screen = pygame.Surface(movie.get_size()).convert()

		self.movie.set_display(movie_screen)
		self.movie.play()


		self.playing = True
		while playing:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.movie.stop()
					self.playing = False

			self.nombreSuperficie.blit(movie_screen,(0,0))
			pygame.display.update()
			self.clock.tick(FPS)
