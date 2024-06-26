import csv

from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import CSVUploadForm
from .models import CarListing


def is_admin(user):
    return user.is_superuser


@user_passes_test(is_admin)
def upload_csv(request):
    if request.method == "POST":
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES["csv_file"]
            decoded_file = csv_file.read().decode("utf-8").splitlines()
            reader = csv.DictReader(decoded_file)
            for row in reader:
                CarListing.objects.create(
                    website=row["Website"],
                    country=row["Country"],
                    type=row["Type"],
                )
            messages.success(request, "Data imported successfully")
            return redirect("upload_csv")
    else:
        form = CSVUploadForm()
    return render(request, "upload_csv.html", {"form": form})
