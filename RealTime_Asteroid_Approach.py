import json, turtle, urllib.request, time
from datetime import date
from datetime import datetime
from datetime import timedelta
from urllib.error import HTTPError

file = open("today.txt","w")
file1 = open("week.txt","w")


def asteroids_approach(startDate, enddate,filename):
    # Our JSON request to retrieve data about asteroids approaching planet Earth.
    url = "https://api.nasa.gov/neo/rest/v1/feed?start_date=" + startDate + "&end_date=" + enddate + "&api_key=DEMO_KEY"

    response = urllib.request.urlopen(url)


    result = json.loads(response.read())

    print("Today " + str(result["element_count"]) + " asteroids will be passing close to planet Earth:")
    print("")
    asteroids = result["near_earth_objects"]

    # Parsing all the JSON data:
    for asteroid in asteroids:
        for field in asteroids[asteroid]:
            try:
                print("Asteroid Name: " + field["name"])
                filename.writelines("Asteroid Name: " + field["name"]+"\n")
                print("Estimated Diameter: " + str(field["estimated_diameter"]["meters"]["estimated_diameter_min"] +
                                                   field["estimated_diameter"]["meters"][
                                                       "estimated_diameter_max"] / 2) + " meters")
                filename.writelines("Estimated Diameter: " + str(field["estimated_diameter"]["meters"]["estimated_diameter_min"] +
                                                   field["estimated_diameter"]["meters"][
                                                       "estimated_diameter_max"] / 2) + " meters\n")
                print("Close Approach Date & Time: " + field["close_approach_data"][0]["close_approach_date_full"])
                filename.writelines("Close Approach Date & Time: " + field["close_approach_data"][0]["close_approach_date_full"]+"\n")
                print("Velocity: " + str(
                    field["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"]) + " km/h\n")
                filename.writelines("Velocity: " + str(
                    field["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"]) + " km/h\n")
                print("Distance to Earth: " + str(field["close_approach_data"][0]["miss_distance"]["kilometers"]) + " km")
                filename.writelines("Distance to Earth: " + str(field["close_approach_data"][0]["miss_distance"]["kilometers"]) + " km\n")

                if field["is_potentially_hazardous_asteroid"]:
                    print("This asteroid could be dangerous to planet Earth!")
                    filename.writelines("This asteroid could be dangerous to planet Earth!\n")
                else:
                    print("This asteroid poses not threat to planet Earth!")
                    filename.writelines("This asteroid poses not threat to planet Earth!\n")
            except:
                print("Unable to access all data.")
            print("--------------------\n")
            filename.writelines("--------------------\n")


today = time.strftime('%Y-%m-%d', time.gmtime())
print("Asteroid approach today..................")
file.writelines("Asteroid approach today..................\n")
print("Date: "+ today)
file.writelines("Date: "+ today+"\n\n")
asteroids_approach(today, today,file)

startDate = datetime.today()+timedelta(days=1)
startDate = startDate.strftime('%Y-%m-%d')
endDate = datetime.today() + timedelta(days=8)
endDate = endDate.strftime('%Y-%m-%d')
print("Asteroid approach for next 7 days...................")
file1.writelines("Asteroid approach for next 7 days...................\n")
print("From: " + startDate)
file1.writelines("From: " + startDate+"\n")
print("To: " + endDate)
file1.writelines("To: " + endDate+"\n\n")
asteroids_approach(startDate, endDate,file1)
file1.close()
