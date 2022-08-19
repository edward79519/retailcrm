from core.models import Company
from salescall.models import Participants, Comment
from django.http import JsonResponse


def getcompinfo(request):
    id_comp = request.GET.get('id_comp')
    company = Company.objects.get(id=id_comp)
    context = {
        'status': company.status.id if company.status else None,
        'pwr_usage': company.pwr_usage,
        'pwr_inquire': company.pwr_inquire,
        'unit_price': company.unit_price,
        'duration': company.duration,
        'warn_date': company.warn_date,
    }
    return JsonResponse(context)


def delparticipant(request):
    try:
        id_parti = request.GET.get('id_parti')
        parti = Participants.objects.get(id=id_parti)
        parti_info = "{}-{}".format(parti.name, parti.title)
        parti.delete()
        msg = "刪除 {} 成功。".format(parti_info)
    except:
        msg = "刪除失敗。"
    context = {
        'msg': msg,
    }
    return JsonResponse(context)


def delcomment(request):
    try:
        cmt_id = request.POST['cmt_id']
        comment = Comment.objects.get(id=cmt_id)
        comment_info = comment.content
        if comment.author == request.user:
            comment.delete()
            msg = "刪除 {} 成功。".format(comment_info)
        else:
            msg = "非原回應者不能刪除。"
    except:
        msg = "刪除失敗。"
    context = {'msg':msg}
    return JsonResponse(context)
