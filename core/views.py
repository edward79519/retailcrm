from datetime import datetime
import os

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

from retailCRM.settings import BASE_DIR
from .forms import AddCustomForm, UpdateCustomForm, XlsUploadForm, CreatFormset
from .models import Company
from .extra.readfiles import readxlsx


def custom_index(request):
    template = loader.get_template('core/custom.html')
    companies = Company.objects.filter(is_open=True).order_by('-add_time')
    context = {
        'companies': companies,
    }
    return HttpResponse(template.render(context, request))


def custom_detail(request, comp_id):
    company = Company.objects.get(id=comp_id)
    template = loader.get_template('core/custom_detail.html')
    records = company.callrecords.filter(is_open=True, is_draft=False).order_by('-calldate')
    context = {
        'company': company,
        'records': records,
    }
    return HttpResponse(template.render(context, request))


@login_required
def custom_add(request):
    template = loader.get_template('core/custom_add.html')
    if request.method == 'POST':
        form = AddCustomForm(request.POST, initial={'author': request.user.id})
        if form.is_valid():
            form.save()
            return redirect('Custom_Index')
    else:
        form = AddCustomForm(initial={'author': request.user.id})
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))


@login_required
def custom_update(request, comp_id):
    company = Company.objects.get(id=comp_id)
    template = loader.get_template('core/custom_update.html')
    if request.method == 'POST':
        form = UpdateCustomForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/core/custom/{}/'.format(company.id))
    else:
        form = UpdateCustomForm(instance=company)
    context = {
        'company': company,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


@login_required
def custom_delete(request, comp_id):
    company = Company.objects.get(id=comp_id)
    if company.author.id == request.user.id:
        company.is_open = False
        company.save()
    return HttpResponseRedirect('/core/custom/')


@login_required
def custom_import(request):
    formset = None
    template = loader.get_template('core/custom_import.html')
    formset_prefix = 'custom'
    if request.method == "POST":
        # Import File Form
        if 'fileupload' in request.POST:
            form = XlsUploadForm(request.POST, request.FILES)
            if form.is_valid():
                filedir = os.path.join(BASE_DIR, 'retailCRM', 'static', 'files', 'custom', 'import')
                if not os.path.exists(filedir):
                    os.makedirs(filedir)
                filename = "TMPXLSUPLOAD_{}.xlsx".format(datetime.now().strftime("%Y%m%d%H%M%S"))
                filepath = os.path.join(filedir, filename)
                with open(filepath, "wb") as f:
                    for chunk in form.cleaned_data["source_file"].chunks():
                        f.write(chunk)
                request.session['filepath'] = filepath
            return HttpResponseRedirect('./')
        if 'add_custom' in request.POST:
            formset = CreatFormset(request.POST, prefix=formset_prefix)
            if formset.is_valid():
                for f in formset:
                    f.save()
                return redirect('Custom_Index')
            else:
                print('hello')
            # return HttpResponseRedirect('./')

    form = XlsUploadForm()
    if 'filepath' in request.session:
        print('getSession')
        filepath = request.session.get('filepath')
        del request.session['filepath']
        rawdata = readxlsx(filepath)
        os.remove(filepath)
        if rawdata['status'] == 'OK':
            print('OK')
            data = rawdata['rawdata']
            user_values = User.objects.all().values('id', 'first_name', 'last_name')
            user_dict = {}
            for row in user_values:
                user_dict["%s%s" % (row['last_name'], row['first_name'])] = row['id']
            initial_data = {
                '{}-TOTAL_FORMS'.format(formset_prefix): len(data),
                '{}-INITIAL_FORMS'.format(formset_prefix): 0,
            }
            count = 0
            for row in data:
                initial_data['{}-{}-fullname'.format(formset_prefix, count)]=row['公司名稱']
                initial_data['{}-{}-shortname'.format(formset_prefix, count)] = row['公司簡稱']
                initial_data['{}-{}-sn'.format(formset_prefix, count)] = row['統一編號']
                initial_data['{}-{}-stock_id'.format(formset_prefix, count)] = row['上市代碼']
                try:
                    initial_data['{}-{}-sponsor'.format(formset_prefix, count)] = user_dict[row['負責人']]
                except KeyError:
                    initial_data['{}-{}-sponsor'.format(formset_prefix, count)] = ""
                initial_data['{}-{}-source'.format(formset_prefix, count)] = row['客戶來源']
                initial_data['{}-{}-author'.format(formset_prefix, count)] = request.user.id
                count += 1
            print(initial_data)
            formset = CreatFormset(initial_data, prefix=formset_prefix)
        else:
            print(rawdata['msg'])
    context = {
        'form': form,
        'formset': formset,

    }
    return HttpResponse(template.render(context, request))
