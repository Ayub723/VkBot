from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import time

print("")
print("----------------------------------- VK BOT -----------------------------------")
print("")

login, password = "89635899739", "ad9559amad9559amad9559am"
vk_session = vk_api.VkApi(login, password)
vk_session.auth()

token = "6a7e330e6878615d74f35a88325220c0b52308042026c86797a947ff89cb5e4c347e2ed603b38aded5b6c"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
print("VB: Done!")
print("")
while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст сообщения: ' + str(event.text))
            print(event.user_id)
            response = event.text.lower()
            if event.from_user and not (event.from_me):
                if response == "ты бот?":
                    time.sleep(0.5)
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Да, меня запрограммировали. Сижу.', 'random_id': 0})
                if response == "ты тупой":
                    time.sleep(0.5)
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Я уважаю людей за их лексику! Пожайлуста не говорите такие вещи. &#128521;', 'random_id': 0})
                if response == "кто админ?":
                    time.sleep(0.5)
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Держите контакты создателя! &#128521; \n\n Вот ссылка на его страницу! \n Ссылка: vk.com/arseniivorono', 'random_id': 0})
                if response == "сколько времени?":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Сейчас времени: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")), 'random_id': 0})
