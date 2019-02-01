# ccdi_alert
使用方法：
```
git clone https://github.com/relei1988/ccdi_alert.git
```

在get_info.py中找到
```
#bot = telegram.Bot(token='YOURTOKEN')
```
去掉注释并将telegram的token填上


在sendmessage中去除
```
#bot.send_message("@channelname", b)
```
的注释，并将@channelname改为自己的频道名