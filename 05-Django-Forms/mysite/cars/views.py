from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ReviewForm
# Create your views here.

def rental_review(request):
    # POST REQUEST --> FORM CONTENTS --> THANK YOU\
    # if actually post sth (through submit)
    if request.method == 'POST':
        # pass to review form
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect(reverse('cars:thank_you'))
    # ELSE, RENDER FORM
    else:
        # first time visite page, no submit operation
        # just create form
        form = ReviewForm
    return render(request, 'cars/rental_review.html', context={'form': form})


def thank_you(request):
    return render(request, 'cars/thank_you.html')
