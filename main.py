#import modules and libraries 

import pygame
import random
import string
from pygame.locals import *
from pygame import mixer
import pickle
from os import path
from time import sleep
import tkinter as tk
from PIL import ImageTk, Image
from Dialogue1 import dialogue


def dialogue2():

    # Defining what happens when user clicks the continue button
    def continue_clicked():
        root.destroy()

    # Create the main window & setting up tkinter program descriptions
    root = tk.Tk()
    root.title("Dialogue Box")

    # Set the window position and dimensions
    root.geometry("600x500")

    # Display text
    dialogue_text = "In this course, you will learn about Reward Programs, and its privacy risks on users."

    # Text properties
    dialogue_label = tk.Label(root, wraplength=500, font=("Arial", 14), text=dialogue_text)
    dialogue_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    # Create button and assign properties
    button = tk.Button(root, text="Continue", width=10, height=2, font=("Arial", 12), command=continue_clicked)
    button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    # Start the Tkinter event loop
    root.mainloop()





    '''
    NOTES:
    relx = x-coordinate ranging from 0.0 to 1.0 (so that means 0.5 is middle)
    rely = y-coordinate ranging from 0.0 to 1.0 (so that means 0.5 is middle)
    anchor options: n, ne, e, se, s, sw, w, nw, or center
    '''
def dialogue3():

    # Create the main window & setting up tkinter program descriptions
    root = tk.Tk()
    root.title("Dialogue Box")

    # Set the window position
    root.geometry("600x500")

    username = ""

    # Display text
    dialogue_text = "But before we continue...\n Please enter your username:"

    # Creating the dialogue text & properties
    dialogue_label = tk.Label(root, wraplength=580, font=("Arial", 14), text=dialogue_text)
    dialogue_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    # Create the entry box for username
    username_entry = tk.Entry(root, width=40, font=("Arial", 12))
    username_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    #~~~~~~~~~~~~~~Creating continue button to close dialogue so it can continue next~~~~~~~~~~~~~~#
    def close_dialogue():
        global username
        username = username_entry.get()
        root.destroy()
    # Create the continue button after every dialogue
    continue_button = tk.Button(root, text="Continue", width=10, height=2, font=("Arial", 12), command=close_dialogue)
    continue_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


    root.mainloop()

    # Displays username in console
    print(f"Username: {username}")

    usernametest = "Adwaittest"


    '''
    NOTES:
    relx = x-coordinate ranging from 0.0 to 1.0 (so that means 0.5 is middle)
    rely = y-coordinate ranging from 0.0 to 1.0 (so that means 0.5 is middle)
    anchor options: n, ne, e, se, s, sw, w, nw, or center
    '''
def dialogue4():

    # Defining what happens when user clicks the continue button
    def continue_clicked():
        root.destroy()

    # Setting descriptions of Tkinter program
    root = tk.Tk()
    root.title("Dialogue Box")

    # Set the window position and dimensions
    root.geometry("600x500")

    # Display text
    dialogue_text = "Rewards Programs offer great benefits, but they also come with many risks...\n\nHackers and scammers target accounts, selling them or stealing untraceable reward points. They use data breaches or send fake emails posing as the program.\n\nSo let's learn to protect ourselves, to stay informed, and to stay safe!"

    # Text properties
    dialogue_label = tk.Label(root, wraplength=530, font=("Arial", 14), text=dialogue_text)
    dialogue_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    #Create button and assign properties
    button = tk.Button(root, text="Continue", width=10, height=2, font=("Arial", 12), command=continue_clicked)
    button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    root.mainloop()





    '''
    NOTES:
    relx = x-coordinate ranging from 0.0 to 1.0 (so that means 0.5 is middle)
    rely = y-coordinate ranging from 0.0 to 1.0 (so that means 0.5 is middle)
    anchor options: n, ne, e, se, s, sw, w, nw, or center
    '''
