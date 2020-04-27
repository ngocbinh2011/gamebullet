import pygame 
import random
pygame.init()

FPS=60
FONT = pygame.font.SysFont(None, 35)
font_toturial = pygame.font.SysFont(None, 20)
font_die = pygame.font.SysFont(None, 40)
Font_start = pygame.font.SysFont(None, 45)
font_damage = pygame.font.SysFont(None, 70)
pygame.display.set_caption("Love yourself")
# image của player khi đi bên phải
walk_right=[pygame.image.load(r"R1.png"), pygame.image.load(r"R2.png"), pygame.image.load(r"R3.png"),\
pygame.image.load(r"R4.png"), pygame.image.load(r"R5.png"), pygame.image.load(r"R6.png"), pygame.image.load(r"R7.png"),\
pygame.image.load(r"R8.png"),pygame.image.load(r"R9.png")]
# trái
walk_left =[pygame.image.load(r"L1.png"), pygame.image.load(r"L2.png"), pygame.image.load(r"L3.png"),\
pygame.image.load(r"L4.png"), pygame.image.load(r"L5.png"), pygame.image.load(r"L6.png"), pygame.image.load(r"L7.png"),\
pygame.image.load(r"L8.png"),pygame.image.load(r"L9.png")]
#image player khi đứng
char = pygame.image.load(r"standing.png")
#background
bg = pygame.image.load(r"bg.jpg")
# image phụ
up_img = pygame.image.load("up.png")
down_img = pygame.image.load("down.png")
left_img = pygame.image.load("left.png")
right_img = pygame.image.load("right.png")
dog_hello = pygame.image.load("doghello.png")
# sound game
background_sound = pygame.mixer.Sound("backgroundmusic.wav")
hit_sound = pygame.mixer.Sound("hit.wav")
bullet_sound = pygame.mixer.Sound("bullet.wav")
background_sound.play()
music_check = True

#window game
game_start = False
display_width = 800
display_height = 450
game_display = pygame.display.set_mode([display_width, display_height])
pygame.display.set_caption("CODE change my life!")
black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
blue = [0, 0, 255]
clock = pygame.time.Clock()
score = 0
# chua dan ban ra
bullets = []

