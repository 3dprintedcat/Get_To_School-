"""
Move Sprite With Keyboard

Simple program to show moving a sprite with the keyboard.
The sprite_move_keyboard_better.py example is slightly better
in how it works, but also slightly more complex.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_keyboard
"""

import time
import arcade
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "GET TO SCHOOL"
BOOKSPEED = 100
# Sprite's properties 
sprite_scaling = 1
sprite_jumping = 10
GRAVITY = 0.7
MOVEMENT_SPEED = 5


tile_size= 32
scaled_tile_size = tile_size * sprite_scaling
map_height = 15
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(  mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
        
def get_map():

    map_file = open("CSVFiles/FullMap.csv")

    # Create an empty list of rows that will hold our map
    map_array = []

    # Read in a line from the file
    for line in map_file:
        line = line.strip()
        map_row = line.split(",")
        
        for index, item in enumerate(map_row):
            map_row[index] = int(item)
        map_array.append(map_row)

    return map_array



        
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
    def __init__(self,width,height,title):
    
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.image = (arcade.load_texture("images/spr_0.png",scale=100))
        self.player_list = None
        self.wall_list = None
        
        #self.doof_list = None
        #self.endFlag_list = None

        self.player_sprite = None
        self.physics_engine = None
        self.books1 = None
        self.books2 = None
        self.books3 = None
        #self.game_over = False
        
        self.total_time = 100.
        #self.bomb = 0
        self.view_left = 0
        self.view_bottom = 0
        

        #Sounds
       # self.spider_hit_sound = arcade.load_sound("audio/EnemyHit.wav")
       # self.pickup_item_sound = arcade.load_sound("audio/PickupItem.wav")



        # Call the parent class initializer
        

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        

        
       

    def setup(self):
        """ Set up the game and initialize the variables. """
       
       
        
        self.player_list = arcade.SpriteList()
        
        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        self.wall_list = arcade.SpriteList()
        
         # Player
        self.player = arcade.Sprite("images/spr_0.png",1)
        self.books1 = arcade.Sprite("images/book.png",1)
        self.books2 = arcade.Sprite("images/book.png",1)
        self.books3 = arcade.Sprite("images/book.png",1)
        
              # Set up the player
        self.player.center_x = 50
        self.player.center_y = 50  
        self.player.scale = .75

        
        self.books1.center_x = 800
        self.books1.center_y = 60


        self.books2.center_x = 50
        self.books2.center_y = 50


        self.books3.center_x = 50
        self.books3.center_y = 50
        
        # Sprite lists
        
        wall = arcade.Sprite("images/ground.png", 25)
        wall.left = 0
        wall.top = 40
        self.wall_list.append(wall)


        
        

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player,self.wall_list, gravity_constant = GRAVITY)




    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        
        
        
        
        texture = arcade.load_texture("images/background.png")
        arcade.draw_texture_rectangle(320, 120, 30* texture.width, 30 * texture.height, texture, 0)
        
        minutes = int(self.total_time) // 60
        seconds = int(self.total_time) % 60
        time_text = f"Time: {minutes:02d}:{seconds:02d}"
        arcade.draw_text(time_text, 25 + self.view_left, 550 + self.view_bottom, arcade.color.BLACK, 20)
        self.total_time-=.01
        self.books1.change_x = -4
        if (self.total_time%20) == 0:
            self.books1.change_x -=4
        if self.total_time == -1:
            self.total_time =0
            end = arcade.load_texture("images/end.png")
            arcade.draw_texture_rectangle(400, 120, 10* end.width, 10 * end.height, end, 0)
            
        self.wall_list.draw()
        self.player.draw()
        self.books1.draw()
    def update(self, delta_time):
        """ Movement and game logic """
        
        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        
        self.player_list.update()
        self.player_list.update_animation()
        self.physics_engine.update()
        self.books1.update()
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.SPACE:
            self.player.change_y = MOVEMENT_SPEED
            if self.physics_engine.can_jump():
                self.player.change_y = sprite_jumping
        elif key == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED
        #elif key == arcade.key.LEFT:
            #self.player.change_x = -MOVEMENT_SPEED
       # elif key == arcade.key.RIGHT:
            #self.player.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.SPACE or key == arcade.key.DOWN:
            self.player.change_y = 0
        #elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
           # self.player.change_x = 0


def main():

    
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

    

if __name__ == "__main__":
    main()
