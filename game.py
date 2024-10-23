import pygame
from settings import *
from os.path import join
import random
from timer import Timer
class Game:
    def __init__(self, update_score, get_next_shape) -> None:
        self.update_score = update_score
        self.surface = pygame.Surface(GAME_SIZE)
        self.surface.fill(BACKGROUND_COLOR)
        self.surface.set_alpha(120)
        self.screen = pygame.display.get_surface()

        self.get_next_shape = get_next_shape

        self.rect = self.surface.get_rect(topleft = (PADDING, PADDING))
        self.sprites = pygame.sprite.Group()
        
        self.field_data = [[0 for x in range(COLUMNS)] for y in range(ROWS)]        
        self.tetromino = Tetromino(self.get_next_shape(), self.sprites, self.create_new_tetromino, self.field_data)
        #self.tetromino = Tetromino('O', self.sprites, self.create_new_tetromino, self.field_data)\
        #self.tetromino = Tetromino(random.choice(list(TETROMINOS.keys())), self.sprites, self.create_new_tetromino, self.field_data)
        self.speed_down = UPDATE_START_SPEED
        self.speed_down_faster = UPDATE_START_SPEED * 0.3
        self.down_pressed = False
        self.timers = {
            'vertical move': Timer(self.speed_down, True, self.move_down),
            'horizontal move' : Timer(MOVE_WAIT_TIME),
            'rotate' : Timer(ROATE_WAIT_TIME)
        }
        self.timers['vertical move'].activate()

        self.current_level = 1
        self.current_score = 0
        self.current_lines = 0

        self.music = pygame.mixer.Sound(join('.', '.', 'landing.wav'))
        self.music.set_volume(0.3)

    def calculate_score(self, num_lines):
        self.current_lines += num_lines
        self.current_score += SCORE_DATA[num_lines] * self.current_level

        if self.current_lines / 10 > self.current_level:
            self.current_level += 1
  
        self.update_score(self.current_lines, self.current_score, self.current_level)
        
    def check_game_over(self):
        for block in self.tetromino.blocks:
            if block.pos.y <= 1:
                self.music.play(10)
                exit()
    def create_new_tetromino(self):
        self.music.play()
        self.check_game_over()
        self.check_clear_row()      

        #self.tetromino = Tetromino(random.choice(list(TETROMINOS.keys())), self.sprites, self.create_new_tetromino, self.field_data)
        self.tetromino = Tetromino(self.get_next_shape(), self.sprites, self.create_new_tetromino, self.field_data)
    def timer_update(self):
        for timer in self.timers.values():
            timer.update()

    def move_down(self):  
        self.tetromino.move_down()

    def draw_grid(self):
        for col in range(1, COLUMNS):
            x = col * CELL_SIZE            
            pygame.draw.line(self.surface, LINE_COLOR, (x, 0), (x, self.surface.get_height()), 1)
        for row in range(1, ROWS):
            y = row * CELL_SIZE
            pygame.draw.line(self.surface, LINE_COLOR, (0, y), (self.surface.get_width(), y), 1)

    def input(self):
        key = pygame.key.get_pressed()
        if not self.timers['horizontal move'].active:
            if key[pygame.K_LEFT]:
                self.tetromino.move_horizontal(-1)
                self.timers['horizontal move'].activate()
            if key[pygame.K_RIGHT]:
                self.tetromino.move_horizontal(1)
                self.timers['horizontal move'].activate()
        if not self.timers['rotate'].active:
            if (key[pygame.K_UP]):
                self.timers['rotate'].activate()
                self.tetromino.rotate()
        if not self.down_pressed and key[pygame.K_DOWN]:
            self.down_pressed = True
            self.timers['vertical move'].duration = self.speed_down_faster
        if self.down_pressed and not key[pygame.K_DOWN]:
            self.down_pressed = False
            self.timers['vertical move'].duration = self.speed_down
    def check_clear_row(self):
        delete_rows = []
        for i, row in enumerate(self.field_data):
            if all(row):
                delete_rows.append(i)
        if delete_rows:
            for delete_row in delete_rows:
                for block in self.field_data[delete_row]:
                    block.kill()
                for row in self.field_data:
                    for block in row:
                        if block and block.pos.y < delete_row:
                            block.pos.y += 1
        self.field_data = [[0 for x in range(COLUMNS)] for y in range(ROWS)]
        for block in self.sprites:
            if block:
                self.field_data[int(block.pos.y)][int(block.pos.x)] = block

        self.calculate_score(len(delete_rows))
    def run(self) -> None:
        self.input()
        self.timer_update()
        self.sprites.update()
        self.screen.blit(self.surface, (PADDING, PADDING))
        self.surface.fill(BACKGROUND_COLOR)
        self.draw_grid()
        pygame.draw.rect(self.screen, LINE_COLOR, self.rect, 2, 2)
        self.sprites.draw(self.surface)

class Tetromino:
    def __init__(self, shape, sprite_group, create_new_tetromino, field_data) -> None:
        self.shape = shape
        self.block_positions = TETROMINOS[self.shape]['shape']
        self.color = TETROMINOS[self.shape]['color']
        self.field_data = field_data
        self.blocks = [Block(sprite_group, pos, self.color) for pos in self.block_positions]
        self.create_new_tetromino = create_new_tetromino
    def rotate(self):
        if self.shape != 'O':
            pivot_pos = self.blocks[0].pos
            
            new_block_position = [block.rotate(pivot_pos) for block in self.blocks]

            for pos in new_block_position:
                if pos.x < 0 or pos.x >= COLUMNS:
                    return 
                
                if self.field_data[int(pos.y)][int(pos.x)]:
                    return 
                if pos.y > ROWS:
                    return

            for i, block in enumerate(self.blocks):
                block.pos = new_block_position[i]
        print('rotate')
    def horizontal_collide(self, amount):
        collide_list = [block.horizontal_collide(block.pos.x + amount, self.field_data) for block in self.blocks]
        return True if any(collide_list) else False
    def vertical_collide(self):
        collide_list = [block.vertical_collide(self.field_data) for block in self.blocks]
        return True if any(collide_list) else False
    def move_horizontal(self, amount):
        if not self.horizontal_collide(amount):
            for block in self.blocks:
                block.pos.x += amount
    def move_down(self):        
        if not self.vertical_collide():
            for block in self.blocks:
                block.pos.y += 1
        else:            
            for block in self.blocks:
                self.field_data[int(block.pos.y)][int(block.pos.x)] = block
            self.create_new_tetromino()

class Block(pygame.sprite.Sprite):
    def __init__(self, group, pos, color) -> None:
        super().__init__(group)
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))        
        self.image.fill(color)
        self.pos = pygame.Vector2(pos) + OFFSET 
        self.rect = self.image.get_rect(topleft = self.pos * CELL_SIZE)
    def rotate(self, pivot_pos):
        distance = self.pos - pivot_pos
        rotated = distance.rotate(90)
        return pivot_pos + rotated
    def horizontal_collide(self, x, field_data):
        return not (0 <= x < COLUMNS and field_data[int(self.pos.y)][int(x)] == 0)
    def vertical_collide(self, field_data):
        return not (self.pos.y + 1 < ROWS and field_data[int(self.pos.y + 1)][int(self.pos.x)] == 0)
    
    def update(self):
        self.rect = self.image.get_rect(topleft = self.pos * CELL_SIZE)