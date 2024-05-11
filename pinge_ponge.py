from pygame import *

win_width = 700
win_height = 500
display.set_caption('pinge-ponge')
window = display.set_mode((win_width, win_height))

back = (200, 255, 255)
window.fill(back)

class GameSprite(sprite.Sprite):
  def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
    sprite.Sprite.__init__(self)
    self.image = transform.scale(image.load(player_image), (size_x, size_y))
    self.speed = player_speed
    self.size_x = size_x
    self.size_y = size_y
    self.rect = self.image.get_rect()
    self.rect.x = player_x
    self.rect.y = player_y
  def reset(self):
    window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
  def update_r(self):
    keys = key.get_pressed()
    if keys[K_UP] and self.rect.y > 5:
      self.rect.y -= self.speed
    if keys [K_DOWN] and self.rect.y < win_height - 80:
      self.rect.y += self.speed
  def update_l(self):
    keys = key.get_pressed()
    if keys[K_LEFT] and self.rect.y > 5:
      self.rect.y -= self.speed
    if keys [K_RIGHT] and self.rect.y < win_height - 80:
      self.rect.y += self.speed

rocket1 = Player("rocket.png", 30, 200, 4, 50, 150)
rocket2 = Player("rocket.png", 620, 200, 4, 50, 150)
ball = GameSprite("balls.png", 200, 200, 4, 50, 30)

speed_y = 3
speed_x = 3
font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (100, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (100, 0, 0))

game = True
finish = False
while game:
  for e in event.get():
    if e.type == QUIT:
      game = False    
  if not finish:
    window.fill(back)
    rocket1.update_l()
    rocket2.update_r()

    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
      speed_x *= -1
      speed_y *= 1

    if ball.rect.y > win_height-50 or ball.rect.y < 0:
      speed_y *= -1

    if ball.rect.x < 0:
      finish = True
      window.blit(lose1, (250, 200)) 
      game_over = True    
        
    if ball.rect.x > win_width:
      finish = True
      window.blit(lose2, (250, 200)) 
      game_over = True            

    rocket1.reset()
    rocket2.reset()
    ball.reset()

    display.update()
  time.delay(50)
