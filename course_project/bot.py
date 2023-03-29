
from random import randint
import logging

try:
    import settings
except ImportError:
    exit('DO cp settings.py.default settings.py and set token!')

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


log = logging.getLogger('bot')


def configure_logging():
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
    stream_handler.setLevel(logging.INFO)
    log.addHandler(stream_handler)

    file_handler = logging.FileHandler('bot.log', encoding='utf-8')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    file_handler.setLevel(logging.DEBUG)
    log.addHandler(file_handler)

    log.setLevel(logging.DEBUG)


class Bot:
    """
    Echo bot for vk.com
    Use python3.7
    """
    def __init__(self, group_id, token):
        """
        :param group_id: group id from group vk
        :param token: secret token
        """
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=settings.TOKEN)
        self.long_poller = VkBotLongPoll(self.vk, self.group_id)
        self.api = self.vk.get_api()

    def run(self):
        """Start bot."""
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception:
                log.exception('Ошибка в обработке события')

    def on_event(self, event):
        """
         Отправляет сообщение назад, если это текст.
         :param event: VkBotMessageEvent object
         :return: None
        """
        if event.type == VkBotEventType.MESSAGE_NEW:
            log.info('Отправляет сообщение назад')
            self.api.messages.send(
                message=event.message.text,
                random_id=randint(0, 2**20),
                peer_id=event.message.peer_id
            )
        else:
            log.info('Мы пока не умеем обрабатывать событие типа %s', event.type)


if __name__ == '__main__':
    configure_logging()
    bot = Bot(settings.GROUP_ID, settings.TOKEN)
    bot.run()
