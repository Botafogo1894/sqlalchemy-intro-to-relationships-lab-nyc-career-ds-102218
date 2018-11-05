from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()

# add and commit the actors and roles below

#roles
forestgump = Role(character = "Forrest_Gump")
jimlovell = Role(character ='Jim_Lovell')
woody = Role(character ="Woody")
rlangdon = Role(character ="Robert_Langdon")

ppotts = Role(character ='Pepper_Potts')
mtenenbaum = Role(character ='Margot_Tenenbaum')

tdetective = Role(character ='True_Detective')
oldmen = Role(character ='Old_Men')

thanks = Actor(name='Tom Hanks')
thanks.roles = [forestgump, jimlovell, woody, rlangdon]
gwyneth = Actor(name="Gwyneth Paltrow")
gwyneth.roles = [ppotts, mtenenbaum]
wharelson = Actor(name="Woody Harrelson")
wharelson.roles = [tdetective, oldmen]

session.add_all([thanks, gwyneth, wharelson])
session.commit()

# forestgump, jimlovell, woody, rlangdon, ppotts, mtenenbaum, tdetective, oldmen
