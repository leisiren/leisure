import pygame
import time
import random
from pygame.locals import *
class HeroPlane:
	def __init__(self,screen):
		self.x = 200
		self.y = 410
		self.screen = screen
		self.image = pygame.image.load("./feiji/hero.gif").convert()
		self.danyaolist = []
		self.imagenum = 0
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))
		tempremove = []
		for temp in self.danyaolist:
			temp.display()
			temp.move()
			if temp.y < 2:
				tempremove.append(temp)
		for i in tempremove:
			self.danyaolist.remove(i)  
	def moveright(self):
		if self.x <= 375:
			self.x += 9
	def moveleft(self):
		if self.x >= 5:
			self.x -= 9
	def shoot(self):
		zidan = ZiDan(self.x,self.y,self.screen)
		self.danyaolist.append(zidan)
class EnemyPlane:
	def __init__(self,screen):
		self.x = 200
		self.y = 0 
		self.screen = screen
		self.image = pygame.image.load("./feiji/enemy-1.gif").convert()
		self.danyaolist = []
		self.diretion = "right"
		self.imagenum = 0
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))
		tempremove = []
		self.shoot()
		self.move()
		for temp in self.danyaolist:
			temp.display()
			temp.move()
			if temp.y > 525:
				tempremove.append(temp)
		for i in tempremove:
			self.danyaolist.remove(i)    
	def move(self):
		if self.diretion == "right":
			self.x += 1
			if self.x > 435:
				self.diretion = "left"
		elif self.diretion == "left":
			self.x -= 1
			if self.x < 0:
				self.diretion = "right"

	def shoot(self):
		num = random.randint(0,50)
		if num == 8:
			enemyzidan = EnemyZiDan(self.x,self.y,self.screen)
			self.danyaolist.append(enemyzidan)
	
class ZiDan:
	def __init__(self,x,y,screen):
		self.x = x + 40
		self.y = y - 20
		self.image = pygame.image.load("./feiji/bullet-3.gif").convert()
		self.screen = screen
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))
	def move(self):
		self.y -= 1
class EnemyZiDan:
	def __init__(self,x,y,screen):
		self.x = x + 22
		self.y = y + 30
		self.image = pygame.image.load("./feiji/bullet-1.gif").convert()
		self.screen = screen
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))
	def move(self):
		self.y += 2
def dazhong(heroplane,enemyplane):
	remove_enemybullet = []
	remove_herobullet = []
	if heroplane and enemyplane:

		for herobullet in heroplane.danyaolist:
			if herobullet.x < enemyplane.x + 40 - 3 and herobullet.x > enemyplane.x and herobullet.y < enemyplane.y + 40 and herobullet.y >enemyplane.y:
				enemyplane.imagenum += 1
	
		for enemybullet in enemyplane.danyaolist:
			if enemybullet.x < heroplane.x + 90 - 3 and enemybullet.x > heroplane.x and enemybullet.y < heroplane.y + 90 and enemybullet.y >heroplane.y:
				heroplane.imagenum += 1
		for herobullet in heroplane.danyaolist:
			for enemybullet in enemyplane.danyaolist:
				
				if herobullet.x >= enemybullet.x - 10 and herobullet.x <= enemybullet.x +15 and herobullet.y >=enemybullet.y - 20 and herobullet.y <= enemybullet.y +30:
					remove_enemybullet.append(enemybullet)
					remove_herobullet.append(herobullet)
		if remove_enemybullet:
			for temp in remove_enemybullet:
				enemyplane.danyaolist.remove(temp)
		for temp in remove_herobullet:
			heroplane.danyaolist.remove(temp)

if __name__ == "__main__":

	screen = pygame.display.set_mode((480,560),0,32)
	bgImageFile = "./feiji/background.png"
	background = pygame.image.load(bgImageFile).convert() 
	heroplane = HeroPlane(screen)
	enemyplane = EnemyPlane(screen)

	while True:
		screen.blit(background,(0,0))
		
		if enemyplane:
			enemyplane.display()
			dazhong(heroplane,enemyplane)
			if enemyplane.imagenum >= 12:
				enemyplane = None
				
			elif enemyplane.imagenum >= 9:
				enemyplane.image = pygame.image.load("./feiji/enemy0_down4.png").convert()
			elif enemyplane.imagenum >= 6:
				enemyplane.image = pygame.image.load("./feiji/enemy0_down3.png").convert()
			elif enemyplane.imagenum >= 4:
				enemyplane.image = pygame.image.load("./feiji/enemy0_down2.png").convert()
			elif enemyplane.imagenum >= 1:
				enemyplane.image = pygame.image.load("./feiji/enemy0_down1.png").convert()
		else:

			if random.randint(0,150) == 18:
				enemyplane = EnemyPlane(screen)
		if heroplane:
			heroplane.display()
			dazhong(heroplane,enemyplane)
			if heroplane.imagenum >= 20:
				heroplane = None
			elif heroplane.imagenum >= 15:
				heroplane.image = pygame.image.load("./feiji/hero_blowup_n4.png").convert()
			elif heroplane.imagenum >= 8:
				heroplane.image = pygame.image.load("./feiji/hero_blowup_n3.png").convert()
			elif heroplane.imagenum >= 4:
				heroplane.image = pygame.image.load("./feiji/hero_blowup_n2.png").convert()
			elif heroplane.imagenum >= 2:
				heroplane.image = pygame.image.load("./feiji/hero_blowup_n1.png").convert()
		else:

			if random.randint(0,100) == 88:
				heroplane = HeroPlane(screen)
		
		for event in pygame.event.get():
			if event.type == QUIT:
				print("exit")
				exit()
			elif event.type == KEYDOWN:
				if event.key == K_a or event.key == K_LEFT:
					print("left")
					if heroplane:
						heroplane.moveleft()
				elif event.key == K_d or event.key == K_RIGHT:
					print("rihgt")
					if heroplane:
						heroplane.moveright()
				elif event.key == K_SPACE:
					print("space")
					if heroplane:
						heroplane.shoot()
		time.sleep(0.01)
		pygame.display.update()

