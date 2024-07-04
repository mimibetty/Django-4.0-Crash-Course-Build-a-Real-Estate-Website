from django.shortcuts import render, get_object_or_404,redirect
from .models import Listing
from .forms import ListingForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def listing_list(request):
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, "listings.html", context)

def listing_retrieve(request, pk):
    listing = get_object_or_404(Listing, id=pk)
    context = {
        "listing": listing
    }
    return render(request, "listing.html", context)


# add
def listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POS, request.FILES)
        # print(form)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "listing_create.html", context)

def listing_update(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)

    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing,files= request.FILES)
        # print(form)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "listing_update.html", context)

def listing_delete(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect("/")





def listing_test(request):
    if request.method == 'GET':
        listings = Listing.objects.all()
        listings_data = [
            {
                "id": listing.id,
                "title": listing.title,
                "price": listing.price,
                "num_bedrooms": listing.num_bedrooms,
                "num_bathrooms": listing.num_bathrooms,
                "square_footage": listing.square_footage,
                "address": listing.address
            } 
            for listing in listings
        ]
        return JsonResponse({"listings": listings_data})


def test_get(request):
    return render(request, 'add_listing_test.html')



@csrf_exempt
def add_listing_test(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        listing = Listing(
            title=data.get('title'),
            price=data.get('price'),
            num_bedrooms=data.get('num_bedrooms'),
            num_bathrooms=data.get('num_bathrooms'),
            square_footage=data.get('square_footage'),
            address=data.get('address')
        )
        listing.save()
        return JsonResponse({"message": "Listing added successfully!"})
    return JsonResponse({"error": "Invalid request method"}, status=400)