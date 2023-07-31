import time

from library import library_TencentVideo as lib_TencentVideo
import pyautogui as pya
import global_var as gv

pya.FAILSAFE = False
pya.PAUSE = 3
tencent = lib_TencentVideo.TencentVideo()

# 设置
gv.tencent_sleep_time = 200  # 默认播放时长设置
gv.tencent_max_count = 5  # 默认循环次数设置


def run():
    tencent.find_icon_and_click('Pictures/common_win_button/search.png')
    tencent.keyboard_write_press('tengxunshipin', 0.2, 'enter', 10)
    tencent.move_to_click(566, 493, 0.5, 10)
    tencent.find_icon_and_click('Pictures/TencentVideo/dianshiju.png')
    tencent.find_icon_and_click('Pictures/TencentVideo/mianfei.png')
    tencent.select_video(787, 663, 1014, 663, 1249, 663)
    tencent.move_to_click(1636, 1045, 0.5, 3)
    time.sleep(gv.tencent_sleep_time)
    tencent.keyboard_press('esc', 3)
    tencent.move_to_click(1931, 346, 0.5, 3)
    tencent.move_to_click(2048, 182, 0.5, 3)
    tencent.find_icon_and_click('Pictures/common_win_button/houtai.png')
    tencent.move_to_right_click('Pictures/TencentVideo/houtai_tencentvideo.png')
    tencent.find_icon_and_click('Pictures/TencentVideo/houtai_tencentvideo_exit.png')


def func_TencentVideo():
    time.sleep(2)
    print('腾讯视频', '\n')

    gv.tencent_count_times = 1
    count = gv.tencent_count_times
    while count < gv.tencent_max_count:
        print('--- 第', count, '次 ---', '\n')
        run()

        print('*** 完成 ***', '\n')
        count += 1
