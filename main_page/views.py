from django.shortcuts import render


def main_page(request):
    context = {
        'title': 'Giocatory - main page',
    }

    return render(request, 'main_page/index.html', context=context)

