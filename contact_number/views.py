from django.shortcuts import render

def contact_number(request):
    return render(
        request,
        'contact_number/contact_number_page.html'
    )
