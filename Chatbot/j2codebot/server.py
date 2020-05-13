from flask import Flask, request
from server_aux import verify_webhook, is_user_message, respond

Callback_URL = "https://00d2fb4f.ngrok.io/webhook"

FB_API_URL = 'https://graph.facebook.com/v2.6/me/messages'
VERIFY_TOKEN = 'j2_bot'# <paste your verify token here>
PAGE_ACCESS_TOKEN = "EAALHBXafgEgBAFZAOzbqZCZAxTvGQjHLfGPd8RWEW7QkvGA3lsqZCKZBJ9Hy938fqR7jdYZAzZA2IlfpHXwHKZC3pQLLOk0ncmA4qx52fBpMIZA6TJzouLEmoO5RZAhw0EbnayVDFerFgYtg7QN2mDP9AZB0lwZBzGxXuM5uYbtWrzkfmwZDZD"

app = Flask(__name__)


# route to listen and respond to Messenger
#https://00d2fb4f.ngrok.io/webhook
@app.route("/webhook", methods=['GET','POST'])
def listen():
    print("entering listen function")
    """This is the main function flask uses to listen at the `/webhook` endpoint"""
    if request.method == 'GET':
        print("GET method")
        return verify_webhook(request, VERIFY_TOKEN)

    if request.method == 'POST':
        print("POST method")
        payload = request.json
        event = payload['entry'][0]['messaging']
        for x in event:
            if is_user_message(x):
                text = x['message']['text']
                sender_id = x['sender']['id']
                respond(sender_id, text, FB_API_URL, PAGE_ACCESS_TOKEN)

        return "ok"



# route to test that your flask app is running
#https://00d2fb4f.ngrok.io/test
@app.route("/test")
def test():
    return "Your messenger app is running"


# route to check the feedback of a specific query:
#https://00d2fb4f.ngrok.io/test_query?query=hello
@app.route("/test_query")
def test_query():
    sender_id = "admin"
    query = request.args.get('query', default = "", type = str)
    return respond(sender_id, query, FB_API_URL, PAGE_ACCESS_TOKEN)
