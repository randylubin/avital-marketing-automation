import csv
import json

def zipConvert(zippy):
    try:
        int(zippy)
        return int(zippy)
    except ValueError:
        return False

people = [[
            'First Name',
            'Last Name',
            'Email',
            'Activity',
            'Local / Visitor',
            'Referral Source',
            'Booking Type',
        ]]

with open('ceSurvey.csv', 'rU') as f:
    reader = csv.DictReader(f)
    for row in reader:
        neighborhood = row['Neighborhood']
        bookingType = row['CE type']

        bayAreaGuests = row['Bay Area guest emails'].split(',')

        for localEmail in bayAreaGuests:
            person = []
            person.append('Unknown')
            person.append('Unknown')
            person.append(localEmail)
            person.append(neighborhood)
            person.append('Northern CA')
            person.append('Previous Customer')
            if bookingType == 'Private':
                person.append('Corporate')
            elif bookingType == 'Public':
                person.append('General')
            else:
                person.append('')

            people.append(person)

        visitingGuests = row['Visiting guest emails'].split(',')

        for visitorEmail in visitingGuests:
            person = []
            person.append('Unknown')
            person.append('Unknown')
            person.append(visitorEmail)
            person.append(neighborhood)
            person.append('')
            person.append('Previous Customer')
            if bookingType == 'Private':
                person.append('Corporate')
            elif bookingType == 'Public':
                person.append('General')
            else:
                person.append('')

            people.append(person)



    with open("ceSurvey-output.csv", "wb") as surveyF:
        writer = csv.writer(surveyF)
        writer.writerows(people)

print people
