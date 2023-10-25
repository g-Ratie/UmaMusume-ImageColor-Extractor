# Uma Musume Image Color Extractor

## 必要な環境

- Python 3.x
- Playwright
- PIL (Pillow)
- requests

## インストール

必要なパッケージをインストールします。

```bash
pip install requirements.txt
```

Playwrightのブラウザバイナリをダウンロードします。

```bash
playwright install
```

## 使い方

1. `main.py` を実行します。

    ```bash
    python main.py
    ```

2. `images` フォルダにウマ娘の画像がダウンロードされます。

3. `umamusume_color.json` ファイルが生成され、各ウマ娘の主要な色情報が保存されます。

## 出力形式

`umamusume_color.json` ファイルには以下のような形式で色情報が保存されます。

```json
{
  "ウマ娘の名前": {
    "subcolor": "(R, G, B)",
    "maincolor": "(R, G, B)"
  },
}
```

