import gc
import time
import pyautogui as pya
import pydirectinput as pyd
import global_var as gv


class Bilibili:

    def find_icon_and_click(self, path):  # 在屏幕中寻找Path路径下的图标，然后鼠标左键点击一次
        find_location = pya.locateCenterOnScreen(path, confidence=0.95)
        if find_location:
            pya.click(find_location, duration=0.5)
            # print(find_location)
        else:
            time.sleep(1)
            pass

        find_location = None
        del find_location
        gc.collect()

    def get_position_and_move_to(self, path):
        get_position = pya.locateCenterOnScreen(path, confidence=0.95)
        pya.moveTo(get_position)
        time.sleep(1)

        get_position = None
        del get_position
        gc.collect()

    def check_button_state(self, path1, path2):  # 检查Path路径下的图标是否存在，通常用来检查播放器是否正在播放，如果在播放则无操作，如果没有播放则点击播放
        check_icon1 = pya.locateCenterOnScreen(path1, confidence=0.95)
        check_icon2 = pya.locateCenterOnScreen(path2, confidence=0.95)
        if check_icon1:
            pya.click(check_icon1, duration=0.5)
            time.sleep(1)
        elif check_icon2:
            time.sleep(1)

        check_icon1 = None
        check_icon2 = None
        del check_icon1
        del check_icon2
        gc.collect()

    def keyboard_write(self, content, sec1, sec2):  # 键盘输入内容
        pya.write(content, sec1)
        time.sleep(sec2)

        content = None
        del content
        gc.collect()

    def move_to_and_double_click(self, x_axis, y_axis):
        pya.moveTo(x_axis, y_axis, 1)
        pya.doubleClick()
        time.sleep(1)

        x_axis = None
        y_axis = None
        del x_axis
        del y_axis
        gc.collect()

    def keyboard_press(self, key, sleep_sec):
        pyd.press(key)
        time.sleep(sleep_sec)

        key = None
        del key
        gc.collect()

    def mouse_move_and_click(self, x1_axis, y1_axis, x2_axis, y2_axis, x3_axis, y3_axis):
        if (gv.count_times_bilibili % 3) == 1:
            pya.moveTo(x1_axis, y1_axis, 1)
            time.sleep(0.5)
            pya.click(x1_axis, y1_axis, duration=0.5)
            time.sleep(3)
            # print('开始播放第 1 段视频')
        elif (gv.count_times_bilibili % 3) == 2:
            pya.moveTo(x2_axis, y2_axis, 1)
            time.sleep(0.5)
            pya.click(x2_axis, y2_axis, duration=0.5)
            time.sleep(3)
            # print('开始播放第 2 段视频')
        elif (gv.count_times_bilibili % 3) == 0:
            pya.moveTo(x3_axis, y3_axis, 1)
            time.sleep(0.5)
            pya.click(x3_axis, y3_axis, duration=0.5)
            time.sleep(3)
            # print('开始播放第 3 段视频')
        else:
            pya.moveTo(x1_axis, y1_axis, 1)
            time.sleep(0.5)
            pya.click(x1_axis, y1_axis, duration=0.5)
            time.sleep(3)
            # print('开始播放第 1 段视频')

        x1_axis = None
        y1_axis = None
        del x1_axis
        del y1_axis
        x2_axis = None
        y2_axis = None
        del x2_axis
        del y2_axis
        x3_axis = None
        y3_axis = None
        del x3_axis
        del y3_axis
        gc.collect()
