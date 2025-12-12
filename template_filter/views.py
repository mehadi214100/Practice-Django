from django.shortcuts import render
from dateutil import parser

def home(request):

    data =  {
            "users": [
                {
                "id": 1,
                "name": "john doe",
                "email": "john@example.com",
                "bio": "Full Stack Developer & Tech Enthusiast",
                "age": 29,
                "joined": "2023-06-12T10:30:00"
                },
                {
                "id": 2,
                "name": "sara ali",
                "email": "",
                "bio": "Python Lover & Django Expert",
                "age": 24,
                "joined": "2022-12-01T09:00:00"
                },
                {
                "id": 3,
                "name": "Mehadi",
                "email": "mehadi@domain.com",
                "bio": "Loves coding, reading books and traveling.",
                "age": 20,
                "joined": "2024-01-05T19:45:00"
                }
            ],

            "articles": [
                {
                "id": 101,
                "title": "django rest framework introduction",
                "content": "Django REST Framework is a powerful and flexible toolkit for building Web APIs...",
                "tags": ["django", "api", "backend", "python"],
                "published": "2023-01-12T12:30:00",
                "views": 220,
                "comments": [
                    { "user": "John", "text": "Great article!", "posted": "2023-01-12T15:00:00" },
                    { "user": "Sara", "text": "Very helpful.", "posted": "2023-01-13T10:10:00" }
                    ]
                },
                {
                "id": 102,
                "title": "python tips and tricks",
                "content": "Python has many hidden features that can make your development faster...",
                "tags": ["python", "tips", "developer"],
                "published": "2023-02-01T09:15:00",
                "views": 150,
                "comments": []
                },
                {
                "id": 103,
                "title": "web development roadmap 2024",
                "content": "To become a full stack developer, you need to master HTML, CSS, JavaScript...",
                "tags": ["web", "frontend", "career"],
                "published": "2023-12-15T18:00:00",
                "views": 350,
                "comments": [
                    { "user": "Mehadi", "text": "Very clean roadmap!", "posted": "2023-12-16T07:00:00" }
                ]
                }
            ],

            "products": [
                { "name": "Laptop", "price": 850, "stock": 10 },
                { "name": "Mobile Phone", "price": 350, "stock": 3 },
                { "name": "Keyboard", "price": 49, "stock": 25 },
                { "name": "Mouse", "price": 20, "stock": 0 }
            ]
        }

    for user in data["users"]:
        user['joined'] = parser.parse(user['joined'])

    for article in data["articles"]:
        article['published'] = parser.parse(article['published'])

    return render(request,'home.html', context=data)