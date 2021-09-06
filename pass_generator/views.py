
from django.shortcuts import render
from django.http  import HttpResponse
import random
# Create your views here.
def home(request):

    midic = {'name':'rene','dom':'Paseo'}
    return render(request,'generator/home.html')

def password(request):
    thepass = ''
    alfabeth =list('abcdefgijklmnopqqrstuvwxyz')

    if request.GET.get('uppercase',''):
        alfabeth.extend(list('ABCDEFGHIGKLMNOPQRESTUVWXYZ'))

    if request.GET.get('special',''):
        alfabeth.extend(list('!@#$%^&*()'))

    if request.GET.get('special',''):
        alfabeth.extend(list('!@#$%^&*()_.'))

    if request.GET.get('numbers',''):
        alfabeth.extend(list('0123456789'))

    length_pass = int(request.GET.get('length',7))


    for i in range(length_pass):
        thepass += random.choice(alfabeth)

    return render(request,'generator/password.html',{'password':thepass})

def about(request):

    DEV_SKILLS = {'tea': 'Password generator: Starts commercial operations as open source project in sep 2021',\
                  'dss': 'Diego Steve is Scrum Master, he has worked Instragram, Amazon. His ADN is profitable',\
                  'res': 'Rene Silva is Telematic enginner, his recent works deserve a notable award in techological innovation',\
                  'pms': 'The youngest software developer Pablo is a Crack in securty systems and big data analisys',\
                  'srs': 'Sofia Renata is a front-end developer, she is expert in JS, React, Node, JSon.',\
                  'mns': 'Midred Nataly is SalesSoft CEO and consulant of multiple startapps, She is Ruby on Rails expert & creative.'}

    s_skills=''
    s_skills = request.GET.get('softdev','tea')

    sof_skills = DEV_SKILLS[s_skills]


    return render(request,'generator/about.html',{'about_skills': sof_skills})
