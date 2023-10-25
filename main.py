import os
from playwright.sync_api import sync_playwright
import requests
from PIL import Image
from io import BytesIO
import json


def get_images():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://umamusume.jp/character/")

        img_elements = page.query_selector_all("ul.character__list li a img")

        # alt属性と画像URLを取得してダウンロード
        for img_element in img_elements:
            alt_text = img_element.get_attribute("alt")
            img_url = img_element.get_attribute("data-src")
            response = requests.get(img_url)
            img = Image.open(BytesIO(response.content))
            if not os.path.exists("images"):
                os.mkdir("images")
            img.save(f"images/{alt_text}.png")
            print(f"{alt_text}の画像を保存しました。")

        browser.close()


# 座標を受け取り、画像の色情報をJSONに変換する
def image_to_color_JSON(x1, y1, x2, y2):
    result = {}
    for file in os.listdir("images"):
        img = Image.open(f"images/{file}")
        subcolor = img.getpixel((x1, y1))[:3]  # RGBAからRGBに変換
        maincolor = img.getpixel((x2, y2))[:3]  # RGBAからRGBに変換
        umamusume_name = file.replace(".png", "")
        result[umamusume_name] = {"subcolor": subcolor, "maincolor": maincolor}
    with open("umamusume_color.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False)


x1 = 20
y1 = 190

x2 = 120
y2 = 190


if __name__ == "__main__":
    if not os.path.exists("images"):
        get_images()
    image_to_color_JSON(x1, y1, x2, y2)
