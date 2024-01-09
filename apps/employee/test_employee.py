from datetime import date
from .models import Position
from .models import Graduation
from apps.mosque.models import Mosque
from apps.common.regions import Regions, Districts

test_employee = [
    {
        'name': "alijon",
        'surname': "valijonov",
        'last_name': "valiyev",
        'phone_number': "+998902003011",
        'address': "45.76800194433285,32443619.846563343",
        'image': None,
        'gender': "male",
        'position': Position.objects.get(id=1),
        'nation': "1",
        'birth_date': date.today(),
        'education': "1",
        'graduated_year': date.today(),
        'diploma_number': "AB123456787654",
        'academic_degree': "2",
        # 'mosque': Mosque.objects.get(id=27),
        'achievement': "1",
    },
    {
        'name': "mirjahon",
        'surname': "halilov",
        'last_name': "aziz",
        'phone_number': "+998902003012",
        'address': "45.76800194433285,32443619.846563343",
        'image': None,
        'gender': "male",
        'position': Position.objects.get(id=1),
        'nation': "1",
        'birth_date': date.today(),
        'education': "1",
        'graduated_year': date.today(),
        'diploma_number': "AB1234562347654",
        'academic_degree': "2",
        # 'mosque': Mosque.objects.get(id=27),
        'achievement': "1",
    },
    {
        'name': "Qodirjon",
        'surname': "asad",
        'last_name': "anvarov",
        'phone_number': "+998902003013",
        'address': "45.76800194433285,32443619.846563343",
        'image': None,
        'gender': "male",
        'position': Position.objects.get(id=1),
        'nation': "1",
        'birth_date': date.today(),
        'education': "1",
        'graduated_year': date.today(),
        'diploma_number': "AB1234568767654",
        'academic_degree': "2",
        # 'mosque': Mosque.objects.get(id=27),
        'achievement': "1",
    },
    {
        'name': "vohibjon",
        'surname': "shami",
        'last_name': "sadullayev",
        'phone_number': "+998902003014",
        'address': "45.76800194433285,32443619.846563343",
        'image': None,
        'gender': "male",
        'position': Position.objects.get(id=1),
        'nation': "1",
        'birth_date': date.today(),
        'education': "1",
        'graduated_year': date.today(),
        'diploma_number': "AB1234522227654",
        'academic_degree': "2",
        # 'mosque': Mosque.objects.get(id=27),
        'achievement': "1",
    },
    {
        'name': "sodiq",
        'surname': "anvar",
        'last_name': "ogabekov",
        'phone_number': "+998902003015",
        'address': "45.76800194433285,32443619.846563343",
        'image': None,
        'gender': "male",
        'position': Position.objects.get(id=1),
        'nation': "1",
        'birth_date': date.today(),
        'education': "1",
        'graduated_year': date.today(),
        'diploma_number': "AB12345555557654",
        'academic_degree': "2",
        # 'mosque': Mosque.objects.get(id=27),
        'achievement': "1",
    },
    {
        'name': "jamshid",
        'surname': "hoshim",
        'last_name': "abduvali",
        'phone_number': "+998902003016",
        'address': "45.76800194433285,32443619.846563343",
        'image': None,
        'gender': "male",
        'position': Position.objects.get(id=1),
        'nation': "1",
        'birth_date': date.today(),
        'education': "1",
        'graduated_year': date.today(),
        'diploma_number': "AB1234522000654",
        'academic_degree': "2",
        # 'mosque': Mosque.objects.get(id=27),
        'achievement': "1",
    },
]

test_users = [
    {
        "email": "jhbj@gmail.com",
        "role": "3",
        "region": Regions.objects.get(id=7),
        "district": Districts.objects.get(id=52),
    },
    {
        "email": "jhbj@gmail.com",
        "role": "3",
        "region": Regions.objects.get(id=7),
        "district": Districts.objects.get(id=53),
    },
    {
        "email": "jhbj@gmail.com",
        "role": "3",
        "region": Regions.objects.get(id=7),
        "district": Districts.objects.get(id=54),
    },
    {
        "email": "jhbj@gmail.com",
        "role": "3",
        "region": Regions.objects.get(id=7),
        "district": Districts.objects.get(id=55),
    },
    {
        "email": "jhbj@gmail.com",
        "role": "3",
        "region": Regions.objects.get(id=7),
        "district": Districts.objects.get(id=56),
    },
    {
        "email": "jhbj@gmail.com",
        "role": "3",
        "region": Regions.objects.get(id=7),
        "district": Districts.objects.get(id=57),
    }
]
