import threading

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Gui(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.width = 10
        self.height = 10
        self.margin = 1
        self.grid = []

        for row in range(50):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(50):
                self.grid[row].append(0)  # Append a cell

    def updateCell(self,x,y,valeur):
        self.grid[x][y]=valeur

    def run(self):
        # Initialize pygame
        pygame.init()

        # Set the HEIGHT and WIDTH of the screen
        WINDOW_SIZE = [550, 505]
        screen = pygame.display.set_mode(WINDOW_SIZE)

        # Set title of screen
        pygame.display.set_caption("Jeu de la vie")

        # Loop until the user clicks the close button.
        done = False

        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        # -------- Main Program Loop -----------
        while not done:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (self.width + self.margin)
                    row = pos[1] // (self.height + self.margin)
                    # Set that location to one
                    self.grid[row][column] = 1
                    print("Click ", pos, "Grid coordinates: ", row, column)

            # Set the screen background
            screen.fill(BLACK)

            # Draw the grid
            for row in range(50):
                for column in range(50):
                    color = WHITE
                    if self.grid[row][column] == 1:
                        color = BLACK


                    pygame.draw.rect(screen,
                                     color,
                                     [(self.margin + self.width) * column + self.margin,
                                      (self.margin + self.height) * row + self.margin,
                                      self.width,
                                      self.height])

            # Limit to 60 frames per second
            clock.tick(60)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

        # Be IDLE friendly. If you forget this line, the program will 'hang'
        # on exit.
        pygame.quit()