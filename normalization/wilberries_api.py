import requests

def get_wildberries_data(product_name):
    url = "https://search.wb.ru/exactmatch/ru/common/v4/search"
    params = {
        "query": product_name,
        "resultset": "catalog",
        "limit": 1
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print(data)
        if data.get("data", {}).get("products"):
            product = data["data"]["products"][0]
            return {
                "Название": product.get("name"),
                "Артикул": product.get("id"),
                "Производитель": product.get("brand"),
            }
    return None

result = get_wildberries_data("Ноутбук HP 15s-fq2023ur")
print(result)