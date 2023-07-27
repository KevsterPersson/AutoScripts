import gc

from library import library_FurMark as lib_FurMark
import time
import pyautogui as pya
import global_var as gv

pya.FAILSAFE = False
pya.PAUSE = 3
furmark = lib_FurMark.FurMark()

# 循环次数设置
gv.count_max = 5  # 默认循环次数
gv.sleep_time = 300


def func_FurMark():
    # 等待
    time.sleep(3)
    print('FurMark测试', '\n')

    def run():
        furmark.find_icon_and_click('Pictures/common_win_button/search.png')
        furmark.keyboard_write('FurMark', 0.2)
        furmark.keyboard_press('enter', 60)
        furmark.check_icon_and_click('Pictures/FurMark/full_screen_off.png', 'Pictures/FurMark/full_screen_on.png')

        furmark.find_icon_and_click('Pictures/FurMark/test_on.png')
        furmark.find_icon_and_click('Pictures/FurMark/test_go.png')
        time.sleep(gv.sleep_time)
        furmark.keyboard_press('esc', 60)
        furmark.find_icon_and_click('Pictures/FurMark/quit.png')
        print('测试完成', '\n')

    gv.count_times = 1
    count = gv.count_times
    while count < gv.count_max:
        print('--- 第', count, '次 ---', '\n')
        run()
        count += 1

        gc.collect()
