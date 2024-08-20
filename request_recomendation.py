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
        raw_inserted_at = recom['get_deal']['result']['values']['inserted_at']
        inserted_at = datetime.fromisoformat(raw_inserted_at).date()
        return inserted_at
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)


url = "https://crm.talisman-online.ru/api/v1/batch"
access_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJpLmFzdGFzaG92IiwiZXhwIjoxNzI0MTY2OTkzfQ.QoyBfnPs3GTw39Y2H21l1zuvjkiITKSMk5aOZzSEjVT-7T2f540mmvBuGASrZ0VGwcjP9qtMBZ8oip0qoHitXffhU33tBGp7PHPaK6nHQzhywfR5RUmiTcrXXu9R_C4_L5vn9oPzMkbVNkXJhwbBNSZaZX7ThkgmhZ485XrJKh3YyiNAP-e89JA-URrPNQf8FmjKInXrYUSpSF6iLkzmwLqnlWECKGTdqHIbg_ysMbFWQe5Vg89Tjvr7CLlT6BzFpHXRQYFrSvsnq3VVvin0z5jEe3s5Puw4V2QHbRWbCLQA9dmout-_o4AmYoLnuMUPdIbL0ZLvSyz1GDaPZ9ZWriEeokoz6M4iu7iYSXHhuo0YWPyuit1ny2Vd9u1DA7JJgDRiu5q2dPSxjlXX_qWXYbT3RbOSBlqmeZm_cK57sScB_qD7dDNvvjiTYhy1z39gKCNUqjYcvQNLxZ6ICbnIE7FH07gSFAxeJdv5oQN10yQHdGFy_rGvFUk_9cyWkIF4ha5VursGsqU3GBl7RGaDWSGRBnAEWLaPVo6oZ_pbWIrEsKEDQaq4WCvGlDzoCy9GRW9vhWgSLoIMGqBYNTTVG6vLz29x3Q7yDAEXcfFqtMfHnSrz2qapG18mkDbBNWlfI4eysZlHL_s63Ic-IBzXyyqtNoBAIX8Z_2ylNKvdh0Y"


if __name__ == "__main__":
    # Вызываем функцию
    print(send_get_request(url, "431 759", access_token))