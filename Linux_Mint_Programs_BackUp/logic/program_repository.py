from mongoengine.connection import connect
from models.program import Program


class ProgramRepository():
    def __init__(self) -> None:
        connect(db='ProgramsToInstallDB', username='toastedguy2',
                password='Overblown-Chapped3-Mongoose', host='mongodb+srv://toastedguy2:Overblown-Chapped3-Mongoose@cluster0.r8vkd.mongodb.net/ProgramsToInstallDB?retryWrites=true&w=majority')

    def get_all(self):
        return Program.objects
