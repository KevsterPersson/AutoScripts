import gc

from library import library_TombRaider as lib_TombRaider
import time
import pyautogui as pya
import global_var as gv

pya.FAILSAFE = False
pya.PAUSE = 3
lora = lib_TombRaider.TombRaider()

# 循环次数设置
gv.count_max_TombRaider = 3  # 默认外循环次数
gv.sub_count_max_TombRaider = 3  # 默认内循环次数


def func_TombRaider():
    # 等待
    time.sleep(2)
    print('古墓丽影暗影', '\n')

    # 测试项 外循环
    gv.count_times_TombRaider = 1
    count = gv.count_times_TombRaider
    while count < gv.count_max_TombRaider:
        count += 1
        round_start = time.time()
        print('--- 第', count - 1, '轮 ---', '\n')

        # 打开steam
        lora.find_icon_and_click('Pictures/common_win_button/search.png')
        lora.keyboard_write('steam', 0.2)
        lora.keyboard_press('enter', 3)

        # 找到游戏
        lora.check_button_state('Pictures/common_steam_button/ku_CN.png',
                                'Pictures/common_steam_button/ku_clicked_CN.png')
        lora.find_icon_and_click('Pictures/common_steam_button/testlist.png')
        lora.find_icon_and_click('Pictures/common_steam_button/testlist_tombraider.png')
        lora.find_icon_and_click('Pictures/common_steam_button/cyberpunk_start_CN.png')

        # 启动游戏
        time.sleep(7)
        lora.absolute_click(952, 712, 11)
        print('进入游戏', '\n')
        lora.keyboard_press('enter', 6)
        lora.keyboard_press('down', 1)
        lora.keyboard_press('down', 1)
        lora.keyboard_press('down', 1)
        lora.keyboard_press('down', 1)
        lora.keyboard_press('enter', 2)
        lora.keyboard_press('down', 1)
        lora.keyboard_press('down', 1)
        lora.keyboard_press('down', 1)
        lora.keyboard_press('enter', 5)

        # 测试项 内循环
        sub_count = 1
        while sub_count < gv.sub_count_max_TombRaider:  # 设置测试次数
            print('&&&', '第', sub_count, '回', '&&&', '\n')
            cycle_start = time.time()
            lora.keyboard_press('r', 200)
            print('开始测试', '\n')
            lora.keyboard_press('f12', 2)
            print('截图完成', '\n')
            cycle_finish = time.time()
            cycle_time = cycle_finish - cycle_start
            print('第', sub_count, '回耗时', round(cycle_time), '秒', '\n')
            sub_count += 1
            cycle_record = cycle_time
            cycle_full_time = cycle_record + cycle_time
            if sub_count == gv.sub_count_max_TombRaider:
                print('内循环', gv.sub_count_max_TombRaider - 1, '次，总耗时', round(cycle_full_time - cycle_time), '秒', '\n')

        # 退出游戏
        lora.keyboard_press('esc', 5)
        lora.keyboard_press('esc', 3)
        lora.keyboard_press('down', 1)
        lora.keyboard_press('down', 1)
        lora.keyboard_press('down', 1)
        lora.keyboard_press('down', 1)
        lora.keyboard_press('down', 1)
        lora.keyboard_press('down', 1)
        lora.keyboard_press('enter', 1)
        print('退出游戏', '\n')
        lora.keyboard_press('enter', 10)

        # 关闭窗口
        lora.find_icon_and_click('Pictures/common_steam_button/close_steam_window.png')

        # 计时器
        round_finish = time.time()
        round_time = round_finish - round_start
        time.sleep(3)
        print('外循环耗时', round(round_time), '秒', '\n')
        round_record = round_time
        round_full_time = round_record + round_time
        if count == gv.count_max_TombRaider:
            print('外循环', gv.count_max_TombRaider - 1, '次，总耗时', round(round_full_time - round_time), '秒', '\n')

        cycle_start = None
        cycle_finish = None
        cycle_time = None
        cycle_record = None
        cycle_full_time = None
        round_start = None
        round_finish = None
        round_time = None
        round_record = None
        round_full_time = None
        del round_start, round_finish, round_time, round_record, round_full_time
        del cycle_start, cycle_finish, cycle_time, cycle_record, cycle_full_time
        gc.collect()