def dialogue5():

    # Defining what happens when user clicks the continue button
    def continue_clicked():
        root.destroy()

    # Setting descriptions of Tkinter program
    root = tk.Tk()
    root.title("Dialogue Box")

    # Set the window position and dimensions
    root.geometry("600x500")

    # Display text
    dialogue_text = "Now, your mission is to beat the platformer level and collect the E-mail!\n Also.. watch out for HACKERS"

    # Text properties
    dialogue_label = tk.Label(root, wraplength=500, font=("Arial", 14), text=dialogue_text)
    dialogue_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    #Create button and assign properties
    button = tk.Button(root, text="Continue", width=10, height=2, font=("Arial", 12), command=continue_clicked)
    button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    root.mainloop()





    '''
    NOTES:
    relx = x-coordinate ranging from 0.0 to 1.0 (so that means 0.5 is middle)
    rely = y-coordinate ranging from 0.0 to 1.0 (so that means 0.5 is middle)
    anchor options: n, ne, e, se, s, sw, w, nw, or center
    '''
def dialogue6():

    # Setting descriptions of Tkinter program
    root = tk.Tk()
    root.title("Dialogue Box")

    # Set the window position and dimensions
    root.geometry("600x500")

    # Display text
    dialogue_text = "Congrats on sucessfully collecting the E-mail! Now let's go create a strong password to further protect ourself from such hackers..."

    # Text properties
    dialogue_label = tk.Label(root, wraplength=500, font=("Arial", 14), text=dialogue_text)
    dialogue_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)


    # Defining what happens when user clicks the continue button
    def continue_clicked():
        root.destroy()

    # Create button and assign properties
    button = tk.Button(root, text="Continue", width=10, height=2, font=("Arial", 12), command=continue_clicked)
    button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    root.mainloop()





    '''
    NOTES:
    relx = x-coordinate ranging from 0.0 to 1.0 (so that means 0.5 is middle)
    rely = y-coordinate ranging from 0.0 to 1.0 (so that means 0.5 is middle)
    anchor options: n, ne, e, se, s, sw, w, nw, or center
    '''
def dialogue7():

    # Setting descriptions of Tkinter program
    root = tk.Tk()
    root.title("Dialogue Box")

    # Set the window position and dimensions
    root.geometry("600x500")

    # Display text
    dialogue_text = "A strong password functions as an impenetrable wall, protecting your sensitive information from intrusive hackers...\n\nThe strength of your password is measured on its randomness and the inclusion of special characters.\n\nLet's use a password generator to generate an example password that you can use for your future benefit..."

    # Text properties
    dialogue_label = tk.Label(root, wraplength=500, font=("Arial", 14), text=dialogue_text)
    dialogue_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)


    # Defining what happens when user clicks the continue button
    def continue_clicked():
        root.destroy()

    # Create button and assign properties
    button = tk.Button(root, text="Continue", width=10, height=2, font=("Arial", 12), command=continue_clicked)
    button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    root.mainloop()





    '''
    NOTES:
    relx = x-coordinate ranging from 0.0 to 1.0 (so that means 0.5 is middle)
    rely = y-coordinate ranging from 0.0 to 1.0 (so that means 0.5 is middle)
    anchor options: n, ne, e, se, s, sw, w, nw, or center
    '''
def dialogue8():

    # Setting descriptions of Tkinter program
    root = tk.Tk()
    root.title("Dialogue Box")

    # Set the window position and dimensions
    root.geometry("600x500")

    # Display text
    dialogue_text = "Congrats on generating a strong and secure password!"

    # Text properties
    dialogue_label = tk.Label(root, wraplength=500, font=("Arial", 14), text=dialogue_text)
    dialogue_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)


    # Defining what happens when user clicks the continue button
    def continue_clicked():
        root.destroy()

    # Create button and assign properties
    button = tk.Button(root, text="Continue", width=10, height=2, font=("Arial", 12), command=continue_clicked)
    button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    root.mainloop()





    '''
    NOTES:
    relx = x-coordinate ranging from 0.0 to 1.0 (so that means 0.5 is middle)
    rely = y-coordinate ranging from 0.0 to 1.0 (so that means 0.5 is middle)
    anchor options: n, ne, e, se, s, sw, w, nw, or center
    '''
