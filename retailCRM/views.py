from django.http import HttpResponse
from django.template import loader
from core.models import Company
from salescall.models import CallRecord
from django.utils import timezone
from datetime import timedelta
from django.db.models import OuterRef, Subquery


def index(request):
    template = loader.get_template('index.html')
    if request.user.is_authenticated:
        company = Company.objects.filter(is_open=True, sponsor=request.user)
        new_comps = company.filter(is_draft=True)
        newest_record = CallRecord.objects.filter(company=OuterRef('pk')).order_by('calldate')
        subquery = Subquery(newest_record.values('calldate')[:1])
        comp_w_rcrddt = Company.objects.filter(
            is_draft=False,
            is_open=True,
            sponsor=request.user).annotate(news_record=subquery).order_by("-news_record")
        cmp_twowk = comp_w_rcrddt.filter(news_record__gte=timezone.now().date() - timedelta(weeks=2))
        cmp_onemon = comp_w_rcrddt.filter(
            news_record__gte=timezone.now().date() - timedelta(weeks=4),
            news_record__lt=timezone.now().date() - timedelta(weeks=2),
        )
        cmp_other = comp_w_rcrddt.filter(news_record__lt=timezone.now().date() - timedelta(weeks=4))[:5]
        cmp_sets = [cmp_twowk, cmp_onemon, cmp_other]
        context = {
            'new_comps': new_comps,
            'cmp_sets': cmp_sets,
        }
    else:
        context = {}
    return HttpResponse(template.render(context, request))
