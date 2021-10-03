import argparse

parser = argparse.ArgumentParser(usage="%(prog)s [options] SUMMARY [BODY]")
parser.add_argument("SUMMARY", help="Notification title, for example 'New mail'")
parser.add_argument("BODY", help="Text of notification, multi-line supported. If BODY isn't set, just the SUMMARY is sent", default="", nargs="?")
parser.add_argument("-n", "--silent", help="send notification with no sound", default=False, action="store_true")
parser.add_argument("-r", "--recipient", metavar="chat_id", help="telegram chat_id (user_id) to send notification", type=int)
parser.add_argument("-t", "--token", help="set telegram bot token to use", type=str)
parser.add_argument("-s", "--stdin", help="read notification BODY from stdin", action="store_true")
parser.add_argument("-z", "--save", help="save recipient & token to config file and use them as defaults in future", action="store_true")
parser.add_argument("-w", "--raw", help="do not escape HTML tags in body (use with caution)", action="store_true")
options = parser.parse_args()
print(options)
