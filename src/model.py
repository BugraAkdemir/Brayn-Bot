from orm import Database
from orm import Model

class Person(Model):

    discord_id = int
    money = int
    work = str
    bank = int
    
    def __init__(self, discord_id, money, work, bank):
        self.discord_id = discord_id
        self.money = money
        self.work = work
        self.bank = bank
        
def get_user_or_false(discord_id):
    objects = Person.manager(db)
    users = list(objects.all())
    
    for user in users:
        if user.discord_id == discord_id:
            return user
    return False

db = Database('person.sqlite')
Person.db = db






