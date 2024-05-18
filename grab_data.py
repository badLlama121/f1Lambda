import fastf1
import csv

race = 'miami'

session = fastf1.get_session(2024, race, 'race')
session.load(telemetry=False, laps=False, weather=False)
drivers = session.drivers
print (session.results)

print(session.get_driver('VER'))

with open('results.csv', 'w') as file:
        file.writelines('Driver,Round1 Points, Round2 Points,Round3 Points\n')
        for driver in drivers:
            row = (session.get_driver(driver).BroadcastName + ',' + str(int(session.get_driver(driver).Points)) + ',' + str(int((session.get_driver(driver).Points))*2) + ',' + str((session.get_driver(driver).GridPosition - session.get_driver(driver).Position )) + '\n')
            file.writelines(row)