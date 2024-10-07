#koodis olen kasutanud w3schools.com
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 1000
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
NUPPU_SUURUS = WIDTH // 16

OLE_KESKEL = (SQUARE_SIZE - NUPPU_SUURUS) // 2

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("malelaud")

# Load piece images
WHITE_PAWN = pygame.image.load('vettur.png').convert_alpha()
BLACK_PAWN = pygame.image.load('mettur.png').convert_alpha()

vratsu = pygame.image.load("vobune.png").convert_alpha()
mratsu = pygame.image.load("mobune.png").convert_alpha()

vvanker = pygame.image.load("vvanker.png").convert_alpha()
mvanker = pygame.image.load("mvanker2.png").convert_alpha()

voda = pygame.image.load("voda.png").convert_alpha()
moda = pygame.image.load("moda.png").convert_alpha()

vlipp = pygame.image.load("vlipp224.png").convert_alpha()
mlipp = pygame.image.load("mlipp2.png").convert_alpha()

vkunn = pygame.image.load("vkunn.png").convert_alpha()
mkunn = pygame.image.load("mkunn.png").convert_alpha()

# Scale piece images
WHITE_PAWN = pygame.transform.scale(WHITE_PAWN, (NUPPU_SUURUS, NUPPU_SUURUS))
BLACK_PAWN = pygame.transform.scale(BLACK_PAWN, (NUPPU_SUURUS, NUPPU_SUURUS))

vratsu = pygame.transform.scale(vratsu, (NUPPU_SUURUS, NUPPU_SUURUS))
mratsu = pygame.transform.scale(mratsu, (NUPPU_SUURUS, NUPPU_SUURUS))

vvanker = pygame.transform.scale(vvanker, (NUPPU_SUURUS, NUPPU_SUURUS))
mvanker = pygame.transform.scale(mvanker, (NUPPU_SUURUS, NUPPU_SUURUS))

voda = pygame.transform.scale(voda, (NUPPU_SUURUS, NUPPU_SUURUS))
moda = pygame.transform.scale(moda, (NUPPU_SUURUS, NUPPU_SUURUS))

vlipp = pygame.transform.scale(vlipp, (NUPPU_SUURUS, NUPPU_SUURUS))
mlipp = pygame.transform.scale(mlipp, (NUPPU_SUURUS, NUPPU_SUURUS))

vkunn = pygame.transform.scale(vkunn, (NUPPU_SUURUS, NUPPU_SUURUS))
mkunn = pygame.transform.scale(mkunn, (NUPPU_SUURUS, NUPPU_SUURUS))




# Board setup: 0 = empty, 1 = white pawn, 2 = black pawn
board = [
    [6, 4, 8, 12, 10, 8, 4, 6],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [5, 3, 7, 11, 9, 7, 3, 5]
]

def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces():
    OLE_KESKEL = (SQUARE_SIZE - NUPPU_SUURUS) // 2
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            x = col * SQUARE_SIZE + OLE_KESKEL  
            y = row * SQUARE_SIZE + OLE_KESKEL
            #ettirud
            if piece == 1:
                screen.blit(WHITE_PAWN, (x, y))
            elif piece == 2:
                screen.blit(BLACK_PAWN, (x, y))
            #hobused
            elif piece == 3:
                screen.blit(vratsu, (x, y))
            elif piece == 4:
                screen.blit(mratsu, (x, y))
            #vanker
            elif piece == 5:
                screen.blit(vvanker, (x, y))
            elif piece == 6:
                screen.blit(mvanker, (x, y))
#oda
            elif piece == 7:
                screen.blit(voda, (x, y))
            elif piece == 8:
                screen.blit(moda, (x, y))
                #lipp
            elif piece == 9:
                screen.blit(vlipp, (x, y))
            elif piece == 10:
                screen.blit(mlipp, (x, y))
            elif piece == 11:
                screen.blit(vkunn, (x, y))
            elif piece == 12:
                screen.blit(mkunn, (x, y))


def highlight_square(row, col):
    pygame.draw.rect(screen, BLUE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 5)
    
