from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404

from madplan.forms import DishForm
from madplan.models import Dish

def index(request):
	print ('Goodbye, cruel world!')
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

    # make sure the logged in user is the owner of the thing
    if dish.user != request.user:
    	raise Http404

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

def create_dish(request):
	form_class = DishForm

	# if we're coming from a submitted form, do this
	if request.method == 'POST':
		# grab the data from the submitted form and
		# apply to the form
		form = form_class(request.POST)
		if form.is_valid():
			# create an instance but don't save yet
			dish = form.save(commit=False)

			# set the additional details
			dish.user = request.user
			dish.slug = slugify(dish.name)

			# save the object
			dish.save()

			# redirect to our newly created dish
			return redirect('dish_detail', slug=dish.slug)

	else:
		form = form_class()

	return render(request, 'dishes/create_dish.html', {
		'form': form,	
		})