import pygame as pg
import sys

def main():
    pg.display.set_caption("はじめてのPygame")
    screen = pg.display.set_mode((800, 600))#画面サイズ設定
    clock = pg.time.Clock()
    font = pg.font.Font(None, 80)

    enn = pg.Surface((20, 20))#円の描画用の枠を作る
    pg.draw.circle(enn, (0, 0, 255), (10, 10), 10)#円の描画　色、中心座標
    enn.set_colorkey((0, 0, 0))

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        txt = font.render(str(tmr), True, (255, 255, 255))
        screen.fill((50, 50, 50))
        screen.blit(txt, [300, 200])
        screen.blit(enn, [100, 400])
        pg.display.update()
        tmr += 1        
        clock.tick(3)#while文が1秒に回る回数


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()