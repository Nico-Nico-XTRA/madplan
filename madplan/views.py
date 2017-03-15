from django.shortcuts import render, redirect

from madplan.forms import DishForm
from madplan.models import Dish

"""
def index(request):
	number = 6
	name = "Asshole"
	return render(request, 'index.html',{
					'number': number,
					'name': name,
					})
"""

def index(request):
	number = 6
	name = "Asshole"
	dishes = Dish.objects.all()

	return render(request, 'index.html', {
		'dishes': dishes,
		'number': number,
		'name': name,
		})

def about(request):
	return render(request, 'about.html')

def contact(request):
	return render(request, 'contact.html')

def dish_detail(request, slug):
	dish = Dish.objects.get(slug=slug)
	return render(request, 'dishes/dish_detail.html', {
		'dish': dish,
		})

def edit_dish(request, slug):
    # grab the object
    dish = Dish.objects.get(slug=slug)
    # set the form we're using
    form_class = DishForm

    # if we're coming to this view from a submitted form
    if request.method == 'POST':
        # grab the data from the submitted form and apply to
        # the form
        form = form_class(data=request.POST, instance=dish)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('dish_detail', slug=dish.slug)
    # otherwise just create the form
    else:
        form = form_class(instance=dish)

    # and render the template
    return render(request, 'dishes/edit_dish.html', {
        'dish': dish,
        'form': form,
    })