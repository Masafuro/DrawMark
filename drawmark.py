import xml.etree.ElementTree as ET
import re
import tkinter as tk
from tkinter import filedialog

from rich import print
from rich.console import Console

def select_xml_file():
    """XMLファイルを選択し、そのファイルパスを返す関数"""
    root = tk.Tk()
    root.withdraw()  # Tkinterのメインウィンドウを非表示にする

    file_path = filedialog.askopenfilename(
        title="XMLファイルを選択",
        filetypes=[("XML Files", "*.xml")]  # XMLファイルのみ選択可能
    )

    return file_path

def save_md_file(content):
    """Tkinterのダイアログを使って.mdファイルの保存先を選択し、保存する"""
    root = tk.Tk()
    root.withdraw()  # Tkinterのウィンドウを非表示にする

    file_path = filedialog.asksaveasfilename(
        title="Markdownファイルを保存",
        defaultextension=".md",
        filetypes=[("Markdown Files", "*.md")]
    )

    if file_path:  # ファイル名が選択された場合のみ保存
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Markdown file '{file_path}' saved")


# XMLファイルを読み込む
xml_file = select_xml_file()  # XMLファイル名
tree = ET.parse(xml_file)
root = tree.getroot()


def extract_tags(value):
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', value)
    p_match = re.search(r'<p>(.*?)</p>', value)

    h1_text = h1_match.group(1) if h1_match else ""
    p_text = p_match.group(1) if p_match else ""

    return [h1_text, p_text]



# mxCellの抽出
cells = root.findall(".//mxCell")

# style要素に"text"を含むものだけを抽出
filtered_cells = [cell for cell in cells if "text" in cell.get("style", "")]


value_list = [cell.get("value", "") for cell in filtered_cells]
structured_list = [extract_tags(value) for value in value_list]

formatted_text = "\n\n".join(["\n\n".join(item) for item in structured_list])

# 結果を出力
print("DrawMark --drawio's Textbox to .md file.--")
print(f"\n=====\n{formatted_text}\n=====\n")
save_md_file(formatted_text)
