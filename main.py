#Official Open Source Library for PPS API
#Linrary Importing
import requests

#Init global data
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
api_url = "http://cq49350.tmweb.ru/api/"
#Function for auth as bot account
def auth(bot_id, bot_secret_key, return_key = True):   
    url = "http://cq49350.tmweb.ru/api/auth_bot?bot_id=" + str(bot_id) + "&bot_secret_key=" + str(bot_secret_key)
    res = requests.get(url, headers = headers)
    ans = res.json()
    try:
        access_key = ans['key']
    except:
        access_key = False
    if access_key and return_key:
        return access_key
    else:
        return ans
#This function is check_key method of API
def check_key(bot_id, access_key, return_stat = True):
    url = api_url + "check_key?bot_id=" + str(bot_id) + "&access_key=" + str(access_key)
    res = requests.get(url, headers = headers)
    ans = res.json()
    if return_stat:
        try:
            return ans['correct']
        except:
            return False
    else:
        return ans
#This function returns all or some of the conversations the bot is in
def get_all_convs(bot_id, access_key, limit = 0):
    url = api_url + "get_bot_convs?bot_id=" + str(bot_id) + "&access_key=" + str(access_key) + "&limit=" + str(limit)
    res = requests.get(url, headers = headers)
    ans = res.json()
    return ans
#Send Message in conversation
def send_message(bot_id, access_key, message, conv_id):
    url = api_url + "send_message?bot_id=" + str(bot_id) + "&access_key=" + str(access_key) + "&message=" + str(message) + "&conv_id=" + str(conv_id)
    res = requests.get(url, headers = headers)
    ans = res.json()
    return ans
#Get last message give id of last message in current conv/ It using in STS API
def get_last_message(bot_id, access_key, conv_id):
    url = api_url + "get_last_message?bot_id=" + str(bot_id) + "&access_key=" + str(access_key) + "&conv_id=" + str(conv_id)
    res = requests.get(url, headers = headers)
    return res.json()
