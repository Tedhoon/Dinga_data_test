from django.shortcuts import render


def datalist(request):
    return render(request, 'data.html',{})
