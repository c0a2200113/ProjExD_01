import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")#左上タイトル
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")#練習1背景画像Surface生成
    kk_img = pg.image.load("ex01/fig/3.png")#練習2こうかとんのSurface生成
    kk_img = pg.transform.flip(kk_img, True, False)#練習2左右反転
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])#練習4背景表示
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()