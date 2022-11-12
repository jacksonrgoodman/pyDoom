import pygame as pg
import sys
from data.settings import *
from data.debug import *
from data.map import *
from data.player import *
from data.raycasting import *
from data.object_renderer import *

generic_icon = "data\images\icon.png"
caption = "pyDOOM"


class Game:
    def __init__(self):
        # ? Game Setup
        pg.init()
        pg.display.set_icon(pg.image.load(generic_icon))
        pg.display.set_caption(caption)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        # fps_debug(f'FPS:{self.clock.get_fps() : .1f}')

    def draw(self):
        self.screen.fill("black")
        self.object_renderer.draw()
        # self.map.draw()
        # self.player.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                print("EXITING", caption)
                sys.exit()

    def run(self):
        # self.screen.fill("black")
        while True:
            self.check_events()
            self.update()
            self.draw()
            debug("RUNNING "+__name__+".py")
            fps_debug(f'FPS:{self.clock.get_fps() : .1f}', WIDTH)


if __name__ == '__main__':
    game = Game()
    game.run()
