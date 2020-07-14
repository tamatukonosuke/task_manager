from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from task_management_app.models import Member
from task_management_app.forms import MemberForm
from collections import OrderedDict
import json

from django.contrib.auth.decorators import login_required



def one(request):
    members = Member.objects.all().order_by('id')
    return render(request, 'members/index.html', {'members':members})

@login_required
def index(request):
    members = Member.objects.all().order_by('id') #値を取得
    return render(request, 'members/index.html', {'members':members}) #Templateに値を渡す

#新規と編集
def edit(request, id=None):

    if id: #idがあるとき（編集の時）
        #idで検索して、結果を戻すか、404エラー
        member = get_object_or_404(Member, pk=id)
    else: #idが無いとき（新規の時）
        #Memberを作成
        member = Member()

    #POSTの時（新規であれ編集であれ登録ボタンが押されたとき）
    if request.method == 'POST':
        #フォームを生成
        form = MemberForm(request.POST, instance=member)
        if form.is_valid(): #バリデーションがOKなら保存
            member = form.save(commit=False)
            member.save()
            return redirect('task_management_app:index')
    else: #GETの時（フォームを生成）
        form = MemberForm(instance=member)

    #新規・編集画面を表示
    return render(request, 'members/edit.html', dict(form=form, id=id))


#削除
def delete(request, id):
    # return HttpResponse("削除")
    member = get_object_or_404(Member, pk=id)
    member.delete()
    members = Member.objects.all().order_by('id')
    return render(request, 'members/index.html', {'members':members}) #Templateに値を渡す

#詳細（おまけ）
def detail(request, id=id):
    member = get_object_or_404(Member, pk=id)
    return render(request, 'members/detail.html', {'member':member})

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