from django.http import HttpResponse

def test_string(request):
    return HttpResponse('1.0')

def test_float(request):
    return HttpResponse(1.0)

def test_decimal(request):
    from decimal import Decimal
    return HttpResponse(Decimal('1.0'))
