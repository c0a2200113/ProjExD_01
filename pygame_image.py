import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")#左上タイトル
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")#練習1背景画像Surface生成
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("ex01/fig/3.png")#練習2こうかとんのSurface生成
    kk_img = pg.transform.flip(kk_img, True, False)#練習2左右反転
    kk_img2 = pg.transform.rotozoom(kk_img, 2.5, 1.0)
    kk_img3 = pg.transform.rotozoom(kk_img, 5, 1.0)
    kk_img4 = pg.transform.rotozoom(kk_img, 7.5, 1.0)
    kk_img5 = pg.transform.rotozoom(kk_img, 10, 1.0)
    kk_imgs = [kk_img, kk_img2, kk_img3, kk_img4, kk_img5, kk_img4, kk_img3, kk_img2, kk_img]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%3200
        screen.blit(bg_img, [-x, 0])#練習4背景表示
        screen.blit(bg_img2, [1600-x, 0])#練習6動く背景画像
        screen.blit(bg_img, [3200-x, 0])
        screen.blit(kk_imgs[tmr%9], [300,200])#練習5こうかとん表示
        pg.display.update()
        tmr += 1
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()