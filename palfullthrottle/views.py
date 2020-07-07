from django.shortcuts import render
from django.http import HttpResponse

import json

from .models import User

def get_user_details(request):
    data = {'ok': True, 'members': []}
    try:
        all_users = User.objects.all()
        for user in all_users:
            user_activity_period = [act_period.format_date() for act_period in user.activityperiod_set.all().order_by('start_time')]
            data['members'].append({
                    'id': user.user_id,
                    'real_name': user.real_name,
                    'tz': user.tz_info,
                    'activity_periods': user_activity_period
            })
    except:
        data['ok'] = False
        data['members'] = []

    return HttpResponse(json.dumps(data, indent=4))

