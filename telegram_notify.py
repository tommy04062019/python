import logging
class Telegram(object):
    def __init__(self, api_token):
        self.api_url = "https://api.telegram.org/bot{}/".format(api_token)
    
    def method(self, method_name, data):
        r = requests.post(self.api_url + method_name, data=data)
        if r.status_code != 200:
          logging.error(r.json())
        return r.json()

    def send_message(self, user_id, text, disable_notification=False):
        return self.method("sendMessage", {"chat_id": user_id,
                                           "text": text,
                                           "disable_notification": disable_notification,
                                           "parse_mode": "HTML"})
