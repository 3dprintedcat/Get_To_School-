
import arcade
import random
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Move with a Sprite Animation Example"


MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        

        

        # Sprite lists
        self.player_list = None
        self.player_list = None

        # Set up the player
        self.score = 0
        self.player = None

    def setup(self):
        self.player_list = arcade.SpriteList()
       

        # Set up the player
        self.score = 0
        self.player = arcade.AnimatedWalkingSprite()

        character_scale = 0.75
        self.player.stand_right_textures = []
        self.player.stand_right_textures.append(arcade.load_texture("images/character_sprites/spr_0.png",
                                                                    scale=character_scale))
        self.player.stand_left_textures = []
        self.player.stand_left_textures.append(arcade.load_texture("images/character_sprites/spr_0.png",
                                                                   scale=character_scale, mirrored=True))

        self.player.walk_right_textures = []

        self.player.walk_right_textures.append(arcade.load_texture("images/character_sprites/spr_0.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("images/character_sprites/spr_1.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("images/character_sprites/spr_2.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("images/character_sprites/spr_3.png",
                                                                   scale=character_scale))

        self.player.walk_left_textures = []

        self.player.walk_left_textures.append(arcade.load_texture("images/character_sprites/spr_0.png",
                                                                  scale=character_scale, mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("images/character_sprites/spr_1.png",
                                                                  scale=character_scale, mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("images/character_sprites/spr_2.png",
                                                                  scale=character_scale, mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("images/character_sprites/spr_3.png",
                                                                  scale=character_scale, mirrored=True))

        self.player.texture_change_distance = 20

        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 2
        self.player.scale = 0.8

        self.player_list.append(self.player)

       
        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
       
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        """
        Called whenever the mouse moves.
        """
        if key == arcade.key.UP:
            self.player.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """
        Called when the user presses a mouse button.
        """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0

    def update(self, delta_time):
        """ Movement and game logic """

       
        self.player_list.update()
        self.player_list.update_animation()

        

       

def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
