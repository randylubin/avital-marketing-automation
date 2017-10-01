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
            'Zip',
            'Activity',
            'Phone',
            'Local / Visitor',
            'Referral Source',
            'Booking Type',
            'Media'
        ]]

with open('peek.csv', 'rU') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if 'Guide gratuity' not in row['Activity / Item'] and 'Alcohol Pairing' not in row['Activity / Item']:
            person = []
            person.append(row['First Name'])
            person.append(row['Last Name'])
            person.append(row['Email'])
            person.append(row['Postal/Zip Code'])
            person.append(row['Activity / Item'])
            person.append(row['Phone'])

            # Local / Visitor

                # California : 90001 - 96162
                # 93601 is first NorCal

                # NJ: 07001 - 08989
                # NY: 00501, 00544, 06390 AND 10001- 14925
                # CONN: 06001 - 06928

            zipCode = zipConvert(row['Postal/Zip Code'])

            if zipCode is not False:

                # Tristate Area
                if (6001 <= zipCode <= 6928) or (7001 <= zipCode <= 8989) or (10001 <= zipCode <= 14925) or (zipCode is 501) or (zipCode is 544) or (zipCode is 6390):
                    person.append('NY, NJ, CONN')

                # California
                elif zipCode >= 90001:
                    if zipCode < 93601:
                        person.append('Southern CA')
                    elif zipCode <= 96162:
                        person.append('Northern CA')
                    else:
                        person.append('')
                else:
                    person.append('')
            else:
                person.append('')



            # Referral Source

            person.append('Previous Customer')

            # Tour Type

            if 'Private' in row['Activity / Item']:
                person.append('Corporate')
            else:
                person.append('General')

            # Media

            if 'MEDIA' in row['Promotion Code']:
                person.append('Yes')
            else:
                person.append('No')

            people.append(person)

    with open("peek-output.csv", "wb") as peekF:
        writer = csv.writer(peekF)
        writer.writerows(people)

print people
