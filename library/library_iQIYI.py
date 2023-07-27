import gc
import time
import pyautogui as pya
import pydirectinput as pyd
import global_var as gv


class iQIYI:

    def find_icon_and_click(self, path):  # 在屏幕中寻找Path路径下的图标，然后鼠标左键点击一次
        find_location = pya.locateCenterOnScreen(path, confidence=0.95)
        pya.click(find_location, duration=1)

        find_location = None
        del find_location
        gc.collect()

    def media_player(self, path1, path2, path3, path4):
        find_location1 = pya.locateCenterOnScreen(path1, confidence=0.95)  # 1_unclick
        find_location2 = pya.locateCenterOnScreen(path2, confidence=0.95)  # 1_clicked
        find_location3 = pya.locateCenterOnScreen(path3, confidence=0.95)  # 2_unclick
        find_location4 = pya.locateCenterOnScreen(path4, confidence=0.95)  # 2_clicked
        if find_location1:
            if find_location4:
                pya.click(find_location1, duration=1)
                time.sleep(3)
            else:
                pya.click(find_location1, duration=1)
                time.sleep(3)
        elif find_location2:
            if find_location3:
                pya.click(find_location3, duration=1)
                time.sleep(3)
            else:
                pya.click(find_location3, duration=1)
                time.sleep(3)
        else:
            if find_location1:
                pya.click(find_location1, duration=1)
                time.sleep(3)
            elif find_location3:
                pya.click(find_location3, duration=1)
                time.sleep(3)

        find_location1 = None
        find_location2 = None
        find_location3 = None
        find_location4 = None
        del find_location1
        del find_location2
        del find_location3
        del find_location4
        gc.collect()

    def find_icon_and_right_click(self, path):
        find_location = pya.locateCenterOnScreen(path, confidence=0.95)
        pya.rightClick(find_location, duration=1)

        find_location = None
        del find_location
        gc.collect()

    def check_popup_window(self, path):  # 判断是否有Path路径的图标，然后点击Path路径的图标，通常用来关闭弹窗
        check_icon = pya.locateCenterOnScreen(path, confidence=0.7)
        if check_icon:
            pya.click(check_icon, duration=1)
            time.sleep(1)
        else:
            pya.click(check_icon, duration=1)
            time.sleep(1)

        check_icon = None
        del check_icon
        gc.collect()

    def check_media_play(self, path1, path2):  # 检查Path路径下的图标是否存在，通常用来检查播放器是否正在播放，如果在播放则无操作，如果没有播放则点击播放
        check_icon1 = pya.locateCenterOnScreen(path1)
        check_icon2 = pya.locateCenterOnScreen(path2)
        if check_icon1:
            pya.click(check_icon1, duration=1)
        elif check_icon2:
            time.sleep(2)

        check_icon1 = None
        check_icon2 = None
        del check_icon1
        del check_icon2
        gc.collect()

    def wait_for_game_update(self, path1, path2,
                             path3):  # 等待游戏更新，Path1是“请求更新”功能图标，Path2是“正在下载”功能图标，Path3是完成下载后“开始游戏”功能图标
        wait_icon1 = pya.locateCenterOnScreen(path1, confident=0.9)
        wait_icon2 = pya.locateCenterOnScreen(path2, confident=0.9)
        wait_icon3 = pya.locateCenterOnScreen(path3, confident=0.9)
        if wait_icon1:
            pya.click(wait_icon1, duration=1)
            while wait_icon2:
                if wait_icon3:
                    pya.click(wait_icon3, duration=1)
                else:
                    time.sleep(5)

        wait_icon1 = None
        wait_icon2 = None
        wait_icon3 = None
        del wait_icon1
        del wait_icon2
        del wait_icon3
        gc.collect()

    def mouse_move_and_click(self, x1_axis, y1_axis, x2_axis, y2_axis, x3_axis, y3_axis):
        count = gv.count_times
        if (count % 3) == 1:
            pya.moveTo(x1_axis, y1_axis, 1)
            pya.click(x1_axis, y1_axis, duration=1)
        elif (count % 3) == 2:
            pya.moveTo(x2_axis, y2_axis, 1)
            pya.click(x2_axis, y2_axis, duration=1)
        elif (count % 3) == 0:
            pya.moveTo(x3_axis, y3_axis, 1)
            pya.click(x3_axis, y3_axis, duration=1)
        else:
            pya.moveTo(x1_axis, y1_axis, 1)
            pya.click(x1_axis, y1_axis, duration=1)

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

    def move_mouse(self, x_axis, y_axis, sec):
        pya.moveTo(x_axis, y_axis, sec)
        time.sleep(1)

        x_axis = None
        y_axis = None
        sec = None
        del x_axis
        del y_axis
        gc.collect()

    def mouse_click(self):
        pya.click()
        time.sleep(1)

        gc.collect()

    def mouse_double_click(self):
        pya.doubleClick()
        time.sleep(1)

        gc.collect()

    def keyboard_write(self, content, sec):  # 键盘输入内容
        pya.write(content, sec)
        time.sleep(1)

        content = None
        sec = None
        del content
        del sec
        gc.collect()

    def keyboard_press(self, content):
        pya.press(content)
        time.sleep(3)

        content = None
        del content
        gc.collect()
