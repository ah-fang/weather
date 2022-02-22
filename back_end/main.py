from functions import *
from creds import open_weather_key
from tabulate import tabulate

# List of city IDs
city_sandiego = '5386053'
city_bloomington = '4254679'
city_murrieta = '5375911'
city_escondido = '5346827'

# List of cities that will be looped through
city_loop = [city_sandiego,
             city_escondido,
             city_murrieta,
             city_bloomington]

# temp displayed units, change to metric if you want
units = 'imperial'

#########################################
######### code starts here ##############
#########################################
df = create_df()
for city_id in city_loop:
    payload = call_open_weather(city_id, open_weather_key, units)
    extract_json(payload, df)
print(tabulate(df, headers='keys', tablefmt='psql', showindex=False, floatfmt='.2f'))
