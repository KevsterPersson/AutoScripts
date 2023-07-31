import time

from library import library_iQIYI as lib_iQIYI
import pyautogui as pya
import global_var as gv

pya.FAILSAFE = False
pya.PAUSE = 3
iQIYI = lib_iQIYI.iQIYI()

# 设置
gv.sleep_time_iQIYI = 200  # 默认播放时长设置
gv.max_count_iQIYI = 5  # 默认循环次数设置


def func_iQIYI():
    # 等待
    time.sleep(20)
    print('爱奇艺客户端播放测试', '\n')

    # 测试
    gv.count_times = 1
    count = gv.count_times_iQIYI
    while count < gv.max_count_iQIYI:
        print('--- 第', count, '次 ---', '\n')
        iQIYI.find_icon_and_click('Pictures/common_win_button/search.png')
        iQIYI.keyboard_write_press('aiqiyi', 0.2, 'enter', 10)
        iQIYI.check_popup_window('Pictures/AIQIYI_Player/aiqiyi_button_popup_window_close.png')  # 检查是否有弹窗
        iQIYI.find_icon_and_click('Pictures/AIQIYI_Player/aiqiyi_icon_dianshiju.png')  # 点击电视剧
        iQIYI.find_icon_and_click('Pictures/AIQIYI_Player/aiqiyi_icon_quanbujuji.png')  # 点击全部剧集
        iQIYI.find_icon_and_click('Pictures/AIQIYI_Player/aiqiyi_icon_zuire.png')  # 点击最热
        # 836,823 1036,823 1240,823
        iQIYI.mouse_move_and_click(836, 625, 1036, 625, 1240, 625)
        iQIYI.media_player('Pictures/AIQIYI_Player/aiqiyi_button_1_unclick.png',
                           'Pictures/AIQIYI_Player/aiqiyi_button_1_clicked.png',
                           'Pictures/AIQIYI_Player/aiqiyi_button_2_unclick.png',
                           'Pictures/AIQIYI_Player/aiqiyi_button_2_clicked.png')
        iQIYI.move_mouse(1456, 978, 1)
        iQIYI.mouse_click()
        time.sleep(gv.sleep_time_iQIYI)  # 播放时长
        iQIYI.move_mouse(2534, 1411, 1)
        iQIYI.mouse_click()  # 退出全屏
        print('结束播放', '\n')

        iQIYI.find_icon_and_click('Pictures/AIQIYI_Player/aiqiyi_button_player_close.png')
        iQIYI.find_icon_and_click('Pictures/AIQIYI_Player/aiqiyi_app_close_button.png')

        iQIYI.find_icon_and_click('Pictures/common_win_button/houtai.png')
        iQIYI.find_icon_and_right_click('Pictures/AIQIYI_Player/win_houtai_aiqiyi_icon.png')
        iQIYI.find_icon_and_click('Pictures/AIQIYI_Player/win_houtai_aiyiqi_exit.png')  # 退出爱奇艺
        print('*** 第', count, '次完成 ***', '\n')
        count += 1
