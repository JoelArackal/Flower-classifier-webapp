from django.shortcuts import render
from .forms import Flowers_Form
from media import image_proc
from .models import Flowers


mod = image_proc.classification()

# Create your views here.

def index(request):
    if request.method == 'POST':
        flower_form = Flowers_Form(request.POST, request.FILES)
        if flower_form.is_valid():
            fl = flower_form.save(commit=False)
            # idf = request.FILES['flower_image']
            fl.save()
            print(fl.id)
            fl2 = Flowers.objects.filter(id=fl.id)
            img = fl2[0].flower_image
            result = mod.pred(fl2[0].flower_image)
        return render(request,'prediction.html',{'result':result,'img':img})        
    else:
        flower_form = Flowers_Form()
    return render(request,'index.html',{'form':flower_form})


    
