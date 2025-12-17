from datetime import *

x = date(2043, 12, 24)
print(x.weekday())

heute = date.today()
geburtstag = date(2029,2,1)
differenz = geburtstag - heute
print(f"Ihre Bachelor-Verleihung ist in {differenz.days} Tagen")
