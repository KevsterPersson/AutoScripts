import gc
from library import library_Bilibili as lib_Bilibili
import time
import pyautogui as pya
import global_var as gv

pya.FAILSAFE = False
pya.PAUSE = 3
bilibili = lib_Bilibili.Bilibili()

# 设置
gv.video_sec_bilibili = 200  # 默认播放时长
gv.count_max_bilibili = 5  # 默认循环次数


def func_bilibili():
    # 等待
    time.sleep(2)
    print('哔哩哔哩', '\n')

    # 测试项
    gv.count_times_bilibili = 1
    # count = gv.count_times_bilibili
    while gv.count_times_bilibili < gv.count_max_bilibili:
        print('--- 第', gv.count_times_bilibili, '次 ---', '\n')
        round_start = time.time()
        time.sleep(3)
        bilibili.find_icon_and_click('Pictures/EdgeBilibili/win_button_search.png')
        bilibili.keyboard_write('Microsoft Edge', 0.2, 1)
        bilibili.keyboard_press('enter', 3)
        bilibili.check_button_state('Pictures/EdgeBilibili/edge_button_min_window.png',
                                    'Pictures/EdgeBilibili/edge_button_max_window_state.png')
        bilibili.find_icon_and_click('Pictures/EdgeBilibili/edge_search_button.png')
        bilibili.keyboard_write('bilibili.com', 0.2, 1)
        bilibili.keyboard_press('enter', 4)
        bilibili.find_icon_and_click('Pictures/EdgeBilibili/edge_bilibili_button_dianshiju.png')
        bilibili.mouse_move_and_click(1241, 682, 1494, 682, 1746, 682)
        bilibili.get_position_and_move_to('Pictures/EdgeBilibili/edge_bilibili_login_button.png')
        bilibili.get_position_and_move_to('Pictures/EdgeBilibili/edge_bilibili_button_sort.png')
        pya.moveTo(2251, 350, 1)
        pya.scroll(600)
        bilibili.check_button_state('Pictures/EdgeBilibili/edge_bilibili_button_1_unclick.png',
                                    'Pictures/EdgeBilibili/edge_bilibili_button_1_clicked.png')
        time.sleep(5)
        bilibili.move_to_and_double_click(1560, 1014)
        print('第', gv.count_times_bilibili % 3, '段视频播放', gv.video_sec_bilibili, '秒')
        time.sleep(gv.video_sec_bilibili)
        bilibili.move_to_and_double_click(1724, 1096)
        bilibili.find_icon_and_click('Pictures/EdgeBilibili/edge_button_max_window_state.png')
        bilibili.find_icon_and_click('Pictures/EdgeBilibili/edge_button_close.png')

        round_finish = time.time()
        round_time = round_finish - round_start
        print('测试耗时', round(round_time), '秒完成', '\n')
        gv.count_times_bilibili += 1
        round_record = round_time
        round_full_time = round_record + round_time
        round_total_time = round(round_full_time - round_time)
        if gv.count_times_bilibili == gv.count_max_bilibili:
            print('完成', gv.count_max_bilibili - 1, '次测试, ', '总耗时', round_total_time, '秒')

        round_start = None
        round_finish = None
        round_time = None
        round_record = None
        round_full_time = None
        round_total_time = None
        del round_start, round_finish, round_time, round_record, round_full_time, round_total_time
        gc.collect()
