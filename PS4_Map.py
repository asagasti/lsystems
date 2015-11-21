import pygame
import turtle
import string

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just outputing the
# information.
class PS4Input:
    Xbutton = 1
    OButton = 2
    Ybutton = 3
    Cbutton = 0
    RI = 5
    LI = 4
    UP = "(0, 1)"
    DOWN = "(0,-1)"
    LEFT = "(-1,0)"
    RIGHT = "(1,0)"
    ENTER = 13
    ABC = string.ascii_uppercase
    letter = 0
    
   
    def __init__(self):
        
        self.reset()
        pygame.init()
        self.font = pygame.font.Font(None, 20)
        self.line = ""
        self.step = True
        self.draw = True
        self.last = pygame.time.get_ticks()
        self.cooldown = 300

    def printf(self,textString):
        textBitmap = self.font.render(textString, True, BLACK)
        global screen
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10
        
    def sendToScreen(self, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        global screen
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
    
    def getline(self, step):
        #Loop until the user clicks the close button.
        done = False
        self.line = ""
        while done==False:
   
    
            # EVENT PROCESSING STEP
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    done=True # Flag that we are done so we exit this loop
            # DRAWING STEP
            # First, clear the screen to white. Don't put other drawing commands
            # above this, or they will be erased with this command.
            screen.fill(WHITE)
            textPrint.reset()

            # Get count of joysticks
            joystick_count = pygame.joystick.get_count()
            # For each joystick:
            for i in range(joystick_count):
                joystick = pygame.joystick.Joystick(i)
                joystick.init()
                # Get the name from the OS for the controller/joystick
                name = joystick.get_name()
                
                # Usually axis run in pairs, up/down for one, and left/right for
                # the other.
                axes = joystick.get_numaxes()
                axis = joystick.get_axis( 0 )
                if(step == 1):
                    textPrint.printf( "Iterations" )
                    textPrint.printf( "Axis {} value: {:>6.3f}".format(0, axis) )
                    textPrint.unindent()
                if(step == 2):
                    textPrint.printf( "Angle" )
                    textPrint.printf( "Axis {} value: {:>6.3f}".format(0, axis) )
                    textPrint.unindent()
                if(step == 3):
                    textPrint.printf( "Axiom" )
                if(step == 4):
                    textPrint.printf( "Rules" )
                buttons = joystick.get_numbuttons()
               #Control buttons to string
                for i in range( buttons ):
                    button = joystick.get_button( i )
                    now = pygame.time.get_ticks()
                    if now - self.last >= self.cooldown:
                        if i == 1 and button:
                            self.last = now
                            self.letter += 1
                        if i == 2 and button:
                            self.last = now
                            self.step = not self.step
                        if i == 3 and button:
                            self.last = now
                            self.draw = not self.draw
                        if i == 0 and button:
                            self.last = now
                            self.line += "c"
                        if i == 11 and button:
                            self.last = now
                            self.line += "="
                        if i == 10 and button:
                            self.last = now
                            axis = joystick.get_axis(0)
                            self.line += str(abs(int("{:>6.3f}".format(axis).replace(".", ""))))
                        if i == 4 and button:
                            self.last = now
                            self.line += "["   
                        if i == 5 and button:
                            self.last = now
                            self.line += "]" 
                        if i == 13 and button:
                            self.last = now
                            done = True 
                        if i == 7 and button:
                            self.last = now
                            self.line += self.ABC[self.letter]
                            self.letter = 0
                        if i == 6 and button:
                            self.last = now 
                            self.line = self.line[:-1]
                        
                textPrint.indent()
                textPrint.printf("Input: " +  self.line)
                   
                textPrint.unindent()
                    
                # Hat switch. All or nothing for direction, not like joysticks.
                # Value comes back in an array.
                hats = joystick.get_numhats()
              
                
                #Control arrows to string
                for i in range( hats ):
                    hat = joystick.get_hat( i )
                    now = pygame.time.get_ticks()
                    if now - self.last >= self.cooldown:
                        if str(hat) == "(0, 1)":
                            self.last = now
                            if self.step and self.draw:
                                self.line += "F"
                            elif self.step and not self.draw:
                                self.line += "f"
                            elif not self.step and self.draw:
                                self.line += "Z"
                            elif not self.step and not self.draw:
                                self.line += "z"
                        if str(hat) == "(0, -1)":
                            self.last = now
                            if self.step and self.draw:
                                self.line += "++F"
                            elif self.step and not self.draw:
                                self.line += "++f"
                            elif not self.step and self.draw:
                                self.line += "++Z"
                            elif not self.step and not self.draw:
                                self.line += "++z"
                        if str(hat) == "(1, 0)":
                            self.last = now
                            self.line += "+"
                        if str(hat) == "(-1, 0)":
                            self.last = now
                            self.line += "-"
                textPrint.unindent()
                # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    
                # Go ahead and update the screen with what we've drawn.
                pygame.display.flip()

                # Limit to 20 frames per second
                clock.tick(20)
                
        return self.line
    def end(self):
        done = True
        pygame.quit()


 
# Set the width and height of the screen [width,height]
size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")



# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()
    
# Get ready to print
textPrint = PS4Input()
# -------- Main Program Loop -----------

    
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.

