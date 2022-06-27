from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AddCustomForm, UpdateCustomForm
from .models import Company


# Create your views here.
def custom_add(request):
    template = loader.get_template('core/custom_add.html')
    if request.method == 'POST':
        form = AddCustomForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('./')
    else:
        form = AddCustomForm()
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def custom_update(request, comp_id):
    company = Company.objects.get(id=comp_id)
    template = loader.get_template('core/custom_update.html')
    if request.method == 'POST':
        form = UpdateCustomForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('./')
    else:
        form = UpdateCustomForm(instance=company)
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))
