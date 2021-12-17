from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import DomainCreate, GroupDomainCreate
from .models import *
from .access import AccessDomain
import datetime

# Create your views here.
def register_dom(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            print ('post method')
            try:
                post = request.POST.copy()
                subDomain = post['sub_domain']
                groupDomain = post['group_domain']
                domainName = subDomain+'.'+groupDomain
                if not Domain.objects.filter(sub_domain=domainName).exists():
                    # or set several values from dict
                    post.update({'sub_domain': domainName, 'group_domain': groupDomain})
                    # and update original POST in the end
                    request.POST = post
                    today = datetime.datetime.utcnow()+datetime.timedelta(hours=7)
                    print (today)
                    form = DomainCreate(request.POST)
                    if form.is_valid():
                        form.save()
                        print ('insert domain data success')
                        messages.success(request, "sukses")
                        
                else:
                    print ('duplicated')
                    messages.warning(request, 'duplicate')
                    subdom = subDomain
                    print (subdom)
                    context = {'form' : DomainCreate(), 'domain' : Domain.objects.all(), 'cpanel' : GroupDomain.objects.all(), 'subdom': subDomain}
                    return render(request, 'domregis/form-domain.html', context)
                    #return redirect('index')
            except Exception as err:
                print (err)
            print ('accessDomain go')
            try:
                AccessDomain(domainName, groupDomain).register()
            except Exception as err:
                print (err)
            return redirect('domregis:register_dom')
            
        context = {'form' : DomainCreate(), 'domain' : Domain.objects.all(), 'cpanel' : GroupDomain.objects.all()}
        return render(request, 'domregis/form-domain.html', context)
    return redirect('account:signin')

def delete_dom(request, task_id):
    try:
        # mengambil data domain yang akan dihapus berdasarkan task id
        task = Domain.objects.get(pk=task_id)
        # menghapus data dari table Domain
        task.delete()
        # mengeset pesan sukses dan redirect ke halaman daftar task
        messages.error(request, 'delete')
        return redirect('domregis:register_dom')
    except Domain.DoesNotExist:
        # Jika data task tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Task tidak ditemukan.")
    
def register_cpanel(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                post = request.POST.copy()
                groupDomain = post['group_domain']
                cpanelDomain = post['cpanel_domain']
                #domainName = subDomain+'.'+groupDomain
                if not GroupDomain.objects.filter(group_domain=groupDomain).exists():
                    # or set several values from dict
                    post.update({'group_domain': groupDomain, 'cpanel_domain': cpanelDomain})
                    # and update original POST in the end
                    request.POST = post
                    form = GroupDomainCreate(request.POST)
                    if form.is_valid():
                        form.save()
                        print ('insert cpanel data success')
                        messages.success(request, "sukses")
                        
                else:
                    print ('duplicated')
                    messages.warning(request, 'duplicate')
                    
                    context = {'form' : GroupDomainCreate(), 'cpanel' : GroupDomain.objects.all() }
                    return render(request, 'domregis/form-cpanel.html', context)
                    #return redirect('index')
            except Exception as err:
                print (err)
            #domainUsed = AccessDomain(domainName, groupDomain).register()
            return redirect('domregis:register_cpanel')
        print ('cpanel')
        context = {'form_cpanel' : GroupDomainCreate(), 'cpanel' : GroupDomain.objects.all()}
        return render(request, 'domregis/form-cpanel.html', context)
    return redirect('account:signin')

def delete_cpanel(request, task_id):
    try:
        # mengambil data domain yang akan dihapus berdasarkan task id
        task = GroupDomain.objects.get(pk=task_id)
        # menghapus data dari table Domain
        task.delete()
        # mengeset pesan sukses dan redirect ke halaman daftar task
        messages.error(request, 'delete')
        return redirect('domregis:register_cpanel')
    except GroupDomain.DoesNotExist:
        # Jika data task tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Task tidak ditemukan.")