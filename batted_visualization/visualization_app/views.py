from django.shortcuts import render
from visualization_app.models import Hit, Batter, Pitcher
from . import forms
from django.shortcuts import redirect

# Create your views here.
def index(request):
    form = forms.NameSearch()
    data = Hit.objects.order_by('date')
    batter_info = Batter.objects.order_by('name')
    pitcher_info = Pitcher.objects.order_by('name')

    if request.method == 'POST':
        form = forms.NameSearch(request.POST)
        if form.is_valid():
            data = Hit.objects.filter(battername__icontains=form.data['name'])
            batter_info = Batter.objects.filter(name__icontains=form.data['name'])
            pitcher_info = Pitcher.objects.filter(name__icontains=form.data['name'])

    context_dict = {'hit_data':data, 'form':form,'batter_info':batter_info,'pitcher_info':pitcher_info}

    return render(request,'visualization_app/index.html', context=context_dict)

def batter_info(request, id):
    data = Hit.objects.filter(batterid__exact=id)
    batter = Batter.objects.get(batterid__exact=id)
    results = { 'all':'All Results', 
        'field_out':'Field Out',
        'single':'Single',
        'double':'Double',
        'triple':'Triple',
        'home_run':'Home Run',
        'grounded_into_double_play':'Grounded into double play',
        'double_play':'Double Play',
        'sac_fly':'Sacrifice Fly',
        'fielders_choice_out':'Fielders Choice',
        'force_out':'Force Out',
        'hit_by_pitch':'Hit By Pitch',
        'catcher_interf':'Catcher Interference',
        'field_error':'Field Error' }

    pitch_types = {
        'all':'All Results',
        'FA':'Fastball',
        'FF':'Four-seam fastball',
        'FT':'Two-steam fastball',
        'FC':'Fastball (cutter)',
        'SI':'Sinker',
        'FS':'Split-fingered',
        'SL':'Slider',
        'CH':'Changeup',
        'CU':'Curveball',
        'KC':'Knuckle-curve'
    }

    context_dict={'hit_data':data,'batter':batter,'results':results, 'pitch_types':pitch_types}


    return render(request,'visualization_app/hit_table.html', context=context_dict)

def pitcher_info(request, id):
    data= Hit.objects.filter(pitcherid__exact=id)
    pitcherdata= Pitcher.objects.get(pitcherid__exact=id)
    context_dict={'hit_data':data,"pitcher_data":pitcherdata}

    return render(request, 'visualization_app/pitcher.html',context=context_dict)