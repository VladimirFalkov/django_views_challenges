"""
В этом задании вам нужно реализовать вьюху, которая валидирует данные о пользователе.

- получите json из тела запроса
- проверьте, что данные удовлетворяют нужным требованиям
- если удовлетворяют, то верните ответ со статусом 200 и телом `{"is_valid": true}`
- если нет, то верните ответ со статусом 200 и телом `{"is_valid": false}`
- если в теле запроса невалидный json, вернуть bad request

Условия, которым должны удовлетворять данные:
- есть поле full_name, в нём хранится строка от 5 до 256 символов
- есть поле email, в нём хранится строка, похожая на емейл
- есть поле registered_from, в нём одно из двух значений: website или mobile_app
- поле age необязательное: может быть, а может не быть. Если есть, то в нём хранится целое число
- других полей нет

Для тестирования рекомендую использовать Postman.
Когда будете писать код, не забывайте о читаемости, поддерживаемости и модульности.
"""
import json
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest


def check_data(data):
    full_name_length = len(data["full_name"])
    email = data["email"]
    registered_from = data["registered_from"]
    age = data.get("age")

    if full_name_length < 5 or full_name_length > 256:
        return False

    if "@" not in email:
        return False

    if registered_from not in ["website", "mobile_app"]:
        return False

    if age and not age.isdigit():
        return False

    return True


def validate_user_data_view(request: HttpRequest) -> HttpResponse:
    data = json.dumps(request.POST)
    if data:
        try:
            json_data = json.loads(data)
            data_is_valid = check_data(json_data)
            if data_is_valid:
                return HttpResponse(200, {"is_valid": True})
            else:
                return HttpResponse(200, {"is_valid": False})
        except ValueError as exc:
            raise HttpResponseBadRequest(exc)
