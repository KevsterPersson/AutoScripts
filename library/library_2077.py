import gc
import time
import pyautogui as pya
import pydirectinput as pyd
import global_var as gv


class Cyberpunk:

    def find_icon_and_click(self, path):  # 在屏幕中寻找Path路径下的图标，然后鼠标左键点击一次
        find_location = pya.locateCenterOnScreen(path, confidence=0.95)
        if find_location:
            pya.click(find_location, duration=0.5)
            # print(find_location)
        else:
            print('没有定位到坐标')
            time.sleep(1)

        find_location = None
        del find_location

    def click_and_click(self):
        pyd.click(287, 755)
        time.sleep(1)

    def keyboard_press(self, key, sec):
        pyd.press(key)
        time.sleep(sec)

        key = None
        del key

    def absolute_click(self, x_axis, y_axis, sec):
        pyd.click(x_axis, y_axis)
        time.sleep(sec)

        x_axis = None
        y_axis = None
        sec = None
        del x_axis
        del y_axis
        del sec

    def find_icon_and_double_click(self, path):
        find_location = pya.locateCenterOnScreen(path, confidence=0.95)
        pya.doubleClick(find_location, duration=0.5)

        find_location = None
        del find_location

    def check_button_state(self, path1, path2):  # 检查Path路径下的图标是否存在，通常用来检查播放器是否正在播放，如果在播放则无操作，如果没有播放则点击播放
        check_icon1 = pya.locateCenterOnScreen(path1, confidence=0.95)
        check_icon2 = pya.locateCenterOnScreen(path2, confidence=0.95)
        if check_icon1:
            pya.click(check_icon1, duration=0.5)
        elif check_icon2:
            pya.click(check_icon2, duration=0.5)

        check_icon1 = None
        del check_icon1
        check_icon2 = None
        del check_icon2
