from django.shortcuts import render

def home_view(request):
    return render(request, "home.html")

def index_view(request):
    students = [
        {
            "id": 1,
            "first_name": "alli",
            "last_name": "aliya",
            "age": 22
        },
        {
            "id": 2,
            "first_name": "alijon",
            "last_name": "amir",
            "age": 12
        },
        {
            "id": 3,
            "first_name": "aziz",
            "last_name": "azizov",
            "age": 23
        }
    ]
    return render(request, "index.html", context={"students": students})