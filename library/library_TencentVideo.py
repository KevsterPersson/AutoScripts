import gc
import time
import pyautogui as pya
import pydirectinput as pyd
import global_var as gv


class TencentVideo:

    def find_icon_and_click(self, icon_path):  # 在屏幕中寻找Path路径下的图标，然后鼠标左键点击一次
        find_location = pya.locateCenterOnScreen(icon_path, confidence=0.9)
        if find_location:
            pya.click(find_location, duration=0.5)
        elif find_location is None:
            print('未定位到坐标')

        find_location = None
        del find_location
        gc.collect()

    def select_video(self, x1_axis, y1_axis, x2_axis, y2_axis, x3_axis, y3_axis):
        if (gv.tencent_count_times % 3) == 1:
            pya.click(x1_axis, y1_axis, duration=0.5)
            print('1')
        elif (gv.tencent_count_times % 3) == 2:
            pya.click(x2_axis, y2_axis, duration=0.5)
            print('2')
        elif (gv.tencent_count_times % 3) == 0:
            pya.click(x3_axis, y3_axis, duration=0.5)

        x1_axis, y1_axis, x2_axis, y2_axis, x3_axis, y3_axis = None, None, None, None, None, None
        del x1_axis, y1_axis, x2_axis, y2_axis, x3_axis, y3_axis
        gc.collect()

    def keyboard_write_press(self, write_content, write_sec, press_content, wait_sec):
        pya.write(write_content, write_sec)
        pya.press(press_content, wait_sec)

        write_content = None
        write_sec = None
        press_content = None
        wait_sec = None
        del write_content, write_sec, press_content, wait_sec
        gc.collect()

    def move_to_click(self, x_axis, y_axis, move_speed, sleep_sec):
        pya.moveTo(x_axis, y_axis, move_speed)
        pya.click()
        time.sleep(sleep_sec)

        x_axis = None
        y_axis = None
        move_speed = None
        sleep_sec = None
        del x_axis, y_axis, move_speed, sleep_sec
        gc.collect()

    def move_to_right_click(self, icon_path):
        find_location = pya.locateCenterOnScreen(icon_path, confidence=0.9)
        pya.moveTo(find_location, duration=0.5)
        pya.rightClick()

        icon_path = None
        del icon_path
        gc.collect()

    def keyboard_press(self, press_content, wait_sec):
        pya.press(press_content, wait_sec)

        press_content = None
        wait_sec = None
        del press_content, wait_sec
