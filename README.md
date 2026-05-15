# MethodDka_Python
🌐 概要（Overview）
MethodDka GUI は、公式ページ（HTML版）と同じ操作感で
高精度多項式の解を求められるデスクトップアプリケーションです。

最高次数を入力すると係数入力欄が自動生成

「計算開始」ボタンで MethodDka を実行

結果はスクロール表示

高精度 Decimal 計算に対応

公式ページと同じ UI 構造（タイトル → 入力 → 実行 → 結果）

📁 フォルダ構成（Project Structure）
コード
MethodDka_Python/
├─ MethodDka.py        # MethodDka 本体（Python 移植版）
├─ MethodDkaGUI.py     # GUI アプリ（本 README の対象）
└─ venv/               # 仮想環境（任意）
重要：MethodDkaGUI.py と MethodDka.py は同じフォルダに置くこと。

▶️ 実行方法（Run）
1. コマンドプロンプトを開く
コード
Win + R → cmd
2. プロジェクトフォルダへ移動
コード
cd C:\Users\ja142\source\repos\YoshiakiKoizumija142397\MethodDka_Python
3. 仮想環境を有効化（任意）
コード
venv\Scripts\activate
4. GUI を起動
コード
python MethodDkaGUI.py
🖥 使い方（How to Use）
① 最高次数を入力
例：

コード
3
② 「係数入力欄を作成」
→ 3次 → 4つの係数入力欄が自動生成される

③ 係数を入力
例：

コード
1, 0, -1, 2
④ 「計算開始」
→ MethodDka が実行され、
→ 解がスクロールテキストに表示される

🧮 計算精度（Precision）
デフォルトは 50 桁：

python
getcontext().prec = 50
必要に応じて：

100 桁

200 桁

任意桁数

に変更可能。

⚠️ 注意事項（Notes）
MethodDka.py が同じフォルダにない場合、ImportError が発生します

係数は数値のみ（Decimal で処理）

虚数部が 0E-74 のように表示されるのは正常（高精度計算の仕様）

📜 MIT License
コード
MIT License

Copyright (c) 2024 Yoshiaki Koizumi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in  
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING  
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER  
DEALINGS IN THE SOFTWARE.
