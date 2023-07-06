import tkinter as tk

root = tk.Tk()

root.title('免费观看电影解析')
root.geometry('800x300+500+350')
tk.Label(root,text='此处本来应该为一张图片',font='楷体').pack()

choose_frame=tk.LabelFrame(root)
choose_frame.pack(fill='both',pady=10)
tk.Label(choose_frame,text='选择接口',font=('楷体',20)).pack(side=tk.LEFT)

num_int_var=tk.IntVar()
num_int_var.set(1)

tk.Radiobutton(choose_frame,text='1号接口',variable=num_int_var,value=1).pack(side=tk.LEFT,padx=2)
tk.Radiobutton(choose_frame,text='2号接口',variable=num_int_var,value=2).pack(side=tk.LEFT,padx=2)
tk.Radiobutton(choose_frame,text='3号接口',variable=num_int_var,value=3).pack(side=tk.LEFT,padx=2)

input_frame=tk.LabelFrame(root)
input_frame.pack(pady=10,padx=1)

input=tk.StringVar
tk.Label(input_frame,text='选择网址',font=('楷体',20)).pack(side=tk.LEFT)
tk.Entry(input_frame,width=100,relief='flat',textvariable=input).pack(side=tk.LEFT,fill='both')

def show():
    num=num_int_var.get()
    url=input.get()
    if num==1:
        pass
    elif num==2:
        pass
    elif num==3:
        pass

tk.Button(root,text='解析',font=('黑体',15),relief='flat',bg='pink',command=show).pack(fill='both')



root.mainloop()

