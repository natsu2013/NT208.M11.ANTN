from django.http import HttpResponseRedirect
from django.shortcuts import render
import datetime

from polls.models import Blog, Diet

# Chức năng đề xuất
result = {}
def get_info(request):
    global result
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        gender = request.POST['gender']
        gender = gender.lower()
        age = int(request.POST['age'])
        high = int(request.POST['high']) 
        weight = int(request.POST['weight'])
        
        if gender == 'nam':
            # Tính BMR cho nam
            BMR = 66.5 + (13.75 * weight) + (5.003 * high) - (6.755 * age)
        else:
            # Tính BMR cho nữ
            BMR = 55.1 + (9.563 * weight) + (1.850 * high) - (4.676 * age)

        # Tính Calo trung bình
        calo = BMR * 1.5

        type = 0
        if calo < 800:
            type = 1
        elif calo > 800 and calo <= 1100:
            type = 2
        elif calo > 1100 and calo <= 1400:
            type = 3
        elif calo > 1400 and calo <= 1700:
            type = 4
        elif calo > 1700 and calo <= 2000:
            type = 5
        elif calo > 2000 and calo <= 2300:
            type = 6
        elif calo > 2300 and calo <= 2600:
            type = 7
        else:
            type = 8

        high = high / 100
        BMI = weight / (2 * high)
        
        search = ""
        if BMI < 18.5:
            search = "weight_gain"
        elif BMI >= 25:
            search = "loss_gain"
        else:
            search = "other"

        result["search"] = search
        result["type"] = type

        return HttpResponseRedirect('/propose')

    return render(request, 'service.html')

def propose(request):
    blog = Blog.objects.filter(topic__contains=result["search"]).all()
    diet = Diet.objects.filter(type=result["type"]).all()
    return render(request, 'blog.html', {"blog": blog, "diet": diet})

#
def homeView(request):
    return render(request, 'home.html',
    {
        'now': datetime.datetime.now()
    }
)

#About
def about_view(request):
    return render(request, 'about.html')

#Begin menu
def service_view(request):
    return render(request, 'service.html')

def menu_view(request):
    return render(request, 'menu.html')
#Begin loss gain
def loss_gain_view(request):
    return render(request, 'main/loss_gain/loss_gain.html')
def loss_gain_paper_1_view(request):
    return render(request, 'main/loss_gain/LG(1).html')
def loss_gain_paper_2_view(request):
    return render(request, 'main/loss_gain/LG(2).html')
def loss_gain_paper_3_view(request):
    return render(request, 'main/loss_gain/LG(3).html')
def loss_gain_paper_4_view(request):
    return render(request, 'main/loss_gain/LG(4).html')
def loss_gain_paper_5_view(request):
    return render(request, 'main/loss_gain/LG(5).html')
def loss_gain_paper_6_view(request):
    return render(request, 'main/loss_gain/LG(6).html')

#begin vegan
def vegan_view(request):
    return render(request, 'main/vegan/vegan.html')
def vegan_paper_1_view(request):
    return render(request, 'main/vegan/vegan(1).html')
def vegan_paper_2_view(request):
    return render(request, 'main/vegan/vegan(2).html')
def vegan_paper_3_view(request):
    return render(request, 'main/vegan/vegan(3).html')

#Begin other
def other_view(request):
    return render(request, 'main/other/other.html')
def other_paper_1_view(request):
    return render(request, 'main/other/other(1).html')
def other_paper_2_view(request):
    return render(request, 'main/other/other(2).html')
def other_paper_3_view(request):
    return render(request, 'main/other/other(3).html')
def other_paper_4_view(request):
    return render(request, 'main/other/other(4).html')
def other_paper_5_view(request):
    return render(request, 'main/other/other(5).html')
def other_paper_6_view(request):
    return render(request, 'main/other/other(6).html')
def other_paper_7_view(request):
    return render(request, 'main/other/other(7).html')


#weight gain
def weight_gain(request):
    return render(request, 'main/weight gain/weight_gain.html')
def weight_gain_paper(request):
    return render(request, 'main/weight gain/weight_gain_paper.html')
def weight_gain_paper_1(request):
    return render(request, 'main/weight gain/weight_gain_paper(1).html')
def weight_gain_paper_2(request):
    return render(request, 'main/weight gain/weight_gain_paper(2).html')
