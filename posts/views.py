from django.shortcuts import render

def home_view(request):
    print(request)
    print('Request Method:',request.method)

    if request.method == 'POST':
        print('bye bye')
    return render(request,'posts/home.html')
