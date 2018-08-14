from django.shortcuts import render
from .models import Document
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def doc_page(request):
    """
    Show default page of Document.All Documents are displayed.
    """
    response = []
    doc = Document.objects.all()
    for each in doc:
        response.append({"doc_name" : each.doc_name,
                         "doc_id" : each.id})
    return render(request, "document/document.html", context={"doc":response})

def doc_detail(request, doc_id):
    """
    Show detail page of specific Document identified by doc_id.
    Document contents are displayed.
    """
    doc = Document.objects.get(id = doc_id)
    context={"doc":doc.src}
    return render(request, "document/document_detail.html", context)

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
