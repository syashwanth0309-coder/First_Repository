from django.shortcuts import render

# Create your views here.


def home(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operation = request.POST['operation']
        if operation == 'add':
            result = num1+num2
        elif operation == 'subtract':
            result = num1-num2
        elif operation == 'multiply':
            result = num1*num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1/num2
            else:
                result = "Error: Division by zero"
        elif operation == 'percentage':
            result = (num1/100) * num2
    return render(request, 'calculator/home.html', {'result': result})
