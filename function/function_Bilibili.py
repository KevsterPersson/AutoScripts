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
    while gv.count_times_bilibili < gv.count_max_bilibili:
        print('--- 第', gv.count_times_bilibili, '次 ---', '\n')
        round_start = time.time()
        bilibili.webbrowser('https://www.bilibili.com/bangumi/play/ep703938?from_spmid=666.25.episode.0',
                            'https://www.bilibili.com/bangumi/play/ep761273?from_spmid=666.25.episode.0',
                            'https://www.bilibili.com/bangumi/play/ep764993?from_spmid=666.25.episode.0', 5)
        bilibili.move_to_and_double_click(1560, 1014)
        print('第', gv.count_times_bilibili % 3, '段视频播放', gv.video_sec_bilibili, '秒')
        time.sleep(gv.video_sec_bilibili)
        bilibili.move_to_and_double_click(1724, 1096)
        bilibili.find_icon_and_click('Pictures/EdgeBilibili/edge_button_close.png')

        # 计时器
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