def highlight_legal_moves(start_row, start_col):
    """Highlight all legal moves for the selected piece."""
    for row in range(ROWS):
        for col in range(COLS):
            if is_valid_move(start_row, start_col, row, col):
                pygame.draw.circle(screen, GREEN, 
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 
                                   SQUARE_SIZE // 6)

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def is_valid_move(start_row, start_col, end_row, end_col):
    piece = board[start_row][start_col]
    target_piece = board[end_row][end_col]

    # Ensure that the target square is not occupied by a piece of the same color
    if (piece % 2 == 1 and target_piece % 2 == 1) or (piece % 2 == 0 and target_piece % 2 == 0 and target_piece != 0):
        return False

    # black pawn movement
    if piece == 2:  
        if start_row == 1 and end_row == start_row + 2 and start_col == end_col and board[end_row][end_col] == 0:
            return True
        if end_row == start_row + 1 and start_col == end_col and board[end_row][end_col] == 0:
            return True
        if end_row == start_row + 1 and abs(start_col - end_col) == 1 and target_piece in [1, 3, 5, 7, 9]:
            return True

    # wjite pawn movement
    elif piece == 1:  
        if start_row == 6 and end_row == start_row - 2 and start_col == end_col and board[end_row][end_col] == 0:
            return True
        if end_row == start_row - 1 and start_col == end_col and board[end_row][end_col] == 0:
            return True
        if end_row == start_row - 1 and abs(start_col - end_col) == 1 and target_piece in [2, 4, 6, 8, 10]:
            return True

    # Knight movement
    elif piece in [3, 4]:  
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            return True

    # Rook movement
    elif piece in [5, 6]:  
        if start_row == end_row or start_col == end_col:  # Moving straight
            if start_row == end_row:  # Horizontal move
                for col in range(min(start_col, end_col) + 1, max(start_col, end_col)):
                    if board[start_row][col] != 0:
                        return False
            if start_col == end_col:  # Vertical move
                for row in range(min(start_row, end_row) + 1, max(start_row, end_row)):
                    if board[row][start_col] != 0:
                        return False
            return True

    # Bishop movement
    elif piece in [7, 8]:  
        if abs(end_row - start_row) == abs(end_col - start_col):  # Moving diagonally
            row_step = 1 if end_row > start_row else -1
            col_step = 1 if end_col > start_col else -1
            for i in range(1, abs(end_row - start_row)):
                if board[start_row + i * row_step][start_col + i * col_step] != 0:
                    return False
            return True

    # Queen movement
    elif piece in [9, 10]:  
        if start_row == end_row or start_col == end_col:  # Rook-like movement
            if start_row == end_row:
                for col in range(min(start_col, end_col) + 1, max(start_col, end_col)):
                    if board[start_row][col] != 0:
                        return False
            if start_col == end_col:
                for row in range(min(start_row, end_row) + 1, max(start_row, end_row)):
                    if board[row][start_col] != 0:
                        return False
            return True
        elif abs(end_row - start_row) == abs(end_col - start_col):  # Bishop-like movement
            row_step = 1 if end_row > start_row else -1
            col_step = 1 if end_col > start_col else -1
            for i in range(1, abs(end_row - start_row)):
                if board[start_row + i * row_step][start_col + i * col_step] != 0:
                    return False
            return True
    elif piece in [11, 12]:  # Assuming 11 = white king, 12 = black king
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        if max(row_diff, col_diff) == 1:  # King moves 1 square in any direction
            return True

    return False

def move_piece(start_row, start_col, end_row, end_col):
    
    piece = board[start_row][start_col]
    
    if is_valid_move(start_row, start_col, end_row, end_col):
        board[end_row][end_col] = board[start_row][start_col]
        board[start_row][start_col] = 0
        
        if piece in [1] and end_row == 0:  # White pawn reaches the last row
            promote_pawn(end_row, end_col, 'white')
        elif piece in [2] and end_row == 7:  # Black pawn reaches the last row
            promote_pawn(end_row, end_col, 'black')
        return True
    return False


def promote_pawn(row, col, color):
    # Display promotion options (queen, rook, bishop, knight)
    promotion_options = [(9 if color == 'white' else 10), 
                         (5 if color == 'white' else 6), 
                         (7 if color == 'white' else 8), 
                         (3 if color == 'white' else 4)]
    option_names = ['Lipp ', 'Vanker', '  Oda ', 'Ratsu']
    
    # Render menu
    font = pygame.font.Font(None, 36)
    menu_width = SQUARE_SIZE * 4
    menu_height = SQUARE_SIZE
    menu_x = WIDTH // 2 - menu_width // 2
    menu_y = HEIGHT // 2 - menu_height // 2
    
    # Draw menu background
    pygame.draw.rect(screen, GREEN, (menu_x, menu_y, menu_width, menu_height))

    for i, option in enumerate(promotion_options):
        text = font.render(option_names[i], True, BLACK)
        screen.blit(text, (menu_x + i * SQUARE_SIZE + 10, menu_y + 10))
    
    pygame.display.flip()
    
    choosing = True
    while choosing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if menu_y <= pos[1] <= menu_y + menu_height:
                    selected_option = (pos[0] - menu_x) // SQUARE_SIZE
                    if 0 <= selected_option < len(promotion_options):
                        board[row][col] = promotion_options[selected_option]
                        choosing = False

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
            highlight_legal_moves(*selected_square)
        pygame.display.flip()

if __name__ == "__main__":
    main()
