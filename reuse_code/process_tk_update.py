import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk() # 创建主窗口对象

progressbar = ttk.Progressbar(root, maximum=100)
progressbar.pack(fill=tk.X, expand=1)

for i in range(101):
    progressbar["value"] = i*10
    root.update() # 强制更新GUI状态
    # 模拟任务执行过程
    time.sleep(0.1)

root.mainloop() # 启动主事件循环