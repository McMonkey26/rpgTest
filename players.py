import pygame
tileSize = 16
class adventurer(pygame.sprite.Sprite):
  def __init__(self, name, race, health, moves=[None, None, None], nick=None):
    super().__init__()
    self.name = name
    self.nick = name if nick == None else nick
    self.race = race
    self.maxHp = health
    self.hp = health
    self.maxStm = 100
    self.stm = 100
    self.strength = 0
    self.dexterity = 0
    self.constitution = 0
    self.wisdom = 0
    self.intelligence = 0
    self.charisma = 0
    self.coins = 0
    self.keys = []
    self.image = pygame.Surface((16, 16))
    self.image.fill((0, 0, 0))
    self.rect = self.image.get_rect()
    self.rect.topleft = (16, 16)
    self.pos = [1, 1]
    self.speed = 1
    self.combat = False
    for move in moves:
      setattr(self, move.id, move)
  def show(self):
    print(self.name,'('+self.nick+')')
    print(self.race)
    print('HP:',self.hp,'/',self.maxHp)
    print('Stamina:',self.stm,'/',self.maxStm)
    print(str(type(self))[(str(type(self)).find('.') if not str(type(self)).find('.') == -1 else str(type(self)).find('\''))+1:-2])
  def move(self, event, group):
    if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
      if event.key == pygame.K_a:
        self.elvenBow.turn('l')
        self.elvenBlade.turn('l')
        self.thievesKnife.turn('l')
        self.bomb.turn('l')
        self.rect.x -= 8 * self.speed
        self.pos[0] -= 0.5 * self.speed
        if (hits:=pygame.sprite.spritecollide(self, group, False)):
          self.rect.x += 8 * self.speed
          self.pos[0] += 0.5 * self.speed
          for hit in hits:
            if hit.type == 'Enemy':
              self.hp -= hit.damage
            elif hit.type == 'Chest':
              hit.open(self)
            elif hit.type == 'Wall':
              pass
      elif event.key == pygame.K_w:
        self.elvenBow.turn('u')
        self.elvenBlade.turn('u')
        self.thievesKnife.turn('u')
        self.bomb.turn('u')
        self.rect.y -= 8 * self.speed
        self.pos[1] -= 0.5 * self.speed
        if (hits:=pygame.sprite.spritecollide(self, group, False)):
          self.rect.y += 8 * self.speed
          self.pos[1] += 0.5 * self.speed
          for hit in hits:
            if hit.type == 'Enemy':
              self.hp -= hit.damage
            elif hit.type == 'Chest':
              hit.open(self)
            elif hit.type == 'Wall':
              pass
      elif event.key == pygame.K_d:
        self.elvenBow.turn('r')
        self.elvenBlade.turn('r')
        self.thievesKnife.turn('r')
        self.bomb.turn('r')
        self.rect.x += 8 * self.speed
        self.pos[0] += 0.5 * self.speed
        if (hits:=pygame.sprite.spritecollide(self, group, False)):
          self.rect.x -= 8 * self.speed
          self.pos[0] -= 0.5 * self.speed
          for hit in hits:
            if hit.type == 'Enemy':
              self.hp -= hit.damage
            elif hit.type == 'Chest':
              hit.open(self)
            elif hit.type == 'Wall':
              pass
      elif event.key == pygame.K_s:
        self.elvenBow.turn('d')
        self.elvenBlade.turn('d')
        self.thievesKnife.turn('d')
        self.bomb.turn('d')
        self.rect.y += 8 * self.speed
        self.pos[1] += 0.5 * self.speed
        if (hits:=pygame.sprite.spritecollide(self, group, False)):
          self.rect.y -= 8 * self.speed
          self.pos[1] -= 0.5 * self.speed
          for hit in hits:
            if hit.type == 'Enemy':
              self.hp -= hit.damage
            elif hit.type == 'Chest':
              hit.open(self)
            elif hit.type == 'Wall':
              pass
  def ability(self, event, screen, group):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP and self.stm >= self.elvenBow.stamina:
        for enemy in group:
          if self.hurtbox(self.elvenBow).colliderect(enemy) and enemy.alive:
            enemy.health -= self.elvenBow.damage
          enemy.interact()
          print(enemy.health)
        pygame.draw.rect(screen, (255, 0, 0), self.hurtbox(self.elvenBow))
        self.stm -= self.elvenBow.stamina
      elif event.key == pygame.K_DOWN and self.stm >= self.bomb.stamina:
        for enemy in group:
          if self.hurtbox(self.bomb).colliderect(enemy) and enemy.alive:
            enemy.health -= self.bomb.damage
          enemy.interact()
          print(enemy.health)
        pygame.draw.rect(screen, (255, 0, 0), self.hurtbox(self.bomb))
        self.stm -= self.bomb.stamina
      elif event.key == pygame.K_RIGHT and self.stm >= self.thievesKnife.stamina:
        for enemy in group:
          if self.hurtbox(self.thievesKnife).colliderect(enemy) and enemy.alive:
            enemy.health -= self.thievesKnife.damage
          enemy.interact()
          print(enemy.health)
        pygame.draw.rect(screen, (255, 0, 0), self.hurtbox(self.thievesKnife))
        self.stm -= self.thievesKnife.stamina
      elif event.key == pygame.K_LEFT and self.stm >= self.elvenBlade.stamina:
        for enemy in group:
          if self.hurtbox(self.elvenBlade).colliderect(enemy) and enemy.alive:
            enemy.health -= self.elvenBlade.damage
          enemy.interact()
          print(enemy.health)
        pygame.draw.rect(screen, (255, 0, 0), self.hurtbox(self.elvenBlade))
        self.stm -= self.elvenBlade.stamina
  def hurtbox(self, weapon):
    return scale(offset(weapon.rect, self.pos), tileSize)
