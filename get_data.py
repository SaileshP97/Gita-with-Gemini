import pandas as pd
import requests
from bs4 import BeautifulSoup

url_list = [
    "https://vedabase.io/en/library/bg/setting-the-scene/",
    "https://vedabase.io/en/library/bg/preface/",
    "https://vedabase.io/en/library/bg/introduction/",
    "https://vedabase.io/en/library/bg/1/advanced-view/",
    "https://vedabase.io/en/library/bg/2/advanced-view/",
    "https://vedabase.io/en/library/bg/3/advanced-view/",
    "https://vedabase.io/en/library/bg/4/advanced-view/",
    "https://vedabase.io/en/library/bg/5/advanced-view/",
    "https://vedabase.io/en/library/bg/6/advanced-view/",
    "https://vedabase.io/en/library/bg/7/advanced-view/",
    "https://vedabase.io/en/library/bg/8/advanced-view/",
    "https://vedabase.io/en/library/bg/9/advanced-view/",
    "https://vedabase.io/en/library/bg/10/advanced-view/",
    "https://vedabase.io/en/library/bg/11/advanced-view/",
    "https://vedabase.io/en/library/bg/12/advanced-view/",
    "https://vedabase.io/en/library/bg/13/advanced-view/",
    "https://vedabase.io/en/library/bg/14/advanced-view/",
    "https://vedabase.io/en/library/bg/15/advanced-view/",
    "https://vedabase.io/en/library/bg/16/advanced-view/",
    "https://vedabase.io/en/library/bg/17/advanced-view/",
    "https://vedabase.io/en/library/bg/18/advanced-view/",
]


def get_df():
    gita_embedding = pd.DataFrame(columns=["text", "embedding"])
    purport_data_para = []

    for url in url_list:
        chapter = url.split("/")[6]
        if chapter.isnumeric():
            chapter = "Chapter " + chapter

        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")

            paragraphs = soup.find_all("p")

            purport_sent = ""

            for paragraph in paragraphs:
                text = paragraph.get_text()

                if len(purport_sent.split()) > 300:
                    purport_data_para.append(purport_sent)
                    purport_sent = ""
                if text.count(";") > 5:
                    continue
                else:
                    purport_sent += " " + text

        else:
            print("Error: Failed to retrieve the web page")

    gita_embedding["text"] = purport_data_para
    return gita_embedding
