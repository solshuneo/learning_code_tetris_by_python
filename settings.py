import pygame
CELL_SIZE = 40
COLUMNS = 10
ROWS = 20
PADDING = 20
GAME_SIZE = pygame.Vector2(COLUMNS * CELL_SIZE, ROWS * CELL_SIZE)

RATIO_PREVIEW = 0.7
PREVIEW_SIZE = pygame.Vector2(COLUMNS * CELL_SIZE / 2, RATIO_PREVIEW * ROWS * CELL_SIZE)

RATIO_SCORE = 1 - RATIO_PREVIEW
SCORE_SIZE = pygame.Vector2(COLUMNS * CELL_SIZE / 2, RATIO_SCORE * ROWS * CELL_SIZE - PADDING)

# WINDOW_SIZE = GAME_SIZE + PREVIEW_SIZE + SCORE_SIZE + (3 * PADDING, 2 * PADDING)
WINDOW_SIZE = GAME_SIZE + (3 * PADDING, 2 * PADDING) + pygame.Vector2(PREVIEW_SIZE.x, 0)

OFFSET = (COLUMNS // 2, 1)

# Biến thể của màu đỏ
LIGHT_RED   = (255, 102, 102)  # Đỏ nhạt
DARK_RED    = (139, 0, 0)      # Đỏ đậm

# Biến thể của màu xanh lá
LIGHT_GREEN = (144, 238, 144)  # Xanh lá nhạt
DARK_GREEN  = (0, 100, 0)      # Xanh lá đậm

# Biến thể của màu xanh dương
LIGHT_BLUE  = (173, 216, 230)  # Xanh dương nhạt
DARK_BLUE   = (0, 0, 139)      # Xanh dương đậm

# Biến thể của màu vàng
LIGHT_YELLOW = (255, 255, 224) # Vàng nhạt
DARK_YELLOW  = (204, 204, 0)   # Vàng đậm

# Biến thể của màu cam
LIGHT_ORANGE = (255, 200, 150) # Cam nhạt
DARK_ORANGE  = (255, 140, 0)   # Cam đậm

# Biến thể của màu tím
LIGHT_PURPLE = (216, 191, 216) # Tím nhạt
DARK_PURPLE  = (75, 0, 130)    # Tím đậm

# Biến thể của màu hồng
LIGHT_PINK   = (255, 182, 193) # Hồng nhạt
DARK_PINK    = (255, 20, 147)  # Hồng đậm

# Biến thể của màu nâu
LIGHT_BROWN  = (222, 184, 135) # Nâu nhạt
DARK_BROWN   = (101, 67, 33)   # Nâu đậm

# Biến thể của màu xám
SILVER       = (192, 192, 192) # Bạc (xám nhạt)
DIM_GRAY     = (105, 105, 105) # Xám mờ

# Một số màu đặc biệt khác
GOLD         = (255, 215, 0)   # Vàng ánh kim
OLIVE        = (128, 128, 0)   # Xanh oliu
TEAL         = (0, 128, 128)   # Xanh mòng két
NAVY         = (0, 0, 128)     # Xanh hải quân

# Hàm để chuyển đổi mã màu hex sang RGB
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')  # Loại bỏ dấu #
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


LINE_COLOR = hex_to_rgb("#ffffff")
BACKGROUND_COLOR = (105, 105, 105)


# Shapes and colors for the Tetris-like tetrominoes
TETROMINOS = {
    'T': {'shape': [(0, 0), (-1, 0), (1, 0), (0, -1)], 'color': 'PURPLE'},
    'O': {'shape': [(0, 0), (0, -1), (1, 0), (1, -1)], 'color': 'YELLOW'},
    'J': {'shape': [(0, 0), (0, 1), (0, -1), (-1, -1)], 'color': 'BLUE'},
    'L': {'shape': [(0, 0), (0, 1), (0, -1), (1, -1)], 'color': 'ORANGE'},
    'I': {'shape': [(0, 0), (0, 1), (0, -2), (0, -1)], 'color': 'CYAN'},
    'S': {'shape': [(0, 0), (-1, 0), (0, -1), (1, -1)], 'color': 'GREEN'},
    'Z': {'shape': [(0, 0), (1, 0), (0, -1), (-1, -1)], 'color': 'RED'}
}

UPDATE_START_SPEED = 300
MOVE_WAIT_TIME = 200
ROATE_WAIT_TIME = 200

# Score data based on the number of lines cleared
SCORE_DATA = {0 : 0, 1: 40, 2: 100, 3: 300, 4: 1200}