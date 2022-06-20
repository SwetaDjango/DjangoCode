import os

# setting configurations for the project
os.environ.setdefault('DJANGO_SETTINGS_MODUlE', 'first_project.settings')

import django

django.setup()

###################

import random
from fourth_app.models import AccessRecord, Topic, Webpage
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[
        0]  # will return a tuple and we r just gonna grab first object of tuple.
    # The get_or_create() method is used to get an existing object from the database or create
    # it if it doesn’t exist. The get _or_create() method returns a tuple.
    # A first element is an object, and the second one boolean value (created is True, not created is False).
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        # get the topic for the entry
        top = add_topic()

        # create fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        #get_craete will return a tuple
        # This is one of those two query one command ORM methods. It would make a query to the database
        # with the given where clause query and if not found then it will
        # create a new entry in the table using the default values.

        # create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print('Populating Scripts ')
    populate(20)
    print('Populating Complete')
