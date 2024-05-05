import fastf1

session = fastf1.get_session(2024, 'china', 'race', backend='fastf1')
session.load(telemetry=False, laps=False, weather=False)

def process_first_round(){


    
}

print (session.results)