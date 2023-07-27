import gc

from library import library_3DMark as lib_3DMark
import time
import pyautogui as pya
import global_var as gv

pya.FAILSAFE = False
pya.PAUSE = 3
benchmark = lib_3DMark.BenchMark()

# 循环次数设置
gv.count_max = 5  # 默认循环次数


def run():
    benchmark.find_icon_and_click('Pictures/common_win_button/search.png')
    benchmark.keyboard_write('3DMark', 0.2)
    benchmark.find_icon_and_click('Pictures/Steam_3DMark/3dmark_win_enter.png')
    time.sleep(60)

    benchmark.move_to_and_click(840, 704)
    time.sleep(400)
    benchmark.find_icon_and_click('Pictures/Steam_3DMark/close.png')


def func_3DMark():
    time.sleep(3)
    print('3DMark测试', '\n')

    gv.count_times = 1
    count = gv.count_times
    while count < gv.count_max:
        print('--- 第', count, '次 ---', '\n')
        run()
        print('测试完成', '\n')
        count += 1

        gc.collect()
