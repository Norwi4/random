import random

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def user(request):
    first = random.choice(range(1, 10))
    leftover = set(range(10)) - {first}
    rest = random.sample(leftover, 3)
    digits = [first] + rest

    context = {
        "code": str(digits)
    }

    return render(request, "index.html", context=context)

#  http://127.0.0.1:8000/?name=Tom&message=Давай дружить