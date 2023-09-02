from product.models import Brand, Product
import random
from faker import Faker
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


def seed_brand(n):
    fake = Faker()
    images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg',
              '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg', '12.jpg']
    for _ in range(n):
        Brand.objects.create(
            name=fake.name(),
            image=f'brands/{images[random.randint(0,10)]}'
        )
    print(f'seed {n} Brands Successfully')


def seed_product(n):
    fake = Faker()
    images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg',
              '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg', '12.jpg']
    flags = ['New', 'Sale', 'Feature']

    for _ in range(n):

        Product.objects.create(
            name=fake.name(),
            image=f'brands/{images[random.randint(0,11)]}',
            flag=flags[random.randint(0, 2)],
            price=round(random.uniform(20.99, 99.99), 2),
            sku=random.randint(1000, 1000000),
            subtitle=fake.text(max_nb_chars=250),
            description=fake.text(max_nb_chars=2500),
            quantity=random.randint(0, 30),
            brand=Brand.objects.get(id=random.randint(1, 105))

        )

        print(f'seed {n} Product Successfully')

def seed_product(n):
    fake = Faker()
    images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg',
              '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg', '12.jpg']
    flags = ['New', 'Sale', 'Feature']

    for _ in range(n):

        Product.objects.create(
            name=fake.name(),
            image=f'brands/{images[random.randint(0,11)]}',
            flag=flags[random.randint(0, 2)],
            price=round(random.uniform(20.99, 99.99), 2),
            sku=random.randint(1000, 1000000),
            subtitle=fake.text(max_nb_chars=250),
            description=fake.text(max_nb_chars=2500),
            quantity=random.randint(0, 30),
            brand=Brand.objects.get(id=random.randint(1, 105))

        )

        print(f'seed {n} Product Successfully')




seed_brand(2000)
#seed_product(5)

