import gc
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
    time.sleep(10)
    print('爱奇艺客户端播放测试', '\n')

    # 测试
    gv.count_times_iQIYI = 1
    while gv.count_times_iQIYI < gv.max_count_iQIYI:
        print('--- 第', gv.count_times_iQIYI, '次 ---', '\n')
        iQIYI.webbrowser('https://www.iqiyi.com/v_10epeqee3vw.html?vfrm=pcw_home&vfrmblk=712211_dianshiju&vfrmrst=712211_dianshiju_image14',
                         'https://www.iqiyi.com/v_1sgk6wg53ms.html?vfrm=pcw_home&vfrmblk=712211_dianshiju&vfrmrst=712211_dianshiju_float_video_area1',
                         'https://www.iqiyi.com/v_s0lo1poj1k.html?vfrm=pcw_home&vfrmblk=712211_dianshiju&vfrmrst=712211_dianshiju_float_video_area3',
                         'https://www.iqiyi.com/v_13g23sh4cw4.html?vfrm=pcw_home&vfrmblk=712211_dianshiju&vfrmrst=712211_dianshiju_image6',
                         'https://www.iqiyi.com/v_dsb5mcling.html?vfrm=pcw_home&vfrmblk=712211_dianshiju&vfrmrst=712211_dianshiju_image9',
                         'https://www.iqiyi.com/v_1tb79lhcrts.html?vfrm=pcw_home&vfrmblk=712211_dianshiju&vfrmrst=712211_dianshiju_float_video_area12', 135)
        iQIYI.find_icon_and_click('Pictures/AIQIYI_Player/browser_close_popup_window.png')
        time.sleep(gv.sleep_time_iQIYI)  # 播放时长
        iQIYI.move_to_and_click(2536, 17)
        print('*** 第', gv.count_times_iQIYI, '次完成 ***', '\n')
        gv.count_times_iQIYI += 1

        gc.collect()
