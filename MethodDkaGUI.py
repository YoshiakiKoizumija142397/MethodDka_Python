import tkinter as tk
from tkinter import messagebox, scrolledtext
from decimal import Decimal, getcontext
from MethodDka import method_dka

# 高精度設定
getcontext().prec = 50

# 公式ページのテーマカラー
PRIMARY = "#0078D4"      # Microsoft Fluent Blue
PRIMARY_HOVER = "#106EBE"
BG = "#FFFFFF"
TEXT = "#000000"
ENTRY_BG = "#F3F3F3"
BORDER = "#D0D0D0"

class MethodDkaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MethodDka GUI（公式ページ統一デザイン）")
        self.root.configure(bg=BG)

        # 共通フォント
        self.font_normal = ("Segoe UI", 11)
        self.font_title = ("Segoe UI", 14, "bold")

        # タイトル
        tk.Label(root, text="MethodDka GUI", font=self.font_title, bg=BG, fg=TEXT).pack(pady=(10, 5))

        # 最高次数
        tk.Label(root, text="最高次数", font=self.font_normal, bg=BG).pack()
        self.degree_entry = tk.Entry(root, width=10, font=self.font_normal, bg=ENTRY_BG, relief="flat")
        self.degree_entry.pack(pady=(0, 10))

        # ボタン（公式ページ風）
        self.create_button = tk.Button(
            root, text="係数入力欄を作成",
            font=self.font_normal,
            bg=PRIMARY, fg="white",
            activebackground=PRIMARY_HOVER,
            relief="flat",
            command=self.create_fields
        )
        self.create_button.pack(pady=(0, 10))

        # 係数入力欄フレーム
        self.coeff_frame = tk.Frame(root, bg=BG)
        self.coeff_frame.pack()

        # 計算ボタン
        self.calc_button = tk.Button(
            root, text="計算開始",
            font=self.font_normal,
            bg=PRIMARY, fg="white",
            activebackground=PRIMARY_HOVER,
            relief="flat",
            command=self.calculate
        )
        self.calc_button.pack(pady=(10, 10))

        # 結果表示
        self.result_box = scrolledtext.ScrolledText(
            root, width=60, height=15,
            font=self.font_normal,
            bg=ENTRY_BG, relief="flat"
        )
        self.result_box.pack(pady=(0, 10))

    def create_fields(self):
        for widget in self.coeff_frame.winfo_children():
            widget.destroy()

        try:
            self.n = int(self.degree_entry.get())
        except Exception:
            messagebox.showerror("エラー", "最高次数を整数で入力してください。")
            return

        self.coeff_entries = []

        for i in range(self.n + 1):
            tk.Label(
                self.coeff_frame,
                text=f"{self.n - i} 次の係数",
                font=self.font_normal,
                bg=BG
            ).grid(row=i, column=0, padx=5, pady=3, sticky="e")

            entry = tk.Entry(
                self.coeff_frame,
                width=20,
                font=self.font_normal,
                bg=ENTRY_BG,
                relief="flat"
            )
            entry.grid(row=i, column=1, padx=5, pady=3)
            self.coeff_entries.append(entry)

    def calculate(self):
        try:
            coeffs = [Decimal(entry.get() or "0") for entry in self.coeff_entries]
        except Exception:
            messagebox.showerror("エラー", "係数は数値で入力してください。")
            return

        # ボタンを無効化し、セーフティロック稼働中であることを明示
        self.calc_button.config(state="disabled", text="計算中（セーフティロック: 最大1万回）...")
        self.root.update()  # 画面表示を即時更新

        # DKA法を実行（最大反復回数を1万回に設定して呼び出し）
        roots = method_dka(coeffs, max_iter=10000)

        # ボタンの状態を通常（最初）に戻す
        self.calc_button.config(state="normal", text="計算開始")
        self.result_box.delete("1.0", tk.END)

        # 収束しなかった場合のバグ・考慮漏れ対応
        if roots is None:
            messagebox.showwarning(
                "計算失敗", 
                "セーフティロックの上限（10000回）以内に収束しませんでした。\n"
                "係数の値を見直してください。"
            )
            self.result_box.insert(tk.END, "【警告】セーフティロック上限（10000回）に達したため計算を終了しました。\n")
            return  # ここで処理を抜け、GUIは最初の入力待ち状態を維持します

        # 収束した場合の結果表示
        for i, (re, im) in enumerate(roots, start=1):
            self.result_box.insert(
                tk.END,
                f"解 {i}: 実数部 = {re}, 虚数部 = {im}\n"
            )

# 実行
if __name__ == "__main__":
    root = tk.Tk()
    app = MethodDkaGUI(root)
    root.mainloop()
