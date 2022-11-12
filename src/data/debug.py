import pygame as pg
pg.init()
font = pg.font.Font(None, 30)


def debug(info, y=10, x=10):
    display_surface = pg.display.get_surface()
    debug_surf = font.render(str(info), True, 'White')
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    pg.draw.rect(display_surface, 'Black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)


def fps_debug(info, x, y=10):
    offset = (x*.92)
    display_surface = pg.display.get_surface()
    debug_surf = font.render(str(info), True, 'White')
    debug_rect = debug_surf.get_rect(topleft=(offset, y))
    pg.draw.rect(display_surface, 'Black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)
