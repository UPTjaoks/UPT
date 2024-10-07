#poolik kood, et tööta
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Load piece images
WHITE_PAWN = pygame.image.load('vettur.png')
BLACK_PAWN = pygame.image.load('mettur.png')

vratsu = pygame.image.load("vobune.png")
mratsu = pygame.image.load("mobune.png")

# Scale piece images
WHITE_PAWN = pygame.transform.scale(WHITE_PAWN, (SQUARE_SIZE, SQUARE_SIZE))
BLACK_PAWN = pygame.transform.scale(BLACK_PAWN, (SQUARE_SIZE, SQUARE_SIZE))

vratsu = pygame.transform.scale(vratsu, (SQUARE_SIZE, SQUARE_SIZE))
mratsu = pygame.transform.scale(mratsu, (SQUARE_SIZE, SQUARE_SIZE))

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Chessboard")

# Board setup: 0 = empty, 1 = white pawn, 2 = black pawn
board = [
    [0, 3, 0, 0, 0, 0, 3, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [0, 4, 0, 0, 0, 0, 4, 0]
]

def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces():
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            #ettirud
            if piece == 1:
                screen.blit(WHITE_PAWN, (col * SQUARE_SIZE, row * SQUARE_SIZE))
            elif piece == 2:
                screen.blit(BLACK_PAWN, (col * SQUARE_SIZE, row * SQUARE_SIZE))
            #hobused
            elif piece == 3:
                screen.blit(vratsu, (col * SQUARE_SIZE, row * SQUARE_SIZE))
            elif piece == 4:
                screen.blit(mratsu, (col * SQUARE_SIZE, row * SQUARE_SIZE))
            #vanker
            elif piece == 5:
                screen.blit(BLACK_PAWN, (col * SQUARE_SIZE, row * SQUARE_SIZE))
            elif piece == 6:
                screen.blit(BLACK_PAWN, (col * SQUARE_SIZE, row * SQUARE_SIZE))

def highlight_square(row, col):
    pygame.draw.rect(screen, BLUE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 5)

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def is_valid_move(start_row, start_col, end_row, end_col):
    piece = board[start_row][start_col]
    if piece == 1:  # White pawn
        if start_row == 1 and end_row == start_row + 2 and start_col == end_col and board[end_row][end_col] == 0:
            return True  # Two-square move from starting position
        if end_row == start_row + 1 and start_col == end_col and board[end_row][end_col] == 0:
            return True  # One-square move
        if end_row == start_row + 1 and abs(start_col - end_col) == 1 and board[end_row][end_col] == 2:
            return True  # Capture
    elif piece == 2:  # Black pawn
        if start_row == 6 and end_row == start_row - 2 and start_col == end_col and board[end_row][end_col] == 0:
            return True  # Two-square move from starting position
        if end_row == start_row - 1 and start_col == end_col and board[end_row][end_col] == 0:
            return True  # One-square move
        if end_row == start_row - 1 and abs(start_col - end_col) == 1 and board[end_row][end_col] == 1:
            return True  # Capture
    return False

def move_piece(start_row, start_col, end_row, end_col):
    if is_valid_move(start_row, start_col, end_row, end_col):
        board[end_row][end_col] = board[start_row][start_col]
        board[start_row][start_col] = 0
        return True
    return False

def main():
    selected_square = None
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                if selected_square:
                    if move_piece(*selected_square, row, col):
                        selected_square = None
                    else:
                        selected_square = (row, col)
                else:
                    selected_square = (row, col)
        
        draw_board()
        draw_pieces()
        
        if selected_square:
            highlight_square(*selected_square)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
