import gc
import time
import pyautogui as pya
import pydirectinput as pyd
import global_var as gv

import webbrowser


class iQIYI:

    def webbrowser(self, url1, url2, url3, url4, url5, url6, sleep_time):
        if gv.count_times_iQIYI % 6 == 1:
            webbrowser.open(url1, autoraise=True)
            time.sleep(sleep_time)
        if gv.count_times_iQIYI % 6 == 2:
            webbrowser.open(url2, autoraise=True)
            time.sleep(sleep_time)
        if gv.count_times_iQIYI % 6 == 3:
            webbrowser.open(url3, autoraise=True)
            time.sleep(sleep_time)
        if gv.count_times_iQIYI % 6 == 4:
            webbrowser.open(url4, autoraise=True)
            time.sleep(sleep_time)
        if gv.count_times_iQIYI % 6 == 5:
            webbrowser.open(url5, autoraise=True)
            time.sleep(sleep_time)
        if gv.count_times_iQIYI % 6 == 0:
            webbrowser.open(url6, autoraise=True)
            time.sleep(sleep_time)
        else:
            pass

        url1, url2, url3 = None, None, None
        url4, url5, url6, sleep_time = None, None, None, None
        del url1, url2, url3
        del url4, url5, url6, sleep_time
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

    def move_to_and_click(self, x_axis, y_axis):
        pya.moveTo(x_axis, y_axis, 1)
        pya.click()
        time.sleep(1)

        x_axis = None
        y_axis = None
        del x_axis
        del y_axis
        gc.collect()
