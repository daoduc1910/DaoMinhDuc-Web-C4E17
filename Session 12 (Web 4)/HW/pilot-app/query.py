from models.service import Service
import mlab

mlab.connect()

id_to_find = "5afad2cc533daa1c1c72b592"


hera = Service.objects.with_id(id_to_find) 

if hera is not None:
    # berry.delete()
    print(hera.address,",", berry.height)
    hera.update(set__address = "Nguyễn Khánh Toàn",
                 set__height = 420)

    hera.reload()
    print(hera.address,",", hera.height)


else:
    print("Service not found")

