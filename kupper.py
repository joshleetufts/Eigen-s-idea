import pygame as pg
import random

# Graphic setup (Initialize and set title)
pg.init()
pg.display.set_caption("Kuppers' illustration of Eigen's idea from "
                           "the book, Dennett's Darwin's Dangerous Idea")


# Simulates natural selection from 3 species (represented by colors)
class NaturalSelection():

    def __init__(self, size, height, width):

        # Size of the total display
        self.display_width = width
        self.display_height = height

        # The width and height of the checkerboard
        self.size = size

        # Scaling for the size of each rectangle
        self.scale_x = width / size
        self.scale_y = height / size

        # Set the screen with the display size (width gets + 100 for label)
        self.screen = pg.display.set_mode((self.display_width + 100,
                                               self.display_height))

        # The object that will hold the checkerboard values
        self.figure = pg.Surface(self.screen.get_size())

        # Colors stores the tuples for colors: brown, white, sky blue
        self.colors =[(130, 82, 1), (255, 255, 255), (135, 206, 235)]

        # The Checkerboard that has 64 (SIZE * SIZE) with random colors
        self.checker_board = [[self.colors[random.randrange(3)] for x in
                               range(self.size)] for y in range(self.size)]


        # The font used for the pg
        self.font = pg.font.Font(None, 20)

        # The count of how many times it took for all to be the same
        self.count = 0
        
        # The rolls from the dice that will be randomly chosen each loop
        self.roll_x = 0
        self.roll_y = 0

        # Initialize the board with random colors in each cell
        for x in range(0, self.size):
            for y in range(0, self.size):
                pg.draw.rect(self.figure, self.checker_board[x][y],
                             (self.scale_x * x, self.scale_y * y,
                              self.scale_x, self.scale_y))
        self.screen.blit(self.figure, [0, 0])
        pg.display.flip()


    def start(self):

        # Loops 10000 times to see if one has won over the others
        while (self.count < 10000):

            # Checks if all the values are the same. If they are, end program
            if self.check_board():
                return

            # Rolls the dice to determine which color reproduces to a new cell
            if self.selection():

                # Draws the board to visualize the changes in the 2D Array
                self.draw_board()

            # Updates the count and the board
            self.update_count()


    def check_board(self):
        # Checks if all values are the same
        for x in range(0, self.size):
            for y in range(0, self.size):
                if (self.checker_board[x][y] != self.checker_board[0][0]):
                    break
                # If all values are the same, print the count and return
                elif x == self.size - 1 and y == self.size - 1:
                    print "\nCount is: " + str(self.count) + "\n"
                    return True
            if (self.checker_board[x][y] != self.checker_board[0][0]):
                break
        return False


    def selection(self):
        # Generates the roll
        self.roll_x = random.randint(0, (self.size - 1))
        self.roll_y = random.randint(0, (self.size - 1))

        # Winner gets the value
        winner = self.checker_board[self.roll_x][self.roll_y]

        # Generates the roll
        self.roll_x = random.randint(0, (self.size - 1))
        self.roll_y = random.randint(0, (self.size - 1))

        # Call draw_board only if it is different (for optimization of speed)
        if (self.checker_board[self.roll_x][self.roll_y] != winner):
            self.checker_board[self.roll_x][self.roll_y] = winner
            return True
        else:
            return False


    def draw_board(self):
        # Updates the values of board
        pg.draw.rect(self.figure, self.checker_board[self.roll_x][self.roll_y],
                         (self.scale_x * self.roll_x, self.scale_y *
                          self.roll_y, self.scale_x, self.scale_y))

        # Draws the updated board to the screen
        self.screen.blit(self.figure, [0, 0])


    def update_count(self):
        # Increments the count, which is the total number of loops
        self.count += 1

        # Makes the counter text at the corner
        count_text = self.font.render("Count: " + str(self.count), 1,
                                      (255, 255, 255))

        # Draws the updated count to the screen
        self.screen.blit(count_text, (800, 100))

        #Update the display with all the previous changes
        pg.display.flip()



# Program run
game = NaturalSelection(8, 800, 800)

game.start()

