import os
import csv
os.environ.setdefault('DJANGO_SETTINGS_MODULE','batted_visualization.settings')

import django
django.setup()

#fake population script

from visualization_app.models import Hit, Batter, Pitcher



def import_data():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    temp=os.path.join(BASE_DIR,'batted_visualization')
    path=os.path.join(temp,'data')
    os.chdir(path) # changes the directory
    
    with open('batting_data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            p = Hit(date=row['date'],
                gamepk=row['gamepk'],
                hometeamid=row['hometeamid'],
                hometeamname=row['hometeamname'],
                awayteamid=row['awayteamid'],
                awayteamname=row['awayteamname'],
                parkid=row['parkid'],
                park=row['park'],
                batterid=row['batterid'],
                battername=row['battername'],
                batside=row['batside'],
                batterteamid=row['batterteamid'],
                pitcherid=row['pitcherid'],
                pitchername=row['pitchername'],
                pitcherteamid=row['pitcherteamid'],
                pitchside=row['pitchside'],
                balls=row['balls'],
                strikes=row['strikes'],
                result_type=row['result_type'],
                pitch_type=row['pitch_type'],
                pitch_speed=row['pitch_speed'],
                zone_location_x=row['zone_location_x'],
                zone_location_z=row['zone_location_z'],
                launch_speed=row['launch_speed'],
                launch_horiz_ang=row['launch_horiz_ang'],
                launch_vert_ang=row['launch_vert_ang'],
                landing_location_x=row['landing_location_x'],
                landing_location_y=row['landing_location_y'],
                hang_time=row['hang_time'])
            p.save()


            batter = Batter.objects.filter(batterid=row['batterid'])
            if len(batter)==0:
                if row['batterteamid'] == row['hometeamid']:
                    teamid = row['hometeamid']
                    teamname = row['hometeamname']
                else:
                    teamid = row['awayteamid']
                    teamname = row['awayteamname']
                batter = Batter(name=row['battername'],
                                batside=row['batside'],
                                teamid=teamid,
                                teamname=teamname,
                                batterid=row['batterid'])
                batter.save()

            pitcher = Pitcher.objects.filter(pitcherid=row['pitcherid'])
            if len(pitcher)==0:
                if row['pitcherteamid'] == row['hometeamid']:
                    teamid = row['hometeamid']
                    teamname = row['hometeamname']
                else:
                    teamid = row['awayteamid']
                    teamname = row['awayteamname']
                pitcher = Pitcher(name=row['pitchername'],
                                pitchside=row['pitchside'],
                                teamid=teamid,
                                teamname=teamname,
                                pitcherid=row['pitcherid'],
                                max_pitch_speed=row['pitch_speed'])
                pitcher.save()
            else:
                if pitcher[0].max_pitch_speed < float(row['pitch_speed']):
                    pitcher.update(max_pitch_speed=row['pitch_speed'])
            

if __name__ =='__main__':
    print("importing data!")
    import_data()
    print("import complete!")
