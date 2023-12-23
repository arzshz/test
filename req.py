import requests

def test_api_responses():
    # URL های وب سرویس ها
    flask_url = "http://localhost:5000"
    django_url = "http://localhost:8000"
    fastapi_url = "http://localhost:7000"

    # ورودی‌های مورد نظر
    payloads = [{"input": "test1"}, {"input": "test2"}, {"input": "test3"}]

    for payload in payloads:
        flask_response = requests.get(flask_url, json=payload)
        django_response = requests.get(django_url, json=payload)
        fastapi_response = requests.get(fastapi_url, json=payload)

    print(flask_response.headers)
    print(fastapi_response.headers)
    print(django_response.headers)
    if flask_response.text == django_response.text and django_response.text == fastapi_response.text :
        print("Outputs are the same.")

test_api_responses()