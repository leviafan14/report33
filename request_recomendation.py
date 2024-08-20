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
access_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJpLmFzdGFzaG92IiwiZXhwIjoxNzI0MjExMTA4fQ.r2XfDh9IaQkfmgPa0EAAvjRJdqcR-1ddef5jMeERoKQuDOh9tc3H2M-Q-TRMLhvKkyumnmFTEhyY_ju3vNmhXTDdxWl49KvvEiUZ4J1jIINnEVccTqwi8-Pg3Kco0rccd-LN4m_n3M6DafYYCR3NrXOAMwllYooRRh1ErIo71-Su6nVzlZX5Cr8YcG3U-cVOsb_b9-zAYpPDaiq2VRKtVBxLsW2e3uptWofoIOL9Af-rtJkyd1FK5UCT9wZdfDk_mQqYqiv2aXHHGfkTqDEi2L8WsmhDN6liGq7vik1exQoaPKpd0FJMhrEKkcKUeapaQ8QUk6t4vb4Krg4zzJqJBhOB_BgVwvJvpRlRlIrRyFbK2KxHleG3zJ4tcIb9bsUnf9JGlmPqfli2awNZFHsUY3PmNUhyBY-fMv8oN2wEIKGSJvh9h6Fb-f35XyfsGXxZyup20ZtVbcTKuKDCiWztcDAYS20yzGJkE7zNRp5Oxv7OJvafMKmWnp5F9EGc447oew4NEmPw5w2yUEZrDHBw_YfsZ08Tr5Er2DYI5JapUU6iMkOvwVl9_n4-TVqKSDImukcoK1LTIzKzVJ9nhYJr0ztR1Xz838uktIw5Ois9p_DyXC1on634hVwwwVzUG01Da9YeiN9a8G3jRU8d4n1ELK_2vY6kgAV-2g6gJWA52d4"


if __name__ == "__main__":
    # Вызываем функцию
    print(send_get_request(url, "411864", access_token))