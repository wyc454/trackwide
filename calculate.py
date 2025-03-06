import tkinter as tk
from tkinter import ttk
import math


class PCBTraceCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("PCB印制电路板线宽计算器")
        # 创建输入框和标签
        ttk.Label(root, text="电流 (A):").grid(row=0, column=0, padx=5, pady=5)
        self.current = ttk.Entry(root)
        self.current.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(root, text="温升 (°C):").grid(row=1, column=0, padx=5, pady=5)
        self.temp_rise = ttk.Entry(root)
        self.temp_rise.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(root, text="copper wide(oz):").grid(row=2, column=0, padx=5, pady=5)
        self.thickness = ttk.Entry(root)
        self.thickness.grid(row=2, column=1, padx=5, pady=5)

        # 计算按钮
        ttk.Button(root, text="calculate", command=self.calculate).grid(row=3, column=0, columnspan=2, pady=10)

        # 结果显示
        self.result_label = ttk.Label(root, text="")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=5)

    def calculate(self):
        try:
            current = float(self.current.get())
            temp_rise = float(self.temp_rise.get())
            thickness = float(self.thickness.get())
            width = (current / (0.048 * math.sqrt(temp_rise))) ** (1 / 0.44)
            width = width / (thickness / 1)  # 根据铜箔厚度调整这里是1oz

            # 转换为mm
            width_mm = width * 0.0254  # mil转mm ,10Mil=0.254mm

            self.result_label.config(text=f"suggest track wide: {width_mm:.2f} mm\n({width:.2f} mil)")
        except ValueError:
            self.result_label.config(text="请输入有效值")

#传入mian函数
if __name__ == "__main__":
    root = tk.Tk()
    app = PCBTraceCalculator(root)
    root.mainloop()
