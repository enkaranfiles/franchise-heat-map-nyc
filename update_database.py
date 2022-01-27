
from update_database_commons import UpdateDatabase
from conf.conf import API_KEY


UpdateDatabase(API_KEY).get_data_of_shake_shack()
UpdateDatabase(API_KEY).get_data_of_five_guys()
UpdateDatabase(API_KEY).get_data_of_burger_king()
UpdateDatabase(API_KEY).get_data_of_mcdonalds()
