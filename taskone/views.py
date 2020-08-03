from django.shortcuts import render
from django.http import HttpResponse

nums = []


def index(request):
    for i in range(1, 21):
        nums.append(i)

    return render(request, 'index.html', {'nums': nums})


def get_nums(request):
    start = int(request.GET.get('start', 1))
    end = int(request.GET.get('end', 21))
    if end > start:
        nums.clear()

        for i in range(start, end+1):
            nums.append(i)

        return render(request, 'Numbers.html', {'nums': nums})
    else:
        return HttpResponse('Ending value cannot be smaller than the Starting Value!')

