import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("주식 물타기 계산기")

        self.label1 = tk.Label(master, text="기존 주식 평단가:")
        self.label1.pack()
        self.avg_price_entry = tk.Entry(master)
        self.avg_price_entry.pack()

        self.label2 = tk.Label(master, text="기존 주식 수량:")
        self.label2.pack()
        self.qty_entry = tk.Entry(master)
        self.qty_entry.pack()

        self.label3 = tk.Label(master, text="현재 매수 주식 가격:")
        self.label3.pack()
        self.current_price_entry = tk.Entry(master)
        self.current_price_entry.pack()

        self.label4 = tk.Label(master, text="현재 매수 수량:")
        self.label4.pack()
        self.current_qty_entry = tk.Entry(master)
        self.current_qty_entry.pack()

        self.calc_button = tk.Button(master, text="계산", command=self.calculate)
        self.calc_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def calculate(self):
        try:
            avg_price = float(self.avg_price_entry.get())
            qty = float(self.qty_entry.get())
            current_price = float(self.current_price_entry.get())
            current_qty = float(self.current_qty_entry.get())

            total_qty = qty + current_qty
            if total_qty == 0:
                self.result_label.config(text="총 수량이 0입니다.")
                return
            total_cost = avg_price * qty + current_price * current_qty
            new_avg = total_cost / total_qty

            self.result_label.config(text=f"물타기 후 평단가: {new_avg:.2f}원\n총 수량: {total_qty:.0f}주")
        except ValueError:
            self.result_label.config(text="올바른 숫자를 입력하세요.")

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
