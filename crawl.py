import json
import requests


def reservoir_crawler(msg):
    url  = "https://www.taiwanstat.com/waters/latest"
    re   = requests.get(url)
    data = re.json()
    data = data[0]

    reservoir = []
    # 水庫名稱
    for d in data:
        reservoir.append(d)

    for r in reservoir:
        if msg in reservoir:
            name = data[str(msg)]["name"]
            volu = data[str(msg)]["volumn"]
            perc = data[str(msg)]["percentage"]
        else:
            continue

    content = ""
    content += f"名稱: {name}\n蓄水百分比: {perc}%\n有效蓄水量: {volu}"

    return content
