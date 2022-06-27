from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AddCallRecordForm, ParticipantFormset, CommentForm, CommentUpdateForm
from core.forms import UpdateCustomForm
from core.models import Company
from .models import CallRecord, Comment


def callrecord_add(request):
    template = loader.get_template('salescall/callrecord_add.html')
    if request.method == 'POST':
        form = AddCallRecordForm(request.POST, request.FILES,)
        formset = ParticipantFormset(request.POST)
        if form.is_valid() and formset.is_valid():
            record_inst = form.save()
            parti_insts = formset.save(commit=False)
            for instance in parti_insts:
                instance.record = record_inst
                instance.save()
            return HttpResponseRedirect("./")
        else:
            return HttpResponseRedirect("./")
    else:
        form = AddCallRecordForm()
        formset = ParticipantFormset()
    context = {
        'form': form,
        'formset': formset,
    }
    return HttpResponse(template.render(context, request))


def firstcall(request, comp_id):
    template = loader.get_template('salescall/firstcall.html')
    company = Company.objects.get(id=comp_id)
    cust_form = UpdateCustomForm(request.POST or None, request.FILES or None, instance=company)
    record_form = AddCallRecordForm(request.POST or None, request.FILES or None, initial={'company': comp_id})
    parti_formset = ParticipantFormset(request.POST or None)
    if request.method == 'POST':
        if cust_form.is_valid() and record_form.is_valid() and parti_formset.is_valid():
            comp = cust_form.save()
            record = record_form.save()
            partis = parti_formset.save(commit=False)
            for parti in partis:
                parti.record = record
                parti.save()
            return HttpResponseRedirect('./')
        else:
            return HttpResponseRedirect('./')
    context = {
        'cust_form': cust_form,
        'record_form': record_form,
        'parti_formset': parti_formset,
    }
    return HttpResponse(template.render(context, request))


def callrecord_update(request, record_id):
    template = loader.get_template('salescall/callrecord_update.html')
    record = CallRecord.objects.get(id=record_id)
    record_form = AddCallRecordForm(request.POST or None, request.FILES or None, instance=record)
    participants = record.participants.all()
    print(participants)
    parti_formset = ParticipantFormset(
        request.POST or None,
        instance=record,
    )
    if request.method == 'POST':
        print(record_form.is_valid(), parti_formset.is_valid())
        if record_form.is_valid() and parti_formset.is_valid():
            record_checked = record_form.save()
            partis = parti_formset.save(commit=False)
            for obj in parti_formset.deleted_objects:
                obj.delete()
            for parti in partis:
                parti.record = record_checked
                parti.save()
            return HttpResponseRedirect('./')
        else:
            return HttpResponseRedirect('./')
    context = {
        'record_form': record_form,
        'parti_formset': parti_formset,
    }
    return HttpResponse(template.render(context, request))


def comment_add(request, record_id):
    record = CallRecord.objects.get(id=record_id)
    template = loader.get_template('salescall/addcomment.html')
    form = CommentForm(request.POST or None, initial={'record': record.id})
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('./')
        else:
            return HttpResponseRedirect('./')
    context = {
        'record': record,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def comment_update(request, cmt_id):
    comment = Comment.objects.get(id=cmt_id)
    form = CommentUpdateForm(request.POST or None, instance=comment)
    template = loader.get_template('salescall/updatecomment.html')
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('./')
        else:
            return HttpResponseRedirect('./')
    context = {
        'comment': comment,
        'form': form,
    }
    return HttpResponse(template.render(context, request))
