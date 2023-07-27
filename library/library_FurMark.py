import gc
import time
import pyautogui as pya
import pydirectinput as pyd
import global_var as gv


class FurMark:

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

    def check_icon_and_click(self, path1_click, path2_pass):
        find_location1 = pya.locateCenterOnScreen(path1_click, confidence=0.9)
        find_location2 = pya.locateCenterOnScreen(path2_pass, confidence=0.9)
        if find_location1:
            pya.click(find_location1, duration=0.5)
            # print(find_location)
        elif find_location2:
            pass

        find_location1 = None
        find_location2 = None
        del find_location1, find_location2

    def keyboard_write(self, content, sec):  # 键盘输入内容
        pya.write(content, sec)

        content = None
        del content
        gc.collect()

    def keyboard_press(self, content, sleep_sec):
        pya.press(content)
        time.sleep(sleep_sec)

        content = None
        del content
        gc.collect()
