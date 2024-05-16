import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.
# def Register(request):
#     if request.method == "PSOT":
#         first_name = request.POST.get['first_name']
#         last_name  = request.POST.get['last_name']
#         username = request.POST.get['user_name']
#         password = request.POST.get['password']
#         confirm_password = request.POST.get['confirm_password']

#         if password == confirm_password:
#             user = User.objects.create(first_name=first_name,last_name=last_name,username=username)
#             user.save()
#             return redirect('/login/')
#         else:
#             return redirect("/register/")

#         # user = User.objects.filter(username = username)
#         # if user.exists():
#         #     messages.info("User Already Exits.")


#     return render(request,"register.html")
def Register(request):
    if request.method == "POST":
        # Retrieve form data
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("user_name")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Perform validation
        errors = []
        if len(first_name) < 2:
            errors.append("First name must be at least 2 characters long.")
        if len(last_name) < 2:
            errors.append("Last name must be at least 2 characters long.")
        if len(username) < 4:
            errors.append("Username must be at least 4 characters long.")
        if len(password) < 6:
            errors.append("Password must be at least 6 characters long.")
        if password != confirm_password:
            errors.append("Password and Confirm Password do not match.")

        # If there are validation errors, return response with error messages
        if errors:
            return HttpResponse(
                json.dumps({"errors": errors}),
                content_type="application/json",
                status=400,
            )

        # If validation passes, proceed with registration logic
        # (for demonstration, let's just return a success response)
        return HttpResponse(
            json.dumps({"message": "Registration successful!"}),
            content_type="application/json",
            status=200,
        )


def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not User.objects.filter(username=username).exists():
            messages.info(request, "Invalid Username")
            return redirect("/login/")
        user = authenticate(username=username, password=password)
        if user is None:
            messages.info(request, "Password Invalid")
            return redirect("/login/")
        else:
            login(request, user)
            return redirect("/blog/")

    return render(request, "login.html")
