from library import library_2077 as lib_2077
import time
import pyautogui as pya
import global_var as gv

pya.FAILSAFE = False
pya.PAUSE = 3
cyberpunk = lib_2077.Cyberpunk()

# 循环次数设置
gv.count_max = 3  # 默认外循环次数
gv.sub_count_max = 3  # 默认内循环次数


def func_cyberpunk():
    # 等待
    time.sleep(2)
    print('赛博朋克2077', '\n')

    # 测试项 外循环
    gv.count_times = 1
    count = gv.count_times
    while count < gv.count_max:
        count += 1
        round_start = time.time()
        print('--- 外循环第', count - 1, '轮 ---', '\n')
        time.sleep(3)

        # 找到游戏
        cyberpunk.find_icon_and_click('Pictures/common_win_button/houtai.png')
        cyberpunk.find_icon_and_double_click('Pictures/common_win_button/houtai_steam.png')
        cyberpunk.check_button_state('Pictures/common_steam_button/ku_CN.png',
                                     'Pictures/common_steam_button/ku_clicked_CN.png')
        cyberpunk.find_icon_and_click('Pictures/common_steam_button/testlist.png')
        cyberpunk.find_icon_and_click('Pictures/common_steam_button/testlist_cyberpunk.png')
        cyberpunk.find_icon_and_click('Pictures/common_steam_button/cyberpunk_start_CN.png')

        # 启动游戏
        time.sleep(10)
        cyberpunk.absolute_click(816, 537, 35)
        print('进入游戏', '\n')
        cyberpunk.keyboard_press('space', 4)
        cyberpunk.keyboard_press('space', 3)

        # 测试项 内循环
        sub_count = 1
        while sub_count < gv.sub_count_max:  # 设置测试次数
            print('&&&', '内循环第', sub_count, '回', '&&&', '\n')
            cycle_start = time.time()
            cyberpunk.click_and_click()
            cyberpunk.keyboard_press('left', 1)
            cyberpunk.keyboard_press('down', 1)
            cyberpunk.keyboard_press('enter', 1)
            print('打开设置', '\n')
            cyberpunk.keyboard_press('b', 92)
            print('开始测试', '\n')
            cyberpunk.keyboard_press('f12', 1)
            print('截图完成', '\n')
            cyberpunk.keyboard_press('esc', 1)
            cyberpunk.keyboard_press('enter', 25)
            cyberpunk.keyboard_press('space', 6)
            cyberpunk.keyboard_press('space', 6)
            cycle_finish = time.time()
            cycle_time = cycle_finish - cycle_start
            print('内循环第', sub_count, '回耗时', round(cycle_time), '秒')
            sub_count += 1
            cycle_record = cycle_time
            cycle_full_time = cycle_record + cycle_time
            if sub_count == gv.sub_count_max:
                print('内循环', gv.sub_count_max - 1, '次，总耗时', round(cycle_full_time - cycle_time), '秒', '\n')

        # 退出游戏
        cyberpunk.keyboard_press('left', 1)
        cyberpunk.keyboard_press('down', 1)
        cyberpunk.keyboard_press('down', 1)
        cyberpunk.keyboard_press('down', 1)
        cyberpunk.keyboard_press('down', 1)
        print('退出游戏', '\n')
        cyberpunk.keyboard_press('enter', 10)

        # 关闭窗口
        cyberpunk.find_icon_and_click('Pictures/common_steam_button/close_steam_window.png')

        # 计时器
        round_finish = time.time()
        round_time = round_finish - round_start
        time.sleep(3)
        print('外循环耗时', round(round_time), '秒', '\n')
        round_record = round_time
        round_full_time = round_record + round_time
        if count == gv.count_max:
            print('外循环', gv.count_max - 1, '次，总耗时', round(round_full_time - round_time), '秒', '\n')
