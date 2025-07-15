from django.shortcuts import render, redirect, get_object_or_404
from .forms import *

from .models import *

def index(request):
    return render(request, 'index.html', {})

#Kwiaty CRUD
def showFlowersView(request):
    flowers = Flower.objects.all()
    context = {
        'flowers': flowers
    }
    return render(request, 'flower/index.html', context)

def showFlowerView(request, f_id):
    flower = get_object_or_404(Flower, id=f_id)
    return render(request, 'flower/show.html', {'flower': flower})

def createFlowerView(request):
    if request.method == "POST":
        form = FlowerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            context = {'form': form}
            return render(request, 'flower/create.html', context)
    else:
        form = FlowerForm()
        context = {
            'form': form
        }
    return render(request, 'flower/create.html', context)

def updateFlowerView(request, f_id):
    flower = Flower.objects.get(id=f_id)
    form = FlowerForm(instance=flower)

    if request.method == "POST":
        form = FlowerForm(request.POST, instance=flower)

        if form.is_valid():
            form.save()
            return redirect('/flower/index')
        else:
            context = {'form': form}
            return render(request, 'flower/update.html', context)
    context = {"form": form}
    return render(request, 'flower/update.html', context)

def deleteFlowerView(delete, f_id):
    flower = get_object_or_404(Flower, id=f_id)
    flower.delete()
    return redirect('/flower/index')


#Kolory CRUD
def showColorsView(request):
    colors = Color.objects.all()
    context = {
        'colors': colors,
    }
    return render(request, 'color/index.html', context)

def showColorView(request, c_id):
    color = get_object_or_404(Color, id=c_id)
    return render(request, 'color/show.html', {'color': color})

def createColorView(request):
    colors = Color.objects.all()
    if request.method == "POST":
        form = ColorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            context = {'form': form}
            return render(request, 'color/create.html', context)
    else:
        form = ColorForm()
        context = {
            'form': form,
            'colors': colors
        }
    return render(request, 'color/create.html', context)

def updateColorView(request, c_id):
    color = Color.objects.get(id=c_id)
    form = ColorForm(instance=color)

    if request.method == "POST":
        form = ColorForm(request.POST, instance=color)

        if form.is_valid():
            form.save()
            return redirect('/color/index')
        else:
            context = {'form': form}
            return render(request, 'color/update.html', context)
    context = {"form": form}
    return render(request, 'color/update.html', context)

def deleteColorView(request, c_id):
    color = get_object_or_404(Color, id=c_id)
    color.delete()
    return redirect('/color/index')

#Kompozycje kwiatore CRUD
def showFlowerArrangementsView(request):
    arrangements = FlowerArrangement.objects.all()
    context = {
        'arrangements': arrangements
    }
    return render(request, 'flower_arrangement/index.html', context)

def showFlowerArrangementView(request, a_id):
    arrangement = get_object_or_404(FlowerArrangement, id=a_id)
    return render(request, 'flower_arrangement/show.html', {'arrangement': arrangement})

def createFlowerArrangementView(request):
    if request.method == 'POST':
        form = FlowerArrangementForm(request.POST, request.FILES)
        files = request.FILES.getlist('images')  # <= wiele plików

        if form.is_valid():
            arrangement = form.save()

            for f in files:
                FlowerArrangementImage.objects.create(arrangement=arrangement, image=f)

            return redirect('show_arrangements')

    else:
        form = FlowerArrangementForm()
    return render(request, 'flower_arrangement/create.html', {'form': form})


def updateFlowerArrangementView(request, a_id):
    arrangement = get_object_or_404(FlowerArrangement, id=a_id)

    if request.method == 'POST':
        form = FlowerArrangementForm(request.POST, request.FILES, instance=arrangement)
        if form.is_valid():
            form.save()

            image_file = request.FILES.get('images')
            if image_file:
                FlowerArrangementImage.objects.create(
                    arrangement=arrangement,
                    image=image_file
                )

            return redirect('show_arrangements')
    else:
        form = FlowerArrangementForm(instance=arrangement)

    return render(request, 'flower_arrangement/update.html', {
        'form': form,
        'arrangement': arrangement,
    })
def deleteFlowerArrangementView(request, a_id):
    arrangement = get_object_or_404(FlowerArrangement, id=a_id)
    arrangement.delete()
    return redirect('/flower_arrangement/index')

def deleteImageView(request, i_id):
    image = get_object_or_404(FlowerArrangementImage, id=i_id)
    image.delete()
    return redirect('/flower_arrangement/index')



def searchFlowersView(request):
    query = request.GET.get('search')
    post_results = []

    if query:
        post_results = FlowerArrangement.objects.filter(name__icontains=query)

    return render(request, 'search/index.html', {
        'query': query,
        'post_results': post_results
    })