from mycroft import MycroftSkill, intent_file_handler


class FakeMusicPlayer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('player.music.fake.intent')
    def handle_player_music_fake(self, message):
        self.speak_dialog('player.music.fake')


def create_skill():
    return FakeMusicPlayer()

