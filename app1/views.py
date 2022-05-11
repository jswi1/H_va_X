from django.shortcuts import render
from .models import *

def home(request):
    qidirish = request.GET.get("qidiruv_sozi")
    togri_var = Togri.objects.filter(soz=qidirish)
    if len(togri_var) == 1:
        notogri_var = Notogri.objects.filter(togri=togri_var[0])
    else:
        n = Notogri.objects.filter(xato_soz=qidirish)
        if len(n) == 1:
            togri_var = Togri.objects.filter(id=n[0].togri.id)
            notogri_var = Notogri.objects.filter(togri=togri_var[0])
        notogri_var = []
    data = {
        "togri":togri_var,
        "notogri":notogri_var
    }
    return render(request, "result.html", data)
