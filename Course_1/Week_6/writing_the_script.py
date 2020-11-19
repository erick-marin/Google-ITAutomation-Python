"""
This script will process events for users logging and users logging out
from machines.  Additionally it will generate a report of events.

Author: Erick Marin
Date: 10/23/2020
"""


class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user


def get_event_date(event):
    """ Helper function that we'll use to sort the list. """
    return event.date


def current_users(events):
    """ Use the helper function as the parameter to the sort function
    to sort the list. """
    events.sort(key=get_event_date)

    # Create the dictionary to store the names end users of a machine.
    machines = {}
    # Iterate through our list of events
    for event in events:
        # Check if the machine affected by the event is in the dictionary.
        # If not, then add it with an empty set as a value.
        if event.machine not in machines:
            machines[event.machine] = set()
        # For the login events, we want to add the user to the list, and for
        # the logout events, we want to remove users from the list.
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout" and event.user in machines[event.machine]:
            machines[event.machine].remove(event.user)
    return machines


def generate_report(machines):
    """ Generate report of machine and users. """
    for machine, users in machines.items():
        # Only print if a machine has users of more that 0 elements.
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machines, user_list))


events_list = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'), ]

users = current_users(events_list)
# print(users)

generate_report(users)
