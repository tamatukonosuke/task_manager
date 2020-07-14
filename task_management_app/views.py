from django.shortcuts import render
from django.http import HttpResponse
from task_management_app.models import Member
from collections import OrderedDict
import json

def index(request):
    members = Member.objects.all().order_by('id')
    return render(request, 'members/index.html', {'members':members})


def api(request):
    members = []
    for member in Member.objects.all().order_by('id'):
        member_dict = OrderedDict([
                ('id',member.id),
                ('name',member.name),
                ('email',member.email),
                ('age',member.age),
            ])
        members.append(member_dict)

    data = OrderedDict([
            ('status','ok'),
            ('members',members),
        ])

    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str, content_type='application/json; charset=utf-8')