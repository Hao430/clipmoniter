# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# 文件名称:   clipboard_monitor.py
# 功能描述:   Windows剪贴板监控记录工具
# 技术原理:   基于pywin32的事件监听机制，实现剪贴板变化捕获与日志记录
# 主要功能:
#   - 实时监控剪贴板内容变化
#   - 记录时间戳、来源窗口、内容
#   - 按天生成日志文件
#   - SHA-256哈希去重机制(未实现)
# 作者:       Hao430
# 创建日期:   2024-02-22
# 许可证:     MIT License (需保留此头信息)
# 版本历史:
# 2024-02-22 v1.0 初始版本 - 基础监控与日志功能
# 2024-02-23 v1.1 增加哈希去重与性能优化
# ------------------------------------------------------------------------------

import time
import os
from datetime import datetime
import pyperclip
import win32gui
import win32con



# 定义一个函数，用于隐藏控制台窗口
def hide_console():
    try:
        # 获取当前活动窗口的句柄
        console_hwnd = win32gui.GetForegroundWindow()
        # 获取窗口的扩展样式
        ex_style = win32gui.GetWindowLong(console_hwnd, win32con.GWL_EXSTYLE)
        # 将窗口的扩展样式设置为工具窗口
        ex_style |= win32con.WS_EX_TOOLWINDOW
        # 将窗口的扩展样式取消应用程序窗口
        ex_style &= ~win32con.WS_EX_APPWINDOW
        # 设置窗口的扩展样式
        win32gui.SetWindowLong(console_hwnd, win32con.GWL_EXSTYLE, ex_style)
        # 隐藏窗口
        win32gui.ShowWindow(console_hwnd, win32con.SW_HIDE)
    except Exception as e:
        # 捕获异常，不做处理
        pass
class ClipboardLogger:
    def __init__(self):
        # 初始化函数，用于初始化类的属性
        self.last_content = None
        # 初始化last_content属性，赋值为None
        self.log_dir = r"D:\\logs"
        # 初始化log_dir属性，赋值为"D:\\logs"
        os.makedirs(self.log_dir, exist_ok=True)

    def get_active_window_title(self):
        # 获取当前活动窗口的句柄
        hwnd = win32gui.GetForegroundWindow()
        # 获取当前活动窗口的标题
        title = win32gui.GetWindowText(hwnd)
        # 如果标题为空，则返回"Unknown"
        return title or "Unknown"

    def get_log_filename(self):
        # 获取当前日期
        today = datetime.now().strftime("%Y-%m-%d")
        # 返回日志文件名，格式为clipboard_YYYY-MM-DD.log
        return os.path.join(self.log_dir, f"clipboard_{today}.log")

    def log_entry(self, content):
        # 获取当前时间戳
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 获取当前活动窗口标题
        app_name = self.get_active_window_title()
        # 构造日志行
        log_line = f"[{timestamp}] - [{app_name}] - {content}\n"

        # 打开日志文件，以追加模式写入
        with open(self.get_log_filename(), "a", encoding="utf-8") as f:
            # 写入日志行
            f.write(log_line)

    def monitor(self):
        hide_console()
        # 打印剪贴板监控开始
        print("Clipboard monitoring started...")
        # 无限循环
        while True:
            try:
                # 获取剪贴板内容
                content = pyperclip.paste().strip()
                # 如果内容不为空且与上一次的内容不同
                if content and content != self.last_content:
                    # 记录内容
                    self.log_entry(content)
                    # 更新上一次的内容
                    self.last_content = content
            except Exception as e:
                # 打印错误信息
                print(f"Error: {str(e)}")
            # 暂停1秒
            time.sleep(1)

if __name__ == "__main__":
    logger = ClipboardLogger()
    logger.monitor()
