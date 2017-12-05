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

        bayAreaGuests = row['Northern California Emails'].split(',')

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

        southernCaliforniaGuests = row['Southern California Emails'].split(',')

        for soCalEmail in southernCaliforniaGuests:
            person = []
            person.append('Unknown')
            person.append('Unknown')
            person.append(soCalEmail)
            person.append(neighborhood)
            person.append('Southern CA')
            person.append('Previous Customer')
            if bookingType == 'Private':
                person.append('Corporate')
            elif bookingType == 'Public':
                person.append('General')
            else:
                person.append('')

            people.append(person)

        newYorkAreaGuests = row['NYC tri-state area emails'].split(',')

        for NYCEmails in newYorkAreaGuests:
            person = []
            person.append('Unknown')
            person.append('Unknown')
            person.append(NYCEmails)
            person.append(neighborhood)
            person.append('NY, NJ, CONN')
            person.append('Previous Customer')
            if bookingType == 'Private':
                person.append('Corporate')
            elif bookingType == 'Public':
                person.append('General')
            else:
                person.append('')

            people.append(person)

        visitingGuests = row['Other emails:'].split(',')

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
