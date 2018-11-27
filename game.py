# Jonathan Eman (jwe6mr) and Luke Jones (ltj7hha)

'''
We are creating a version of the popular phone app Temple Run. Our version will be two dimensional from a side view. The player will move along a track and run for as long as possible.
'''


# ----- we will save the high score of the player, which will be displayed during future games
# ---- this high score will be saved in a text file

import pygame
import gamebox
import random
camera = gamebox.Camera(800,600)
game_on = False
game_speed = 10
speed = 0

score = 0  # the score is determined by the amount of time that has elapsed, as well as the    number of coins collected

# ------ introduce player, background, enemies, health meter, floor speed etc.

floor = gamebox.from_color(400, 500, "dark red", 1200, 20)

player = gamebox.from_color(400, 440, "dark green", 100, 100)
# background =
# enemy_1 =  # Chase after the player. May randomly jump in front of player and force player to move around it in order for game to continue.
# enemy_2 =
# health_meter =  # Health meter starts half full. Health decreases gradually as time progresses, and significantly if the player fails to dodge an obstacle. Player must collect coins to increase health. If health meter becomes full, player receives a superpower (ex: invincibility, coin magnet, superspeed). If health meter falls to 0, player stops moving and is killed by enemies that are chasing after it.
# scoreboard =
# coin_counter =  # Coins will be randomly placed and user must use keyboard to move and collect them.
# Obstacles =  # we will have a list of different obstacles (gamebox boxes) that we will randomly place and subsequently remove from the game screen
#

# ------ create start screen with our names and basic instructions


def tick(keys):


   #  global game_on
   #  global score
   #  global coin_count
   global game_speed

   #  -- Camera and Floor Movement---
   #  the camera will scroll with the player, as time progresses the camera and the player will speed up. The screen will scroll faster and faster, making the game harder.

   camera.x += game_speed
   floor.x += game_speed

   # -- Refreshing the Floor ---


   #
   #
   #  # --- PLAYER MOVEMENT ---
   #  if game_on:
   #      player.move_speed()
   #
   # # if the player is not touching the ground we need to introduce gravity:
   #   player.yspeed += 2
   #
   #  # ------- INPUT ---------
   #  if pygame.K_SPACE in keys:
   #      game_on = True
   #  if pygame.K_UP in keys:
   #      player.y -= 5
   #
   #   #-------OBSTACLE INTRODUCTION -----
   #   #-------we will have lists of different obstacles and then we will add in these obstacles randomly at various times
   #

   camera.clear("light blue")
   camera.draw(floor)
   camera.draw(player)
   camera.display()

ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)
