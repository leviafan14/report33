import requests
import json
from datetime import datetime


def send_get_request(url: str, raw_deal_id: str, access_token: str):
    deal_id = raw_deal_id.replace(" ", "")

    # Формируем данные для запроса
    request_data = {
        "actions": [
            {
                "action": "get",
                "name": "get_deal",
                "params": {
                    "$embeds": [
                        "status_id",
                        "client_recommendation_id"
                    ],
                    "id": f"e:deals:{deal_id}"
                }
            }
        ]
    }

    # Отправляем GET-запрос
    response = requests.post(url,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        },
        data=json.dumps(request_data)
    )

    # Проверяем результат
    if response.status_code == 200:
        recom = response.json()
        raw_inserted_at = recom['get_deal']['result']['embeds']['client_recommendation_id']['values']['from_date']
        inserted_at = datetime.fromisoformat(raw_inserted_at).date()
        return inserted_at
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)


url = "https://crm.talisman-online.ru/api/v1/batch"
access_token = ""

if __name__ == "__main__":
    # Вызываем функцию
    print(send_get_request(url, "411864", access_token))