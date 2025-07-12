from address import Address
from mailing import MaiLing
to_address = Address ("603000","Nizhniy Novgorod", "Zalomova", "1", "1")
from_address = Address ("603000","Nizhniy Novgorod", "Zalomova", "2", "1")
mailing = MaiLing (to_address,from_address,track='23',cost='100')

print(mailing)