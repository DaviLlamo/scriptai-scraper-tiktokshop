from playwright.sync_api import sync_playwright
from openpyxl import Workbook
import time
import os
from datetime import datetime


def pegar_videos(query):
    dados = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(f"https://www.tiktok.com/search?q={query}")
        time.sleep(7)

        videos = page.query_selector_all("a[href*='/video/']")

        links_usados = set()
        count = 0

        for video in videos:
            if count >= 5:
                break

            try:
                link = video.get_attribute("href")
                texto = video.inner_text()

                if not link or not texto:
                    continue

                if not link.startswith("http"):
                    link = "https://www.tiktok.com" + link

                if link in links_usados:
                    continue

                links_usados.add(link)

                dados.append({
                    "nome": texto[:80],
                    "link": link
                })

                count += 1

            except:
                continue

        browser.close()

    return dados


def salvar_excel(dados):
    wb = Workbook()
    ws = wb.active

    ws.append(["Nome", "Link"])

    for d in dados:
        ws.append([d["nome"], d["link"]])

    downloads = os.path.join(os.path.expanduser("~"), "Downloads")
    nome = f"tiktok_{datetime.now().strftime('%H-%M-%S')}.xlsx"
    caminho = os.path.join(downloads, nome)

    wb.save(caminho)
    return caminho