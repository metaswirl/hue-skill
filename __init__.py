from mycroft import MycroftSkill, intent_file_handler


class Hue(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('hue.intent')
    def handle_hue(self, message):
        self.speak_dialog('hue')


def create_skill():
    return Hue()

