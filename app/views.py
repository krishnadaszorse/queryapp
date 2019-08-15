from django.shortcuts import render
from django.http import HttpResponse
from .models import Query
from .forms import QureyForm

def index_view(request):
    form = QureyForm()
    columns = None
    data = None
    query = None
    queryset = Query.objects.all()
    print(queryset.query)
    if request.method == 'POST':
        form = QureyForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            query_obj = Query()
            query_obj.query = query
            query_obj.save()
            query_set = Query.objects.raw(query_obj.query)
            columns = query_set.columns
            print([item for item in query_set])
            print([[getattr(item, col) for col in columns] for item in query_set])
            data = [[getattr(item, col) for col in columns] for item in query_set]
    content = {'form':form, 'columns':columns, 'data':data, 'query':query}
    return render(request, "index.html", content)
