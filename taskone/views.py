from django.shortcuts import render
from django.http import HttpResponse

nums = []


def index(request):
    for i in range(1, 21):
        nums.append(i)

    return render(request, 'index.html', {'nums': nums})


def get_nums(request):
    start = 1
    end = 21
    try:
        assert start is not None and end is not None

        start = int(request.GET.get('start'))
        end = int(request.GET.get('end'))

        if end > start:
            nums.clear()

            for i in range(start, end + 1):
                nums.append(i)

            return render(request, 'Numbers.html', {'nums': nums})
        else:
            return HttpResponse('Ending value cannot be smaller than the Starting Value!')
    except ValueError:
        tpl = tuple(x for x in range(1, 21))
        context = {
            'iterator': tpl
        }
        return render(request, 'Numbers.html', context=context)
