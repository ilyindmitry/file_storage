from django.shortcuts import render
import datetime
from .models import UserFile
from .form import UploadFileForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    if request.user.is_anonymous:
        return render(request, "home.html")
    else:
        return HttpResponseRedirect(reverse("file_list"))


@login_required
def userfile_list(request):

    userfiles_list = UserFile.objects.filter(user=request.user)

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            userfile = UserFile(
                upload_datetime=datetime.datetime.now(),
                user=request.user,
                file=request.FILES['file'],
                status='p'
            )
            userfile.save()
            return HttpResponseRedirect(reverse("file_list"))
    else:
        if request.method == 'GET' and request.is_ajax():

            return render(
                request,
                'storage/userfile_list.html',
                context={'userfiles': userfiles_list}
            )
        else:
            form = UploadFileForm()
            return render(
                request,
                'storage/userfile_list.html',
                context={'form': form, 'userfiles': userfiles_list}
            )

