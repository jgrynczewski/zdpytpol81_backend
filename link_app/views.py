from django.shortcuts import render

# Create your views here.
def first_view(request):
    return render(
        request,
        'link_app/first.html'
    )


def second_view(request):
    return render(
        request,
        'link_app/second.html'
    )


def third_view(request, param):
    return render(
        request,
        'link_app/third.html',
        {'param': param}
    )
