from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from palfullthrottle.models import User, ActivityPeriod

import datetime

class Command(BaseCommand):
    help = 'Add user details'

    def add_arguments(self, parser):
        parser.add_argument('id', type=str, help='enter user id')
        parser.add_argument('name', type=str, help='enter user name')
        parser.add_argument('tz', type=str, help='enter timezone info')
        parser.add_argument('--start_time', type=str, help='enter activity start datetime')
        parser.add_argument('--end_time', type=str, help='enter activity end datetime')

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                user_id, name, tz = options['id'], options['name'], options['tz']
                user, created = User.objects.get_or_create(
                            pk=user_id,
                            defaults={
                                'real_name': name,
                                'tz_info': tz
                            }
                        )
                if not created:
                    self.stdout.write(f'User {user_id} already exists!')
                    if user.real_name != name:
                        self.stdout.write(f'name provided does not match! Proceeding with user_id')
                    if user.tz_info != tz:
                        self.stdout.write('tz info provided does not match! Proceeding with user_id')
                else:
                    self.stdout.write(f'User {user_id} added!')

                if options.get('start_time', '') and options.get('end_time', ''):
                    start_time = datetime.datetime.strptime(options['start_time'], '%b %d %Y  %I:%M%p')
                    end_time = datetime.datetime.strptime(options['end_time'], '%b %d %Y %I:%M%p')
                    user_activity_period = user.activityperiod_set.create(start_time=start_time, end_time=end_time)
                    self.stdout.write(f'User activity added for {user_id}')
        except ValueError as e:
            self.stdout.write('Please check date time format!')


