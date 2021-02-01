attendees = ["Ken", "Lena", "Treasure"]
attendees.append("Ashley")
attendees.extend(["James", "Gail"])
optional_attendees = ["Ben", "Dave"]
potential_attendees = attendees + optional_attendees

print('There are {} potential attendees currently'.format(len(potential_attendees)))
print("Attendees: ")
for attendee in attendees:
    print("* " + attendee)
    print()

def display(event, attendees):
    people = attendees.copy()
    print(event + ": ")
    presenter = people.pop(0)
    print("========> ", presenter, "<========")
    for person in people:
        print("* " + person)
    print()

display("General Session", attendees)
display("breakout One", attendees)

to_line = ", ".join(attendees)
cc_line = ", ".join(optional_attendees)

print("To: " + to_line)
print("CC: " + cc_line)