class Paladin(adventurer):
  def __init__(self, name, race, health, moves=[None, None, None], nick=None):
    super().__init__(name, race, health, moves, nick)
    self.type = 'Paladin'
class weapon:
  def __init__(self, id, name, type, damage, dType, hBox, stamina):
    self.id = id
    self.name = name
    self.type = type
    self.damage = damage
    self.dType = dType
    self.hurtbox = hBox
    self.rect = pygame.Rect(hBox[0], hBox[1], hBox[2], hBox[3])
    self.defRect = pygame.Rect(hBox[0], hBox[1], hBox[2], hBox[3])
    self.stamina = stamina
  def turn(self, direction):
    if direction == 'u':
      self.rect = pygame.Rect(self.defRect.y, -self.defRect.x - self.defRect.width + 1, self.defRect.height, self.defRect.width)
    elif direction == 'd':
      self.rect = pygame.Rect(self.defRect.y, self.defRect.x, self.defRect.height, self.defRect.width)
    elif direction == 'l':
      self.rect = pygame.Rect(-self.defRect.x - self.defRect.width + 1, self.defRect.y, self.defRect.width, self.defRect.height)
    elif direction == 'r':
      self.rect = pygame.Rect(self.defRect.x, self.defRect.y, self.defRect.width, self.defRect.height)
def offset(rectangle, amt):
  return pygame.Rect(rectangle.x+amt[0], rectangle.y+amt[1], rectangle.width, rectangle.height)
def scale(rectangle, amt):
  return pygame.Rect(rectangle.x*amt, rectangle.y*amt, rectangle.width*amt, rectangle.height*amt)
elvenBlade = weapon('elvenBlade', 'Elven Blade', 'sword', 10, 'Normal', (1,0,2,1), 10) #left
elvenBow = weapon('elvenBow', 'Elven Bow', 'bow', 10, 'Projectile', (1,0,5,1), 20) #up
thievesKnife = weapon('thievesKnife', 'Thieve\'s Knife', 'dagger', 20, 'Normal', (1,0,1,1), 3) #right
bomb = weapon('bomb', 'Bomb', 'explosive', 10, 'Blast', (2,-1,3,3), 20) #down
julian = adventurer('Hawk Feather', 'Tabaxi', 81, [elvenBlade, elvenBow, thievesKnife, bomb], 'Hawk')
julian.show()