def dialogue9():

    root = tk.Tk()
    root.title("Dialogue Box")

    # Calculate the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the center coordinates of the screen
    center_x = int((screen_width - 800) / 2)
    center_y = int((screen_height - 600) / 2)

    # Set the window position and dimensions
    root.geometry(f"800x600")

    # Load and resize the images
    image1 = Image.open("H:\pyzo\CPT Dialogues\email1.png")
    image1 = image1.resize((300, 400), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(image1)

    image2 = Image.open("H:\pyzo\CPT Dialogues\email2.jpg")
    image2 = image2.resize((300, 400), Image.ANTIALIAS)
    image2 = ImageTk.PhotoImage(image2)

    # Create labels for the images
    label1 = tk.Label(root, image=image1)
    label1.place(relx=0.25, rely=0.3, anchor=tk.CENTER)

    label2 = tk.Label(root, image=image2)
    label2.place(relx=0.75, rely=0.3, anchor=tk.CENTER)

    # Create text labels below the images
    text1 = "Image 1 description"
    text_label1 = tk.Label(root, text=text1)
    text_label1.place(relx=0.25, rely=0.6, anchor=tk.CENTER)

    text2 = "Image 2 description"
    text_label2 = tk.Label(root, text=text2)
    text_label2.place(relx=0.75, rely=0.6, anchor=tk.CENTER)


    def continue_clicked():
        root.destroy()
    # Create the "Continue" button
    button = tk.Button(root, text="Continue", width=10, height=2, font=("Arial", 12), command=continue_clicked)
    button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    root.mainloop()
def dialogue10():

    root = tk.Tk()
    root.title("Dialogue Box")

    # Set the window position and dimensions
    root.geometry("1000x700")

    # Load and size the images
    image1 = Image.open("H:\pyzo\CPT Dialogues\images\email1.png")
    image1 = image1.resize((475, 350), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(image1)

    image2 = Image.open("H:\pyzo\CPT Dialogues\images\email2.jpg")
    image2 = image2.resize((400, 450), Image.ANTIALIAS)
    image2 = ImageTk.PhotoImage(image2)

    # Create labels for the images
    label1 = tk.Label(root, image=image1)
    label1.place(relx=0.3, rely=0.4, anchor=tk.CENTER)

    label2 = tk.Label(root, image=image2)
    label2.place(relx=0.75, rely=0.33, anchor=tk.CENTER)

    # Create text labels below the images
    top_text = "We can tell a E-mail is legit by checking\nthe email address and the format of the email\n For example:"
    top_text = tk.Label(root, font=("Arial", 14, "bold"), text=top_text)
    top_text.place(relx=0.3, rely=0.07, anchor=tk.CENTER)

    text1 = "This E-mail seems FAKE because the sender's email address doesn't belong to Costco, the logo is inaccurate, and the email is not associated with their company/website."
    text_label1 = tk.Label(root, font=("Arial", 12,), wraplength=450, text=text1)
    text_label1.place(relx=0.3, rely=0.7, anchor=tk.CENTER)

    text2 = "This email seems LEGIT as it has a more neat and professional email format, and the sender's email address is linked to their official website. (as seen near the bottom)\n\n It's important to be careful and check if the email is genuine before doing anything it asks you to do."
    text_label2 = tk.Label(root, font=("Arial", 12,), wraplength=400, text=text2)
    text_label2.place(relx=0.75, rely=0.75, anchor=tk.CENTER)

    # Continue button command
    def continue_clicked():
        root.destroy()
    # Create the "Continue" button
    button = tk.Button(root, text="Continue", width=10, height=2, font=("Arial", 12), command=continue_clicked)
    button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    root.mainloop()
def certificate_dialogue():
    def close_dialogue():
        root.destroy()

    root = tk.Tk()
    root.title("Certificate")


    # Set the window position and dimensions
    root.geometry(f"800x400")


    # Create the top text label
    top_text_label = tk.Label(root, text="Congratulations!", font=("Arial", 24, "bold"))
    top_text_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    # Create the middle text label for username
    top_text_label = tk.Label(root, text="Congrats", font=("Arial", 20, "underline"))
    top_text_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Create the bottom text label
    bottom_text_label = tk.Label(root, text="for sucessfully completing this program", font=("Arial", 18))
    bottom_text_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    # Create the "Close" button
    close_button = tk.Button(root, text="Close", width=10, height=2, font=("Arial", 12), command=close_dialogue)
    close_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    root.mainloop()
def platformer():

	pygame.mixer.pre_init(44100, -16, 2, 512)
	mixer.init()
	pygame.init()

	clock = pygame.time.Clock()
	fps = 60

	screen_width = 1000
	screen_height = 1000

	screen = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption('Platformer')


	#define font
	font = pygame.font.SysFont('Bauhaus 93', 70)
	font_score = pygame.font.SysFont('Bauhaus 93', 30)


	#define game variables
	tile_size = 50
	game_over = 0
	main_menu = True
	level = 3
	max_levels = 7
	score = 0


	#define colours
	white = (255, 255, 255)
	blue = (0, 0, 255)


	#load images
	sun_img = pygame.image.load('img/sun.png')
	bg_img = pygame.image.load('img/sky.png')
	restart_img = pygame.image.load('img/restart_btn.png')
	start_img = pygame.image.load('img/start_btn.png')
	exit_img = pygame.image.load('img/exit_btn.png')

	#load sounds
	pygame.mixer.music.load('img/music.wav')
	pygame.mixer.music.play(-1, 0.0, 5000)
	coin_fx = pygame.mixer.Sound('img/coin.wav')
	coin_fx.set_volume(0.5)
	jump_fx = pygame.mixer.Sound('img/jump.wav')
	jump_fx.set_volume(0.5)
	game_over_fx = pygame.mixer.Sound('img/game_over.wav')
	game_over_fx.set_volume(0.5)


	def draw_text(text, font, text_col, x, y):
		img = font.render(text, True, text_col)
		screen.blit(img, (x, y))


	#function to reset level     
	def reset_level(level):
		player.reset(100, screen_height - 130)
		blob_group.empty()
		platform_group.empty()
		coin_group.empty()
		lava_group.empty()
		exit_group.empty()

		#load in level data and create world
		if path.exists(f'level{level}_data'):
			pickle_in = open(f'level{level}_data', 'rb')
			world_data = pickle.load(pickle_in)
		world = World(world_data)
		#create dummy coin for showing the score
		score_coin = Coin(tile_size // 2, tile_size // 2)
		coin_group.add(score_coin)
		return world


	class Button():
		def __init__(self, x, y, image):
			self.image = image
			self.rect = self.image.get_rect()
			self.rect.x = x
			self.rect.y = y
			self.clicked = False

		def draw(self):
			action = False

			#get mouse position
			pos = pygame.mouse.get_pos()

			#check mouseover and clicked conditions
			if self.rect.collidepoint(pos):
				if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
					action = True
					self.clicked = True

			if pygame.mouse.get_pressed()[0] == 0:
				self.clicked = False


			#draw button
			screen.blit(self.image, self.rect)

			return action


	class Player():
		def __init__(self, x, y):
			self.reset(x, y)

		def update(self, game_over):
			dx = 0
			dy = 0
			walk_cooldown = 5
			col_thresh = 20

			if game_over == 0:
				#get keypresses
				key = pygame.key.get_pressed()
				if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
					jump_fx.play()
					self.vel_y = -15
					self.jumped = True
				if key[pygame.K_SPACE] == False:
					self.jumped = False
				if key[pygame.K_LEFT]:
					dx -= 5
					self.counter += 1
					self.direction = -1
				if key[pygame.K_RIGHT]:
					dx += 5
					self.counter += 1
					self.direction = 1
				if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
					self.counter = 0
					self.index = 0
					if self.direction == 1:
						self.image = self.images_right[self.index]
					if self.direction == -1:
						self.image = self.images_left[self.index]


				#handle animation
				if self.counter > walk_cooldown:
					self.counter = 0	
					self.index += 1
					if self.index >= len(self.images_right):
						self.index = 0
					if self.direction == 1:
						self.image = self.images_right[self.index]
					if self.direction == -1:
						self.image = self.images_left[self.index]


				#add gravity
				self.vel_y += 1
				if self.vel_y > 10:
					self.vel_y = 10
				dy += self.vel_y

				#check for collision
				self.in_air = True
				for tile in world.tile_list:
					#check for collision in x direction
					if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
						dx = 0
					#check for collision in y direction
					if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
						#check if below the ground i.e. jumping
						if self.vel_y < 0:
							dy = tile[1].bottom - self.rect.top
							self.vel_y = 0
						#check if above the ground i.e. falling
						elif self.vel_y >= 0:
							dy = tile[1].top - self.rect.bottom
							self.vel_y = 0
							self.in_air = False


				#check for collision with enemies
				if pygame.sprite.spritecollide(self, blob_group, False):
					game_over = -1
					game_over_fx.play()

				#check for collision with lava
				if pygame.sprite.spritecollide(self, lava_group, False):
					game_over = -1
					game_over_fx.play()

				#check for collision with exit
				if pygame.sprite.spritecollide(self, exit_group, False):
					game_over = 1


				#check for collision with platforms
				for platform in platform_group:
					#collision in the x direction
					if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
						dx = 0
					#collision in the y direction
					if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
						#check if below platform
						if abs((self.rect.top + dy) - platform.rect.bottom) < col_thresh:
							self.vel_y = 0
							dy = platform.rect.bottom - self.rect.top
						#check if above platform
						elif abs((self.rect.bottom + dy) - platform.rect.top) < col_thresh:
							self.rect.bottom = platform.rect.top - 1
							self.in_air = False
							dy = 0
						#move sideways with the platform
						if platform.move_x != 0:
							self.rect.x += platform.move_direction


				#update player coordinates
				self.rect.x += dx
				self.rect.y += dy


			elif game_over == -1:
				self.image = self.dead_image
				draw_text('GAME OVER!', font, white, (screen_width // 2) - 200, screen_height // 2)
				if self.rect.y > 200:
					self.rect.y -= 5

			#draw player onto screen
			screen.blit(self.image, self.rect)

			return game_over


		def reset(self, x, y):
			self.images_right = []
			self.images_left = []
			self.index = 0
			self.counter = 0
			for num in range(1, 5):
				img_right = pygame.image.load(f'img/guy{num}.png')
				img_right = pygame.transform.scale(img_right, (40, 80))
				img_left = pygame.transform.flip(img_right, True, False)
				self.images_right.append(img_right)
				self.images_left.append(img_left)
			self.dead_image = pygame.image.load('img/ghost.png')
			self.image = self.images_right[self.index]
			self.rect = self.image.get_rect()
			self.rect.x = x
			self.rect.y = y
			self.width = self.image.get_width()
			self.height = self.image.get_height()
			self.vel_y = 0
			self.jumped = False
			self.direction = 0
			self.in_air = True



	class World():
		def __init__(self, data):
			self.tile_list = []

			#load images
			dirt_img = pygame.image.load('img/dirt.png')
			grass_img = pygame.image.load('img/grass.png')

			row_count = 0
			for row in data:
				col_count = 0
				for tile in row:
					if tile == 1:
						img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
						img_rect = img.get_rect()
						img_rect.x = col_count * tile_size
						img_rect.y = row_count * tile_size
						tile = (img, img_rect)
						self.tile_list.append(tile)
					if tile == 2:
						img = pygame.transform.scale(grass_img, (tile_size, tile_size))
						img_rect = img.get_rect()
						img_rect.x = col_count * tile_size
						img_rect.y = row_count * tile_size
						tile = (img, img_rect)
						self.tile_list.append(tile)
					if tile == 3:
						blob = Enemy(col_count * tile_size, row_count * tile_size + 15)
						blob_group.add(blob)
					if tile == 4:
						platform = Platform(col_count * tile_size, row_count * tile_size, 1, 0)
						platform_group.add(platform)
					if tile == 5:
						platform = Platform(col_count * tile_size, row_count * tile_size, 0, 1)
						platform_group.add(platform)
					if tile == 6:
						lava = Lava(col_count * tile_size, row_count * tile_size + (tile_size // 2))
						lava_group.add(lava)
					if tile == 7:
						coin = Coin(col_count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2))
						coin_group.add(coin)
					if tile == 8:
						exit = Exit(col_count * tile_size, row_count * tile_size - (tile_size // 2))
						exit_group.add(exit)
					col_count += 1
				row_count += 1


		def draw(self):
			for tile in self.tile_list:
				screen.blit(tile[0], tile[1])



	class Enemy(pygame.sprite.Sprite):
		def __init__(self, x, y):
			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.image.load('img/blob.png')
			self.rect = self.image.get_rect()
			self.rect.x = x
			self.rect.y = y
			self.move_direction = 1
			self.move_counter = 0

		def update(self):
			self.rect.x += self.move_direction
			self.move_counter += 1
			if abs(self.move_counter) > 50:
				self.move_direction *= -1
				self.move_counter *= -1


	class Platform(pygame.sprite.Sprite):
		def __init__(self, x, y, move_x, move_y):
			pygame.sprite.Sprite.__init__(self)
			img = pygame.image.load('img/platform.png')
			self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
			self.rect = self.image.get_rect()
			self.rect.x = x
			self.rect.y = y
			self.move_counter = 0
			self.move_direction = 1
			self.move_x = move_x
			self.move_y = move_y


		def update(self):
			self.rect.x += self.move_direction * self.move_x
			self.rect.y += self.move_direction * self.move_y
			self.move_counter += 1
			if abs(self.move_counter) > 50:
				self.move_direction *= -1
				self.move_counter *= -1





	class Lava(pygame.sprite.Sprite):
		def __init__(self, x, y):
			pygame.sprite.Sprite.__init__(self)
			img = pygame.image.load('img/lava.png')
			self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
			self.rect = self.image.get_rect()
			self.rect.x = x
			self.rect.y = y


	class Coin(pygame.sprite.Sprite):
		def __init__(self, x, y):
			pygame.sprite.Sprite.__init__(self)
			img = pygame.image.load('img/coin.png')
			self.image = pygame.transform.scale(img, (tile_size // 2, tile_size // 2))
			self.rect = self.image.get_rect()
			self.rect.center = (x, y)


	class Exit(pygame.sprite.Sprite):
		def __init__(self, x, y):
			pygame.sprite.Sprite.__init__(self)
			img = pygame.image.load('img/exit.png')
			self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))
			self.rect = self.image.get_rect()
			self.rect.x = x
			self.rect.y = y



	player = Player(100, screen_height - 130)

	blob_group = pygame.sprite.Group()
	platform_group = pygame.sprite.Group()
	lava_group = pygame.sprite.Group()
	coin_group = pygame.sprite.Group()
	exit_group = pygame.sprite.Group()

	#create dummy coin for showing the score
	score_coin = Coin(tile_size // 2, tile_size // 2)
	coin_group.add(score_coin)

	#load in level data and create world
	if path.exists(f'level{level}_data'):
		pickle_in = open(f'level{level}_data', 'rb')
		world_data = pickle.load(pickle_in)
	world = World(world_data)


	#create buttons
	restart_button = Button(screen_width // 2 - 50, screen_height // 2 + 100, restart_img)
	start_button = Button(screen_width // 2 - 350, screen_height // 2, start_img)
	exit_button = Button(screen_width // 2 + 150, screen_height // 2, exit_img)


	run = True
	while run:

		clock.tick(fps)

		screen.blit(bg_img, (0, 0))
		screen.blit(sun_img, (100, 100))

		if main_menu == True:
			if exit_button.draw():
				run = False
			if start_button.draw():
				main_menu = False
		else:
			world.draw()

			if game_over == 0:
				blob_group.update()
				platform_group.update()
				#update score
				#check if a coin has been collected
				if pygame.sprite.spritecollide(player, coin_group, True):
					score += 1
					coin_fx.play()
				draw_text('X ' + str(score), font_score, white, tile_size - 10, 10)
			
			blob_group.draw(screen)
			platform_group.draw(screen)
			lava_group.draw(screen)
			coin_group.draw(screen)
			exit_group.draw(screen)

			game_over = player.update(game_over)

			#if player has died
			if game_over == -1:
				if restart_button.draw():
					world_data = []
					world = reset_level(level)
					game_over = 0
					score = 0

			#if player has completed the level
			if game_over == 1:
				#reset game and go to next level
				level += 1
				if level <= max_levels:
					#reset level
					world_data = []
					world = reset_level(level)
					game_over = 0
				else:
					draw_text('YOU WIN!', font, white, (screen_width // 2) - 140, screen_height // 2)
					pygame.quit()
                    

		pygame.display.update()

	pygame.quit()


dialogue()

dialogue2()

dialogue3()

dialogue4()

dialogue5()

platformer()

dialogue6()

dialogue7()

dialogue8()

dialogue9()

dialogue10()

certificate_dialogue()