import gc

from function import function_3DMark as func_3DMark, function_2077 as func_2077, function_Bilibili as func_Bilibili, \
    function_FurMark as func_FurMark, function_iQIYI as func_iQIYI, function_TombRaider as func_Raider, \
    function_TencentVideo as func_TencentVideo
import time
import global_var as gv


# 赛博朋克2077
def run_2077():
    gv.count_max_2077 = 5  # 设置外循环次数
    gv.sub_count_max_2077 = 10  # 设置内循环次数
    func_2077.func_cyberpunk()


# 哔哩哔哩
def run_Bilibili():
    gv.video_sec_bilibili = 2000  # 设置播放时长
    gv.count_max_bilibili = 2000  # 设置循环次数
    func_Bilibili.func_bilibili()


# 3DMark
def run_3DMark():
    gv.count_max_3DMark = 30  # 设置循环次数
    func_3DMark.func_3DMark()


# 爱奇艺
def run_iQIYI():
    gv.sleep_time_iQIYI = 1000  # 设置播放时长设置
    gv.max_count_iQIYI = 20  # 设置循环次数设置
    func_iQIYI.func_iQIYI()


# 古墓丽影暗影
def run_TombRaider():
    gv.count_max_TombRaider = 50  # 设置外循环次数
    gv.sub_count_max_TombRaider = 5  # 设置内循环次数
    func_Raider.func_TombRaider()


# FurMark
def run_FurMark():
    gv.count_max_FurMark = 200  # 设置循环次数
    gv.sleep_time_FurMark = 300  # 设置每次运行时长
    func_FurMark.func_FurMark()


# 腾讯视频
def run_TencentVideo():
    gv.tencent_sleep_time = 300  # 默认播放时长设置
    gv.tencent_max_count = 200  # 默认循环次数设置
    func_TencentVideo.func_TencentVideo()


if __name__ == "__main__":
    print('--- 开始 ---', '\n')

    # 计时器
    section_start = time.time()

    # run
    run_Bilibili()

    # 计时器
    section_finish = time.time()
    section_time = round(section_finish - section_start)
    print('总耗时', section_time, '秒', '\n')
    print('*** 测试结束 ***')

    section_start = None
    section_finish = None
    section_time = None
    del section_start, section_finish, section_time

    gc.collect()
