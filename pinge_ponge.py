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
rocket2 = Player("rocket.png", 30, 200, 4, 50, 150)
ball = GameSprite("balls.png", 200, 200, 4, 50, 30)



game = True
finish = False
while game:
  for e in event.get():
    if e.type == QUIT:
      game = False    
    if not finish:
      window.fill(back)

    if not finish:
      window.fill(back)
      rocket1.update_l()
      rocket2.update_r()

      rocket1.reset()
      rocket2.reset()
      ball.reset()

      display.update()
    time.delay(50)
