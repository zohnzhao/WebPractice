from django.shortcuts import render, get_object_or_404
from .models import Schooldetails, Schoolscore, Specialtydetails, Specialtyscore
from django.core.paginator import Paginator
from django.http import JsonResponse
from urllib import parse


# Create your views here.
def Schooldetails_list(request, list_pk):
    context = {}
    Schooldetailsall = Schooldetails.objects.all().order_by('id')
    paginator = Paginator(Schooldetailsall, 10)  # 每10页 分页
    page_of_school = paginator.get_page(list_pk)
    context['schooldetails_list'] = page_of_school
    return render(request, "schooldetails_list.html", context)


def School_details(request, school_pk):
    context = {}
    context['schooldetails'] = get_object_or_404(Schooldetails, pk=school_pk)
    context['specialtydetails'] = Specialtydetails.objects.filter(schoolname=context['schooldetails'].name)
    return render(request, "Schooldetails.html", context)


def School_core(request):
    if request.method == 'POST':
        data = {}
        temp = []
        school = parse.unquote(str(request.body))
        schoolname = parse.parse_qs(school)["b'schoolname"][0]
        province = parse.parse_qs(school)["province"][0]
        pici = parse.parse_qs(school)["pici"][0]
        year = parse.parse_qs(school)["year"][0].rstrip("'")
        schoolcore = Schoolscore.objects.filter(schoolname=schoolname, province=province, pici=pici,
                                                year=year).distinct()
        if len(schoolcore) > 1:
            data['status'] = 'SUCCESS'
            for x in schoolcore:
                temp.append([x.schoolname, x.province, x.pici, x.ambit, x.year, x.maxscore, x.average, x.minscore])
            data['schoolcore'] = temp
            print(data['schoolcore'])
        else:
            data['status'] = 'NODATA'
            data['schoolcore'] = ['暂无数据']
    return JsonResponse(data)


def Specialty_details(request):
    if request.method == 'POST':
        data = {}
        temp = []
        school = parse.unquote(str(request.body))
        schoolname = parse.parse_qs(school)["b'schoolname"][0]
        province = parse.parse_qs(school)["province"][0]
        pici = parse.parse_qs(school)["pici"][0]
        year = parse.parse_qs(school)["year"][0].rstrip("'")
        schoolcore = Specialtyscore.objects.filter(schoolname=schoolname, province=province, ambit=pici,
                                                   year=year).distinct()
        if len(schoolcore) > 0:
            data['status'] = 'SUCCESS'
            for x in schoolcore:
                temp.append([x.schoolname, x.province, x.ambit, x.year, x.maxscore, x.average, x.minscore])
            data['schoolcore'] = temp
        else:
            data['status'] = 'NODATA'
            data['schoolcore'] = ['暂无数据']
    return JsonResponse(data)


def inquiry(request):
    context = {}
    return render(request, "inquiry.html", context)


def inquiry_core(request):
    if request.method == 'POST':
        data = {}
        temp = []
        body = parse.unquote(str(request.body))
        core = parse.parse_qs(body)["b'core"][0].rstrip("'")
        school = Schoolscore.objects.exclude(minscore='--').distinct()
        if len(school) > 0:
            data['status'] = 'SUCCESS'
            for x in school:
                if x.minscore != '':
                    if int(core) >= int(x.minscore):
                        schoolde = get_object_or_404(Schooldetails, name=x.schoolname)
                        temp.append(
                            [schoolde.id,x.schoolname, x.province, x.pici, x.ambit, x.year, x.maxscore, x.average, x.minscore])
            data['schoolcore'] = temp
        else:
            data['status'] = 'NODATA'
            data['schoolcore'] = ['暂无数据']
    return JsonResponse(data)
