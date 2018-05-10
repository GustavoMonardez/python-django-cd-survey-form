from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "surveys/index.html")

def success(request):
    return render(request, "surveys/success.html")

def process(request):
    if not "count" in request.session:
        request.session["count"] = 0
    request.session["count"] += 1
    request.session["name"]= request.POST["name"]
    request.session["location"] = request.POST["location"]
    request.session["language"] = request.POST["language"]
    request.session["comment"] = request.POST["comment"]   
    return redirect("/success")

def reset(request):
    request.session.flush()
    return redirect("/")
