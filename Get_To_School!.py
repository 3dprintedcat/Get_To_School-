"""
Move Sprite With Keyboard

Simple program to show moving a sprite with the keyboard.
The sprite_move_keyboard_better.py example is slightly better
in how it works, but also slightly more complex.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_keyboard
"""

import arcade
import os

SPRITE_SCALING = 2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Move Sprite with Keyboard Example"

MOVEMENT_SPEED = 5

class Player(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Initializer
        """

        # Call the parent class initializer
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Variables that will hold sprite lists
        self.player_list = None

        # Set up the player info
        self.player = None

        # Set the background image
        self.image = (arcade.load_texture("images/spr_0.png",scale=100))

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()

        # Set up the player

        self.player = arcade.AnimatedWalkingSprite()


        self.player.stand_right_textures = []
        
        self.player.stand_right_textures.append(arcade.load_texture("images/spr_0.png",scale=SPRITE_SCALING))
       


        self.player.stand_left_textures = []
        
        self.player.stand_left_textures.append(arcade.load_texture("images/spr_0.png",scale=SPRITE_SCALING))
        
        
        
        self.player.walk_right_textures = []
        
        self.player.walk_right_textures.append(arcade.load_texture("images/spr_0.png",scale=SPRITE_SCALING))
        self.player.walk_right_textures.append(arcade.load_texture("images/spr_1.png",scale=SPRITE_SCALING))
        self.player.walk_right_textures.append(arcade.load_texture("images/spr_2.png", scale=SPRITE_SCALING))
        self.player.walk_right_textures.append(arcade.load_texture("images/spr_3.png", scale=SPRITE_SCALING))


        self.player.walk_left_textures = []
        
        self.player.walk_left_textures.append(arcade.load_texture("images/spr_0.png",scale=SPRITE_SCALING))
        self.player.walk_left_textures.append(arcade.load_texture("images/spr_1.png",scale=SPRITE_SCALING))
        self.player.walk_left_textures.append(arcade.load_texture("images/spr_2.png", scale=SPRITE_SCALING))
        self.player.walk_left_textures.append(arcade.load_texture("images/spr_3.png", scale=SPRITE_SCALING))



        self.player.texture_change_distance = 20
       
        self.player_list.append(self.player)


        self.player.center_x = 50
        self.player.center_y = 50

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        texture = arcade.load_texture("images/greenguyrun1.png")
        arcade.draw_texture_rectangle(540, 120, 100 * texture.width, 100 * texture.height, texture, 0)
        self.player_list.draw()
        

    
       

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.SPACE:
            self.player.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.SPACE or key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0
            
    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        
        self.player_list.update()
        self.player_list.update_animation()

def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()
    

if __name__ == "__main__":
    main()