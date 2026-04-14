import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #練習１
    kk_img = pg.image.load("fig/3.png") #練習３
    kk_img = pg.transform.flip(kk_img, True, False) #練習３ 反転
    bg_img2 = pg.transform.flip(bg_img, True, False) #練習８ 反転
    kk_rct = kk_img.get_rect() #練習10 : こうかとんのRectの取得
    kk_rct.center = 300, 200 #こうかとんの初期座標の設定
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        key_lst = pg.key.get_pressed() #練習10
        # print(key_lst)
        if key_lst[pg.K_RIGHT] == False:
            kk_rct.move_ip((-1, 0))
        if key_lst[pg.K_UP]:
            kk_rct.move_ip((0, -1))
        if key_lst[pg.K_DOWN]:
            kk_rct.move_ip((0, +1))
        if key_lst[pg.K_LEFT]:
            kk_rct.move_ip((-1, 0))
        if key_lst[pg.K_RIGHT]:
            kk_rct.move_ip((+1, 0))


        x = tmr%3200 #練習５ #練習９ %3200追加
        screen.blit(bg_img, [-x, 0]) #練習２
        screen.blit(bg_img2, [-x+1600, 0]) #練習７　こちらを先に書かないとこうかとん消える
        screen.blit(bg_img, [-x+3200, 0])
        # screen.blit(kk_img, [300, 200]) #練習４
        screen.blit(kk_img, kk_rct) #練習10
        pg.display.update()
        tmr += 1        
        clock.tick(200) #練習６


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()