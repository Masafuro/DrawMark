# DrawMark
DrawMark は、draw.ioの図をXMLとして保存し、Markdown形式に変換することで、開発ドキュメントの管理を効率化するツールです。

## 目的

色々と開発をするときに、往々にして、行ったり来たり彷徨った感じになる。そのような感じでそのまま開発記録をつけつつ、最終的にはマニュアルや振り返りに使いやすいマークダウンを同時に作れるような感じにしたかった。


## 使い方

[https://www.drawio.com/](https://www.drawio.com/)

1. drawioでTextboxを使ってなにか作る。このとき、マークダウン記法で書くものとする。
2. xmlエクスポートする。
3. drawmark.pyを実行すると読み込みダイアログがでるので、2のxmlファイルを読み込む。
4. 保存ダイアログで.mdファイルを保存する。

## 利用イメージ

- sample.xml

![image](https://github.com/user-attachments/assets/8318e244-1f18-4b13-9893-924c25982319)

- sample_output.md

![image](https://github.com/user-attachments/assets/588c38e9-85ef-4d0c-9a89-956e74c05622)

![image](https://github.com/user-attachments/assets/0f460293-7d26-4565-8491-8da6942c2c72)

