import csv
import json

def zipConvert(zippy):
    try:
        int(zippy)
        return int(zippy)
    except ValueError:
        return False

people = [[
            'Email',
            'Previous Neighborhood Activity',
            'State/Region',
            'Previous Tour Customer',
            'Contact Added Via Source',
            'Gets Tour Marketing Emails'
        ]]

with open('ceSurvey.csv', 'rU') as f:
    reader = csv.DictReader(f)
    for row in reader:
        neighborhood = row['Neighborhood:']
        bookingType = row['Tour Type']
        if bookingType == "Private":
            neighborhood = "Private " + neighborhood

        southernCaliforniaGuests = row['Southern California Emails'].split(',')

        for southernCaliforniaEmail in southernCaliforniaGuests:
            person = []
            person.append(southernCaliforniaEmail)
            person.append(neighborhood)
            person.append('Southern CA')
            person.append('Yes')
            person.append('On Tour Sign Up')
            person.append('Yes')

            people.append(person)

        bayAreaGuests = row['Northern California Emails'].split(',')

        for bayAreaEmail in bayAreaGuests:
            person = []
            person.append(bayAreaEmail)
            person.append(neighborhood)
            person.append('Northern CA')
            person.append('Yes')
            person.append('On Tour Sign Up')
            person.append('Yes')

            people.append(person)

        newYorkAreaGuests = row['NYC tri-state area emails'].split(',')

        for NYCEmail in newYorkAreaGuests:
            person = []
            person.append(NYCEmail)
            person.append(neighborhood)
            person.append('NY, NJ, CONN')
            person.append('Yes')
            person.append('On Tour Sign Up')
            person.append('Yes')

            people.append(person)

        visitingGuests = row['Other emails:'].split(',')

        for visitorEmail in visitingGuests:
            person = []
            person.append(visitorEmail)
            person.append(neighborhood)
            person.append('')
            person.append('Yes')
            person.append('On Tour Sign Up')
            person.append('Yes')

            people.append(person)

        privateGuests = row['Guest email addresses:'].split(',')

        for guestEmail in privateGuests:
            person = []
            person.append(guestEmail)
            person.append(neighborhood)
            person.append('Southern CA')
            person.append('Yes')
            person.append('On Tour Sign Up')
            person.append('Yes')

            people.append(person)

    with open("ceSurvey-output.csv", "wb") as surveyF:
        writer = csv.writer(surveyF)
        writer.writerows(people)

print people
