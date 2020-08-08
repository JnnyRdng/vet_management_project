import pdb

from models.vet import Vet
from models.owner import Owner
from models.animal import Animal
from models.record import Record

import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository
import repositories.animal_repository as animal_repository
import repositories.record_repository as record_repository

record_repository.delete_all()
animal_repository.delete_all()
vet_repository.delete_all()
owner_repository.delete_all()

vet_1 = Vet("Sandra", "Jones")
vet_repository.save(vet_1)

owner_1 = Owner("Jam", "Jimson", "07162626243", "jim@email.com")
owner_2 = Owner("Jim", "Jamson", "07162626243", "jim@email.com")
owner_repository.save(owner_1)
owner_repository.save(owner_2)

pet_1 = Animal("Floof", "01-02-1987", "cat", owner_1, vet_1, "05-08-2020")
pet_2 = Animal("Fluff", "03-04-1958", "dog", owner_2, vet_1, "05-08-2020")
animal_repository.save(pet_1)
animal_repository.save(pet_2)

record_1 = Record("06-08-2020", "Cat is ill", pet_1)
record_2 = Record("07-08-2020", "Cat is still ill", pet_1)
record_3 = Record("06-08-2020", "Now dog is sick", pet_2)
record_repository.save(record_1)
record_repository.save(record_2)
record_repository.save(record_3)


pdb.set_trace()
