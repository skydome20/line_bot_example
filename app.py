
"""
Heroku安裝及使用教學：https://github.com/twtrubiks/Deploying-Flask-To-Heroku
line-python-sdk(程式碼教學)：https://github.com/line/line-bot-sdk-python



git add .
git commit -am "make it better"
git push heroku master

"""
 
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
from random import choice
app = Flask(__name__)
# 設定linebot的基本資訊
line_bot_api = LineBotApi('xxxxxxxxxxx')
handler = WebhookHandler('xxxxxxxxxxxx') # channel secret


# 設定route 和 webhook
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

	
# 文字handle
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
	text = event.message.text

			
	
	if ("嗨" in text):
		line_bot_api.reply_message(
			event.reply_token, 
			TextSendMessage(text="""呵呵
"""))		

					
	# 其他
	else:
		line_bot_api.reply_message(
			event.reply_token, 
			TextSendMessage(text="""這是當沒有關鍵字符合時，就預設的回覆~~
"""))						
						



# 貼圖handle
@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):

    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(sticker_id = choice(['146','145','140','170','507']),
						   package_id = '2'))
						   

if __name__ == "__main__":
    app.run()
	
	
	
	
	
	
	
	
