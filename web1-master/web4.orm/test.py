from models.db_session import global_init, create_session
from models.__all_models import *

global_init("sqlite:///db/holidays_studio.db")
session = create_session()
client = Client(full_name="Chelik 1", phone=88005553535, email="ya_sobaka@ti_sobaka.com")
session.add(client)
session.commit()
