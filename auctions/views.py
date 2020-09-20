from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError, models
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Listing, Comments, Bids, Wishlist

# Load the index page 
def index(request):
    listings = Listing.objects.all()
    
    return render(request, "auctions/index.html", {
        "listings": listings
    })


# Login page
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


# Logout page
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


# Register page for new users
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

categories = ["Books", "Clothing", "Shoes", "Toys", "Electronics", "Home"]

# Create new listing 
# Only registered users can visit this page
@login_required
def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        startingbid = request.POST["startingbid"]
        imageurl = request.POST.get("imageurl", "")
        category = request.POST.get("category", "")
        user = request.user

        listing = Listing(title=title, description=description, startingbid=startingbid, imageurl=imageurl, category=category, user=user, price=startingbid)
        listing.save()

        return HttpResponseRedirect(reverse("index"))

    return render(request, "auctions/create.html", {
        "categories": categories
    })

# Page for all the indivisual listings
# Shows all the details about the lising and handles bids form
def listing(request, id):
    listing = Listing.objects.get(pk=id)
    user = request.user
    if request.user.is_anonymous:
        value = ""
    else:
        if Wishlist.objects.filter(listing=listing, user=user):
            value = "Remove from watchlist"
        else:
            value = "Add to watchlist"  

    if request.method == "POST":
        bid = request.POST['bid']
        if request.user.is_anonymous:
            return render(request, "auctions/listing.html", {
                "listing": listing,
                "value": value,
                "message": "Login to place your bid."
            })
        if listing.active == False:
             return render(request, "auctions/listing.html", {
                "listing": listing,
                "value": value,
                "message": "Auction on this listing is closed."
            })
        if bid == "":
            return render(request, "auctions/listing.html", {
                "listing": listing,
                "value": value,
            })
        if int(bid) < listing.price:
             return render(request, "auctions/listing.html", {
                "listing": listing,
                "value": value,
                "message": "Bid should be higher than the price."
            })
        else:
            bid = Bids.objects.create(bid=bid, user=user)
            bid.listing.add(listing)
            bid.save()            
            listing.bidcount = listing.bidcount + 1
            listing.price = bid.bid
            listing.winner = user
            listing.save()
            return render(request, "auctions/listing.html", {
                "listing": listing,
                "value": value,
                "message": "Bid placed."
            })
              
    return render(request, "auctions/listing.html", {
        "listing": listing,
        "value": value
    })

# Shows all the listing what are added to Watchlist by the user
@login_required
def wishlist(request):
    user = request.user
    wishlists = user.wishlist.all()

    if request.method == "POST":
        listing_id = request.POST["id"]

        if Wishlist.objects.filter(listing=Listing.objects.get(pk=listing_id), user=user):
            Wishlist.objects.filter(listing=Listing.objects.get(pk=listing_id), user=user).delete()
            return HttpResponseRedirect(reverse("listing", args=[listing_id]))
        
        else:
            wishlist = Wishlist.objects.create(listing=Listing.objects.get(pk=listing_id))
            wishlist.user.add(user)
            wishlist.save()
            return HttpResponseRedirect(reverse("listing", args=[listing_id]))

    return render(request, "auctions/wishlist.html", {
        "wishlists": wishlists
    })    

# Handles the close form and closed the listing
# Only allowed to user that has created the listing
# Highest bidder on the listing is declared the winner
@login_required
def close(request, id):
    listing = Listing.objects.get(pk=id)
    if Wishlist.objects.filter(listing=listing, user=request.user):
        value = "Remove from watchlist"
    else:
        value = "Add to watchlist"

    if request.method == "POST":
        if (request.user == listing.user):
            listing.active = False
            listing.save()

        return render(request, "auctions/listing.html", {
            "listing": listing,
            "value": value
        })


    return render(request, "auctions/listing.html", {
        "listing": listing,
        "value": value
    })

# Show comments on each of the listing's page
def comment(request, id):
    listing = Listing.objects.get(pk=id)
    if request.user.is_anonymous:
        value = ""
    else:
        if Wishlist.objects.filter(listing=listing, user=request.user):
            value = "Remove from watchlist"
        else:
            value = "Add to watchlist"
    
    if request.method == "POST":
        if request.user.is_anonymous:
            return render(request, "auctions/listing.html", {
                "listing": listing,
                "value": value,
                "message2": "Login to comment."
            }) 
        comment = request.POST['comment']
        new_comment = Comments.objects.create(comment=comment, user=request.user)
        new_comment.listing.add(listing)

    return render(request, "auctions/listing.html", {
        "listing": listing,
        "value": value
    })    

# Shows the list of categorie to chose from
def categorylist(request):
    return render(request, "auctions/categories.html", {
        "categories": categories
    })

# Shows all the listings whose category is the category chosen by the user
def category(request, category):
    listings = Listing.objects.filter(category=category)
    return render(request, "auctions/category.html", {
        "listings": listings,
        "category": category
    })