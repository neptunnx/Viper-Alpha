import faker
from faker import Factory

fake_generator = Factory.create()
gened = int(input("Amount of ip's: "))
for i in range(gened):
  print(fake_generator.ipv4())
