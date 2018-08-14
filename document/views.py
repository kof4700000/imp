from django.shortcuts import render
from .models import Document
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings
from django.views import generic

# Create your views here.
class DocListView(generic.ListView):
    template_name = "document/document.html"
    model = Document
    context_object_name = "doc"

class DocDetailView(generic.DetailView):
    template_name = "document/document_detail.html"
    model = Document
    context_object_name = "doc"

@csrf_exempt
def upload_file(request):
    """
    handle upload file function.
    """
    try:
        upload_file = request.FILES["file"]
        #upload_file is a InMemoryUploadedFile object. For more information
        #check django DOC page 967.
        file_path = settings.UPLOAD_FILE_PATH
        #abs_path = file_path + upload_file.name
        print((file_path + upload_file.name))
        with open((file_path + upload_file.name), 'wb+') as destination:
            for chunk in upload_file.chunks():
                destination.write(chunk)
        new_doc = Document(doc_name = upload_file.name, tag = request.POST['tag'],
                           src = upload_file.name)
        new_doc.save()
    except Exception as e:
        print e
        return HttpResponse({"success":0})
    return HttpResponse({"success":1})
