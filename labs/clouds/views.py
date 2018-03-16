from django.shortcuts import render
import csv, os

def index(request):
    return render(request, 'clouds/index.html')

def clouds(request):
    f = open('../labs_prof_filtered.csv', 'r')
    r = csv.reader(f)
    labs = []
    for row in r:
        if row[0] == 'Abbreviation': continue
        lab = {}
        lab['short'] = row[0]
        lab['full'] = row[1]
        lab['profs'] = row[2]
        lab['image_path'] = 'cloud_' + lab['short'] + '.png'
        if not os.path.isfile('../' + lab['image_path']): lab['image_path'] = None
        labs.append(lab)
    return render(request, 'clouds/clouds.html', {'labs': labs})
