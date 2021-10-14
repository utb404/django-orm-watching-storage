from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import format_duration
from django.shortcuts import render


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    passcard = Passcard.objects.filter(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    for visit in visits:
        passcard_visit = {
                'entered_at': visit.entered_at,
                'duration': format_duration(visit.get_duration()),
                'is_strange': visit.is_long()
            }
        this_passcard_visits.append(passcard_visit)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
