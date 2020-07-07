from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True)
    real_name = models.CharField(max_length=50)
    tz_info = models.CharField(max_length=50)
    class Meta:
        db_table = 'user'

class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, db_column='user', on_delete=models.CASCADE)
    start_time = models.DateTimeField('session start datetime info')
    end_time = models.DateTimeField('session end datetime info')
    
    def format_date(self):
        formatted_start_date = self.start_time.strftime('%b %d %Y  %I:%M%p')
        formatted_end_date = self.end_time.strftime('%b %d %Y %I:%M%p')
        return {'start_time': formatted_start_date, 'end_time':formatted_end_date}
    class Meta:
        db_table = 'activity_period'