class player:
	def __init__(self, x, y, x_change, y_change, player_width, player_height, value_change, health,\
				right_ckeck_player, left_check_player, step_check_player, step_player,\
				fps_player, walk_count, stand_check_player):
		self.x = x
		self.y = y
		self.x_change = x_change
		self.y_change = y_change
		self.player_width = player_width
		self.player_height = player_height
		self.value_change = value_change
		self.health = health
		self.right_ckeck_player = right_ckeck_player
		self.left_check_player = left_check_player
		self.step_check_player = step_check_player
		self.step_player = step_player
		self.fps_player = fps_player
		self.walk_count = walk_count
		self.stand_check_player = stand_check_player
	# điều khiển player
	def move_player(self):
		if self.walk_count > self.fps_player:
			self.walk_count = 0
		if self.stand_check_player:
			if self.right_ckeck_player:
				game_display.blit(walk_right[0], [self.x, self.y])
			elif self.left_check_player:
				game_display.blit(walk_left[0], [self.x, self.y])
			else:
				game_display.blit(char, [self.x, self.y])
		elif self.left_check_player:
			# 1 picture = 4 frame(khung hinh)
			game_display.blit(walk_left[self.walk_count//4], [self.x, self.y])
			self.walk_count +=1	
		elif self.right_ckeck_player:
			game_display.blit(walk_right[self.walk_count//4], [self.x, self.y])
			self.walk_count +=1 

# class đạn
class object_bullet:
	def __init__(self, x_bullet, y_bullet, radius, speed_change, check_space):
		self.x_bullet = x_bullet
		self.y_bullet = y_bullet
		self.radius = radius
		self.speed_change = speed_change
		self.check_space = check_space
	def draw_bullet(self):
		pygame.draw.circle(game_display, red, [self.x_bullet, self.y_bullet], self.radius)

# class enemy
class enemy:
	enemy_left = [pygame.image.load("L1E.png"), pygame.image.load("L2E.png"), pygame.image.load("L3E.png"),\
	 			pygame.image.load("L4E.png"), pygame.image.load("L5E.png"), pygame.image.load("L6E.png"),\
	 			pygame.image.load("L7E.png"), pygame.image.load("L8E.png"), pygame.image.load("L9E.png"),\
	 			pygame.image.load("L10E.png"), pygame.image.load("L11E.png")]
	enemy_right = [pygame.image.load("R1E.png"), pygame.image.load("R2E.png"), pygame.image.load("R3E.png"),\
	 			pygame.image.load("R4E.png"), pygame.image.load("R5E.png"), pygame.image.load("R6E.png"),\
	 			pygame.image.load("R7E.png"), pygame.image.load("R8E.png"), pygame.image.load("R9E.png"),\
	 			pygame.image.load("R10E.png"), pygame.image.load("R11E.png")]

	def __init__(self, x_enemy, y_enemy, width_enemy, height_enemy,\
				 start_enemy, end_enemy, fps_enemy, walk_enemy, right_check_enemy, left_check_enemy,\
				  speed_enemy, blood_enemy):
		self.x_enemy = x_enemy
		self.y_enemy = y_enemy
		self.speed_enemy = speed_enemy
		self.width_enemy = width_enemy
		self.height_enemy = height_enemy
		self.start_enemy = start_enemy
		self.end_enemy = end_enemy
		self.fps_enemy = fps_enemy
		self.walk_enemy = walk_enemy
		self.right_check_enemy = right_check_enemy
		self.left_check_enemy = left_check_enemy
		self.blood_enemy = blood_enemy
	def draw_enemy(self):
		pygame.draw.rect(game_display, black, [self.x_enemy+10, self.y_enemy-10, 50, 6])
		pygame.draw.rect(game_display, red, [self.x_enemy+10, self.y_enemy-10, self.blood_enemy, 6])
		if self.walk_enemy > self.fps_enemy:
			self.walk_enemy = 0
		if self.right_check_enemy:
			self.x_enemy += self.speed_enemy
			game_display.blit(self.enemy_right[self.walk_enemy//3], [self.x_enemy, self.y_enemy])
			self.walk_enemy += 1
		if self.left_check_enemy:
			self.x_enemy -= self.speed_enemy
			game_display.blit(self.enemy_left[self.walk_enemy//3], [self.x_enemy, self.y_enemy])
			self.walk_enemy += 1
	#di chuyển enemy
	def move_enemy(self):
		if self.start_enemy <= display_width // 2:
			self.right_check_enemy = True
			self.left_check_enemy = False
			#đổi chỗ start end khi x_enemy=end
			if self.x_enemy >= self.end_enemy:
				c = self.start_enemy
				self.start_enemy = self.end_enemy
				self.end_enemy = c
		else:
			self.left_check_enemy = True
			self.right_check_enemy = False
			if self.x_enemy == self.end_enemy:
				c = self.start_enemy
				self.start_enemy = self.end_enemy
				self.end_enemy = c


#ve dan
def bullet_screen():
	for BULLET in bullets:
		BULLET.draw_bullet()
		if one_enemy.blood_enemy > 10:
			if music_check == True:
				bullet_sound.play()
		pygame.display.update()

#vẽ background
def background():
	game_display.blit(bg, [0,0])


#vẽ nhân vật + di chuyển:
def draw_move_player():
	pygame.draw.rect(game_display, black, [human.x+5, human.y -5, 60, 5])
	pygame.draw.rect(game_display, blue, [human.x+5, human.y-5, human.health, 5])
	human.move_player()

#ve enemy
def draw_anemy_display():
	one_enemy.move_enemy()
	one_enemy.draw_enemy()
	pygame.display.update()

# điểm
def score_count():
	text = FONT.render("score: {}".format(score), True, black)
	game_display.blit(text, [display_width-130,30])
	pygame.display.update()

# check enemy
def enemy_die():
	global one_enemy
	if one_enemy.blood_enemy >0:
		one_enemy.blood_enemy -= 2
	else:
		# x_enemy_rad = random.randrange(0,display_width-50)
		if music_check == True:
			hit_sound.play()
		pygame.display.update()
		one_enemy= enemy(0, display_height-70,  50, 50, 0, 500, 30, 0, False, False, 7, 50)
		draw_anemy_display()

# điều khiển heath player
def heath_player():
	text_heath = font_damage.render("-5", True, red)
	global human, game_countinue, run
	c = 3*human.player_width //4
	if one_enemy.x_enemy >= human.x and one_enemy.x_enemy <= human.x + human.player_width//4 or\
	one_enemy.x_enemy >= human.x + c and one_enemy.x_enemy <= human.x + human.player_width:
		if one_enemy.y_enemy >= human.y and one_enemy.y_enemy <= human.y +human.player_height:
			if human.health >=5:
				human.health -= 5
				game_display.blit(text_heath, [200,100])
				pygame.time.delay(15)
			else:
				game_countinue = True
				run = False
	pygame.display.update()

# xử lí khi thua game
def lose_game():
	game_display.fill(black)
	text_die1 = font_die.render("YOU LOSE!", True, white)
	text_die2 = font_die.render("Press C to restart and Q to quit", True, white)
	game_display.blit(text_die1, [display_width//2-30, display_height//2-10])
	game_display.blit(text_die2, [display_width//5, display_height//2+15])
	pygame.display.update()

# hướng dẫn game
def tutorial_game():
	press_space = font_toturial.render("SPACE to shoot", True,  blue)
	press_right = font_toturial.render("to right", True, blue)
	press_left = font_toturial.render("to left", True, blue)
	press_up = font_toturial.render("to jump", True, blue)
	text_music = font_toturial.render("Press M to pause/unpause music", True, blue)
	game_display.blit(text_music, [display_width//3, display_height//2-20])
	game_display.blit(press_space, [display_width//3, display_height//2])
	game_display.blit(right_img, [display_width//3, display_height//2+ 25])
	game_display.blit(press_right, [display_width//3 +35, display_height//2 +30])
	game_display.blit(left_img, [display_width//3, display_height//2+ 50])
	game_display.blit(press_left, [display_width//3 +35, display_height//2 +55])
	game_display.blit(up_img, [display_width//3, display_height//2+ 75])
	game_display.blit(press_up, [display_width//3 +35, display_height//2 +80])

# interface game
def start():
	global game_start, game_out
	text_start = Font_start.render("Welcome to my game!press any key to start", True, white)
	while not game_start:
		game_display.blit(text_start, [display_width//8, display_height//3])
		game_display.blit(dog_hello, [display_width//3+100, display_height//2+35])
		tutorial_game()
		pygame.display.update()
		for ev in pygame.event.get():
			if ev.type == pygame.QUIT:
				game_out = True
				game_start = True
			if ev.type == pygame.KEYDOWN:
				game_start = True

# control music
def music_control():
	global music_check
	keys = pygame.key.get_pressed()
	if keys[pygame.K_m]:
		pygame.time.delay(100)
		music_check = not music_check
		if music_check:
			pygame.mixer.unpause()
		else:
			pygame.mixer.pause()


game_out = False
# game system
def game_loop():
	global score, game_out, run, game_countinue, human, one_enemy
	score = 0
	human = player(300, 370, 0, 0, 50, 60, 10, 60, False, False, False, 7, 32, 0, True)
	one_enemy= enemy(0, display_height-70,  50, 50, 0, 500, 30, 0, False, False, 7, 50)
	run = True
	game_countinue = False
	# vòng lặp game
	while not game_out:
		# xử lí thua game
		while game_countinue:
			lose_game()
			for evt in pygame.event.get():
				if evt.type == pygame.QUIT:
					game_countinue = False
					game_out = True
				if evt.type == pygame.KEYDOWN:
					if evt.key == pygame.K_c:
						game_loop()
					if evt.key == pygame.K_q:
						game_countinue = False
						game_out = True

		# vòng lặp chính game
		while run:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
					game_out = True
				# if event.type == pygame.KEYDOWN:
				# 	music_control(event.type)

			for bul in bullets:
				if bul.x_bullet >= one_enemy.x_enemy and bul.x_bullet <= one_enemy.x_enemy + one_enemy.width_enemy\
					and bul.y_bullet > one_enemy.y_enemy and bul.y_bullet <= one_enemy.y_enemy + one_enemy.height_enemy:
					bullets.remove(bullets[bullets.index(bul)])
					score += 1
					enemy_die()
				elif bul.x_bullet >= 0 and bul.x_bullet <= display_width:
					bul.x_bullet += bul.speed_change
				else:
					#remove vien dan qua gioi han
					bullets.remove(bullets[bullets.index(bul)])

			#player
			KEY = pygame.key.get_pressed()
			if KEY[pygame.K_SPACE]:
				if len(bullets) < 5 :
					if human.left_check_player:
						speed = -20
					elif human.right_ckeck_player:
						speed = 20
					else:
						if human.stand_check_player == True:
							speed = 20
					#chèn 1 object vào mảng trống
					bullets.append(object_bullet(human.x + 30, human.y + 40,  5, speed, False))				
			if KEY[pygame.K_RIGHT] and human.x + human.player_width < display_width:
				human.right_ckeck_player = True
				human.left_check_player = False
				human.stand_check_player = False
				human.x += human.value_change
			elif KEY[pygame.K_LEFT] and human.x >= 0:
				human.left_check_player = True
				human.right_ckeck_player = False
				human.stand_check_player = False
				human.x += -human.value_change
			else:
				human.stand_check_player = True
			if not(human.step_check_player):
				# if KEY[pygame.K_UP] and human.y >= 0:
				# 	human.y += -human.value_change
				# if KEY[pygame.K_DOWN] and human.y + human.player_height < display_height:
				# 	human.y += human.value_change
				if KEY[pygame.K_UP]:
					human.right_ckeck_player = False
					human.step_check_player = True
					human.left_check_player = False
			else:
				if human.step_player >= -7:
					jump = 1
					if human.step_player < 0:
						jump = -1
					human.y -= (human.step_player**2) * jump
					human.step_player -= 1
				else:
					human.step_player = 7
					human.step_check_player = False

			#game
			background()
			draw_move_player()
			draw_anemy_display()
			heath_player()
			bullet_screen()
			score_count()
			music_control()
			pygame.time.delay(50)
			clock.tick(FPS)
			pygame.display.update()

start()
game_loop()
pygame.quit()