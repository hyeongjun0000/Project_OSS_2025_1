import tkinter as tk
from decimal import Decimal, getcontext
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("계산기")
        self.label = tk.Label(master, text="숫자를 입력하세요 (예: 파이의 몇 번째 소수점 자릿수?)")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.calc_button = tk.Button(master, text="계산", command=self.calculate)
        self.calc_button.pack()
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def calculate(self):
        try:
            n = int(self.entry.get())
            if n <= 0 or n > 1000:
                self.result_label.config(text="1~1000 사이 숫자를 입력하세요.")
                return
            getcontext().prec = n + 5
            pi = str(Decimal(math.pi))
            if '.' not in pi:
                self.result_label.config(text="파이 값 계산 실패")
                return
            decimals = pi.split('.')[1]
            if len(decimals) < n:
                self.result_label.config(text="정밀도 부족")
            else:
                digit = decimals[n - 1]
                self.result_label.config(text=f"파이 소수점 {n}번째 자리: {digit}")
        except ValueError:
            self.result_label.config(text="유효한 숫자를 입력하세요.")
