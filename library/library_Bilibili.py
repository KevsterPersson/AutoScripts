import gc
import time
import pyautogui as pya
import pydirectinput as pyd
import global_var as gv

import webbrowser


class Bilibili:

    def webbrowser(self, url1, url2, url3, sleep_time):
        if gv.count_times_bilibili % 3 == 1:
            webbrowser.open(url1, autoraise=True)
            time.sleep(sleep_time)
        if gv.count_times_bilibili %3 == 2:
            webbrowser.open(url2, autoraise=True)
            time.sleep(sleep_time)
        if gv.count_times_bilibili %3 == 0:
            webbrowser.open(url3, autoraise=True)
            time.sleep(sleep_time)
        else:
            pass

        url1, url2, url3 = None, None, None
        del url1, url2, url3
        gc.collect()

    def find_icon_and_click(self, path):
        find_location = pya.locateCenterOnScreen(path, confidence=0.9)
        if find_location:
            pya.click(find_location, duration=0.5)
            # print(find_location)
        else:
            time.sleep(1)
            pass

        find_location = None
        del find_location
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
