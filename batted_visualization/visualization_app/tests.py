from django.test import TestCase
from visualization_app.models import Hit, Batter, Pitcher
import datetime
# Create your tests here.

class HitTestCase(TestCase):
    def setUp(self):
        datetime_object = datetime.datetime.now()
        Hit.objects.create(date= datetime_object,
                            gamepk= 123723,
                            hometeamid= 1223423,
                            hometeamname='homeName',
                            awayteamid=123123,
                            awayteamname='wayteam',
                            parkid=1208763,
                            park='parkname',
                            batterid=1278923,
                            battername='John',
                            batside='R',
                            batterteamid=123423,
                            pitcherid=456234,
                            pitchername='Jane',
                            pitcherteamid=745634,
                            pitchside='L',
                            balls=2,
                            strikes=1,
                            result_type='home_run',
                            pitch_type='FF',
                            pitch_speed=100.0000000,
                            zone_location_x=150.0000000,
                            zone_location_z=200.0000000,
                            launch_speed=110.0000000,
                            launch_vert_ang=50.0000000,
                            launch_horiz_ang=90.0000000,
                            landing_location_x=90.0000000,
                            landing_location_y=5.0000000,
                            hang_time=4.0000000,
        )

    def test_hit_string(self):
        test_date = datetime.datetime.now()
        hit = Hit.objects.all()[:1]
        self.assertEqual(str(hit[0]),test_date.strftime('%m/%d/%Y')+" : John")