from django.shortcuts import render
from datetime import datetime

dict1 = {
    'str1' : "Hello, I\'m Emon",
    'value1' : 10,
    'str2' : 'this is a beautiful day',
    'date' : datetime.now(),
    'emptystr': "",
    'lst1' : [
        {'name': 'joe', 'age': 31},
        {'name': 'zed', 'age': 19},
        {'name': 'amy', 'age': 22},
    ],
    'value2' : 987654321,
    'lst2' : ['Bangladesh', 'is', 'a', 'beautiful', 'country',],
    "previous_date": datetime(2024, 12, 10, 12, 0),
    'lst3' : ['States', ['Kansas', ['Lawrence', 'Topeka'], 'Illinois']],
    'num1' : 1,
    'num2' : 5,
    
}

# Create your views here.
def earthly(request):
    return render(request, 'app1/earthly.html', dict1)

def geeksforgeeks(request):
    return render(request, 'app1/geeksforgeeks.html', dict1)

def test(request):
    return render(request, 'test.html')
