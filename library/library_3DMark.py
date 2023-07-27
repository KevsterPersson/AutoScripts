import gc
import time
import pyautogui as pya
import pydirectinput as pyd
import global_var as gv


class BenchMark:

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

    def move_to_and_click(self, x_axis, y_axis):
        pya.moveTo(x_axis, y_axis, 1)
        pya.click()
        time.sleep(1)

        x_axis = None
        y_axis = None
        del x_axis
        del y_axis
        gc.collect()

    def keyboard_write(self, content, sec):  # 键盘输入内容
        pya.write(content, sec)

        content = None
        del content
        gc.collect()