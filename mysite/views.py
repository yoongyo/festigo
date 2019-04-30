from django.shortcuts import render
import sys
sys.path.append('..')
from festival.models import Region


def main(request):
    regions = Region.objects.all()
    return render(request, 'main.html', {
        'regions':regions
    })

