from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.


monthly_challenges = {
    "january": "Eat no meat for the entire moth",
    "feburary": "Walk everyday for atleast 1h every day",
    "march": "Don't drink alcohol for entire month",
    "april": "Take cold showers every day",
    "may": "Learn Django for 1h every day",
    "june": "Eat no meat for the entire moth",
    "july": "Walk everyday for atleast 1h every day",
    "august": "Take cold showers every day",
    "september": "Learn Django for 1h every day",
    "october": "Don't drink alcohol for entire month",
    "november": "Walk everyday for atleast 1h every day",
    "december": None
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html", {"text": challenge_text,
                                                            "month_name": month.capitalize()})
    except:
        raise Http404()
   
