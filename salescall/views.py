from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from django.shortcuts import redirect

from core.forms import UpdateCustomForm, UpdatePWRInfoForm
from core.models import Company
from .forms import AddCallRecordForm, ParticipantFormset, PartiUpdateFormset, UpdateCallRecordForm, FirstCallRecordForm
from .models import CallRecord, Comment


def callrecord_index(request):
    template = loader.get_template("salescall/callrecord_list.html")
    records = CallRecord.objects.filter(is_open=True).order_by("-add_time")
    records_draft = records.filter(is_draft=True, author_id=request.user.id)
    records_cmplt = records.filter(is_draft=False)
    context = {
        'records_draft': records_draft,
        'records_cmplt': records_cmplt,
    }
    return HttpResponse(template.render(context, request))


def record_detail(request, record_id):
    template = loader.get_template("salescall/record_detail.html")
    record = CallRecord.objects.get(id=record_id)
    cust_partis = record.participants.filter(side=True)
    our_partis = record.participants.filter(side=False)
    if request.method == "POST":
        cmt_id = request.POST['cmt_id']
        content = request.POST['cmt_cnt']
        if cmt_id:
            comment = Comment.objects.get(id=cmt_id)
            comment.content = content
            comment.save()
            return HttpResponseRedirect("./#cmt_div")
        else:
            comment = Comment(record=record, author=request.user, content=content)
            comment.save()
            return HttpResponseRedirect("./#cmt_div")
    context = {
        'record': record,
        'cust_partis': cust_partis,
        'our_partis': our_partis,
    }
    return HttpResponse(template.render(context, request))


def record_add(request):
    template = loader.get_template('salescall/record_add.html')
    if request.method == 'POST':
        post_copy = request.POST.copy()
        monrcrdcnt = CallRecord.objects.filter(add_time__month=timezone.now().month).count()
        post_copy['sn'] = '{}{}'.format(timezone.now().strftime('%Y%m'), str(monrcrdcnt).zfill(3))
        form = AddCallRecordForm(post_copy, request.FILES)
        if request.POST['company']:
            company = Company.objects.get(id=request.POST['company'])
            pwrform = UpdatePWRInfoForm(request.POST, instance=company)
        custformset = ParticipantFormset(request.POST, prefix="cust")
        ourformset = ParticipantFormset(request.POST, prefix="our")

        if form.is_valid() and custformset.is_valid() and ourformset.is_valid() and pwrform.is_valid():
            comppwr_inst = pwrform.save()
            print(comppwr_inst.history)
            record_inst = form.save()
            formsets = [custformset, ourformset]
            for formset in formsets:
                parti_insts = formset.save(commit=False)
                for instance in parti_insts:
                    instance.record = record_inst
                    instance.save()
            return HttpResponseRedirect("/salescall/")
    else:
        form = AddCallRecordForm(initial={'author': request.user.id})
        if request.GET.get('id_comp'):
            company = Company.objects.get(id=request.GET.get('id_comp'))
            form.fields["company"].initial = company.id
            pwrform = UpdatePWRInfoForm(instance=company)
        else:
            pwrform = UpdatePWRInfoForm()
        custformset = ParticipantFormset(prefix="cust")
        ourformset = ParticipantFormset(prefix="our", initial=[{'side': False}])
    context = {
        'form': form,
        'pwrform': pwrform,
        'custformset': custformset,
        'ourformset': ourformset,
    }
    return HttpResponse(template.render(context, request))


def record_lock(request, record_id):
    record = CallRecord.objects.get(id=record_id)
    if record.author.id == request.user.id:
        record.is_draft = False
        record.save()
    return HttpResponseRedirect('../')


def record_delete(request, record_id):
    record = CallRecord.objects.get(id=record_id)
    if record.author.id == request.user.id:
        record.is_open = False
        record.save()
    return HttpResponseRedirect('/salescall/')


def record_update(request, record_id):
    template = loader.get_template('salescall/record_update.html')
    record = CallRecord.objects.get(id=record_id)
    our_parti = record.participants.filter(side=False)
    cust_parti = record.participants.filter(side=True)
    company = record.company
    if request.method == 'POST':
        form = UpdateCallRecordForm(request.POST, request.FILES, instance=record)
        pwrform = UpdatePWRInfoForm(request.POST, instance=company)
        custformset = PartiUpdateFormset(request.POST, prefix="cust", queryset=cust_parti, instance=record)
        ourformset = PartiUpdateFormset(request.POST, prefix="our", queryset=our_parti, instance=record)
        form_list = [form, pwrform, custformset, ourformset]
        formcheck = [f.is_valid() for f in form_list]
        if False not in formcheck:
            form.save()
            formsets = [custformset, ourformset]
            for formset in formsets:
                formset.save()
            return HttpResponseRedirect('../')
    else:
        form = UpdateCallRecordForm(instance=record)
        pwrform = UpdatePWRInfoForm(instance=company)
        custformset = PartiUpdateFormset(prefix="cust", queryset=cust_parti, instance=record)
        ourformset = PartiUpdateFormset(prefix="our", queryset=our_parti, instance=record, initial=[{'side': False}])
    context = {
        'record': record,
        'form': form,
        'pwrform': pwrform,
        'custformset': custformset,
        'ourformset': ourformset,
    }
    return HttpResponse(template.render(context, request))


def comment_index(request):
    template = loader.get_template("salescall/comment_list.html")
    records = CallRecord.objects.all()
    if request.method == "POST":
        if 'cmt_add' in request.POST:
            comment = Comment(record_id=request.POST["record"],
                              author_id=request.POST["author"],
                              content=request.POST["content"])
            comment.save()
            return HttpResponseRedirect('./')
        if 'cmt_update' in request.POST:
            comment = Comment.objects.get(id=request.POST['comment'])
            comment.author.id = request.POST['author']
            comment.content = request.POST['content']
            comment.save()
            return HttpResponseRedirect('./')
    context = {
        'records': records,
    }
    return HttpResponse(template.render(context, request))


def firstcall(request, comp_id):
    template = loader.get_template('salescall/firstcall.html')
    company = Company.objects.get(id=comp_id)
    cust_form = UpdateCustomForm(request.POST or None,
                                 request.FILES or None,
                                 instance=company)
    form = FirstCallRecordForm(request.POST or None,
                               request.FILES or None,
                               initial={
                                   'company': comp_id,
                                   'author': request.user.id,
                               })
    custformset = ParticipantFormset(request.POST or None, prefix="cust")
    ourformset = ParticipantFormset(request.POST or None, prefix="our", initial=[{'side': False}])
    if request.method == "POST":
        form_list = [cust_form, form, custformset, ourformset]
        formcheck = [f.is_valid() for f in form_list]
        if False not in formcheck:
            custom = cust_form.save(commit=False)
            custom.is_draft = False
            custom.save()
            record_inst = form.save()
            formsets = [custformset, ourformset]
            for formset in formsets:
                parti_insts = formset.save(commit=False)
                for instance in parti_insts:
                    instance.record = record_inst
                    instance.save()
            return HttpResponseRedirect('../')
        return HttpResponseRedirect('./')
    context = {
        'company': company,
        'cust_form': cust_form,
        'form': form,
        'custformset': custformset,
        'ourformset': ourformset,
    }
    return HttpResponse(template.render(context, request))
