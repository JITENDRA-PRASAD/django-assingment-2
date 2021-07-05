from django.shortcuts import render

# Create your views here.
users = [{
    'name': 'jitendra prasad',
    'dob' : '29/04/1997',
    'position': 'SDE 1',
    'blogs': 'be happy' ,
},
{
    'name': 'ashish sharma',
    'dob' : '05/06/1998',
    'position': 'SDE 2',
    'blogs': 'live long',
},
{
    'name': 'vishesh meena',
    'dob' : '01/08/1997',
    'position':'SDE 3' ,
    'blogs': 'never die',
},
{
    'name': 'sonu meena',
    'dob' : '12/09/1997',
    'position': 'SDE 4',
    'blogs': 'i am with you',
}]

def display(request):
    return render(request,'friends/firstpage.html',{
        "users": users
    })

def buddy(request):
    return render(request,'friends/second.html', {
        'users':users
    })

def F_name(request, Name):
    friend = None
    for i in users:
        if i['name']==Name:
            friend = i
    if friend!= None:
        return render(request, 'friends/myfriend.html', {
            'dost': friend
        })
    else:

        return render(request,'friends/404.html')