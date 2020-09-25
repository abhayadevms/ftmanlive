from django.core.management.base import BaseCommand, CommandError
import django
from random import *
from faker import Faker
import random
from ManApi.models import User, UserActivity

django.setup()
fake = Faker()


class Command(BaseCommand):

    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('num', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **option):
        option = option['num']

        for i in range(option):
            users = User.objects.create(u_id=random.randint(1, 1000), real_name=fake.name(), tz=fake.timezone())

            for j in range(0, randint(0, 4)):
                users.activity_periods.add(
                    UserActivity.objects.create(start_time=fake.date_time(), end_time=fake.date_time()))

        self.stdout.write(self.style.SUCCESS('successfully Added member!'))
