"""
В этом задании вам нужно научиться генерировать текст заданной длинны и возвращать его в ответе в виде файла.

- ручка должна получать длину генерируемого текста из get-параметра length;
- дальше вы должны сгенерировать случайный текст заданной длины. Это можно сделать и руками
  и с помощью сторонних библиотек, например, faker или lorem;
- дальше вы должны вернуть этот текст, но не в ответе, а в виде файла;
- если параметр length не указан или слишком большой, верните пустой ответ со статусом 403

Вот пример ручки, которая возвращает csv-файл: https://docs.djangoproject.com/en/4.2/howto/outputting-csv/
С текстовым всё похоже.

Для проверки используйте браузер: когда ручка правильно работает, при попытке зайти на неё, браузер должен
скачивать сгенерированный файл.
"""

from django.http import HttpResponse, HttpRequest
from faker import Faker


def generate_fake_text(text_length: int) -> str:
    fake = Faker()
    return fake.text(text_length)


def generate_file_with_text_view(request: HttpRequest) -> HttpResponse:
    length = request.POST.get("length")
    if not length or int(length) > 1000:
        return HttpResponse(status=403)

    generated_text = generate_fake_text(int(length))
    filename = f"{generated_text.split()[0].lower()}.txt"

    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )
    return response
