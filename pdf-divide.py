import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from pypdf import PdfReader, PdfWriter

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("サンプル")

        self.create_widgets()

    def create_widgets(self):
        # Frame1の作成
        frame1 = ttk.Frame(self.root, padding=10)
        frame1.grid(row=0, column=1, sticky=E)

        # 「ファイル参照」ラベルの作成
        IFileLabel = ttk.Label(frame1, text="変換元参照＞＞", padding=(5, 2))
        IFileLabel.pack(side=LEFT)

        # 「ファイル参照」エントリーの作成
        self.entry1 = StringVar()
        IFileEntry1 = ttk.Entry(frame1, textvariable=self.entry1, width=30)
        IFileEntry1.pack(side=LEFT)

        # 「ファイル参照」ボタンの作成
        IFileButton1 = ttk.Button(frame1, text="参照", command=lambda: self.filedialog_clicked(self.entry1))
        IFileButton1.pack(side=LEFT)

        # Frame2の作成
        frame2 = ttk.Frame(self.root, padding=10)
        frame2.grid(row=1, column=1, sticky=E)

        # 「変換先参照」ラベルの作成
        IFileLabe2 = ttk.Label(frame2, text="変換先参照＞＞", padding=(5, 2))
        IFileLabe2.pack(side=LEFT)

        # 「変換先参照」エントリーの作成
        self.entry2 = StringVar()
        IFileEntry2 = ttk.Entry(frame2, textvariable=self.entry2, width=30)
        IFileEntry2.pack(side=LEFT)

        # 「変換先参照」ボタンの作成
        IFileButton2 = ttk.Button(frame2, text="参照", command=lambda: self.asksavefiledialog_clicked(self.entry2))
        IFileButton2.pack(side=LEFT)

        # Frame3の作成
        frame3 = ttk.Frame(self.root, padding=10)
        frame3.grid(row=2, column=1, sticky=E)

        # 「開始ページ」ラベルの作成
        startPageLabel = ttk.Label(frame3, text="開始ページ:", padding=(5, 2))
        startPageLabel.pack(side=LEFT)

        # 「開始ページ」エントリーの作成
        self.startPageEntry = StringVar()
        startPageEntryWidget = ttk.Entry(frame3, textvariable=self.startPageEntry, width=10)
        startPageEntryWidget.pack(side=LEFT)

        # 「終了ページ」ラベルの作成
        endPageLabel = ttk.Label(frame3, text="終了ページ:", padding=(5, 2))
        endPageLabel.pack(side=LEFT)

        # 「終了ページ」エントリーの作成
        self.endPageEntry = StringVar()
        endPageEntryWidget = ttk.Entry(frame3, textvariable=self.endPageEntry, width=10)
        endPageEntryWidget.pack(side=LEFT)

        # Frame4の作成
        frame4 = ttk.Frame(self.root, padding=10)
        frame4.grid(row=3, column=1, sticky=W)

        # 実行ボタンの設置
        button1 = ttk.Button(frame4, text="実行", command=self.conduct_main)
        button1.pack(fill="x", padx=30, side="left")

        # キャンセルボタンの設置
        button2 = ttk.Button(frame4, text="閉じる", command=self.root.quit)
        button2.pack(fill="x", padx=30, side="left")

    # ファイル指定の関数
    def filedialog_clicked(self, entry):
        fTyp = [("", "*")]
        iFile = os.path.abspath(os.path.dirname(__file__))
        iFilePath = filedialog.askopenfilename(filetype=fTyp, initialdir=iFile)
        entry.set(iFilePath)

    def asksavefiledialog_clicked(self, entry):
        fTyp = [("", "*")]
        iFile = os.path.abspath(os.path.dirname(__file__))
        iFilePath = filedialog.asksaveasfilename()
        entry.set(iFilePath)
        
    # 実行ボタン押下時の実行関数
    def conduct_main(self):
        filePath = self.entry1.get()
        savePath = self.entry2.get()
        startPage = self.startPageEntry.get()
        endPage = self.endPageEntry.get()

        if not filePath or not savePath or not startPage or not endPage:
            messagebox.showerror("error", "全ての入力フィールドを記入してください。")
            return

        try:
            startPage = int(startPage)
            endPage = int(endPage)
        except ValueError:
            messagebox.showerror("error", "ページ番号は整数でなければなりません。")
            return

        if startPage > endPage:
            messagebox.showerror("error", "開始ページは終了ページより小さくなければなりません。")
            return

        try:
            reader = PdfReader(filePath)
            writer = PdfWriter()
            
            writer.append(reader, pages=(startPage - 1, endPage))
            writer.write(savePath)
            messagebox.showinfo('info', '完了しました')
        except Exception as e:
            messagebox.showerror("error", f"エラーが発生しました: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    app = MainApp(root)
    root.mainloop()
