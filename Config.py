import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "20400887"))
    API_HASH = os.environ.get("API_HASH", "535abea1d0cc67a4be1f57de026a846f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5893743036:AAETdm2RTVOrNMjb-IRFn0PBHUVVnvlKN58")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJQBuzO39VMFL5YE7npso-Q8zypjl5bcnXiQSCa478p3N_oUU0sLXyGwJFYihDOYINgljAtq0FeI6rJyydI0iuGeTApi0oKrM87driS5PW_EWEnEX4tlKfjQrrExawq90jUOFT0ojH5iKVG8Z2LlkiXTfQ0li4TsFF4ZxmbzFdDbsg5f0vxoT4NzVajAsjLMCmZE7HPaKcj0wDkhFcFKdmJ6XWVsFnK4XRG85vQLcfH9Gh7wPlz6RvLbSriSt3KC2DpSSXQcdbEet4n-Ro3F2D5hGzTAa1_aHtPTcl991KBuPBtVCffcCgqcU0sGwtHVE64telpyOeOij5r25agG3Itj81A=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Skyzo_Musicbot")
    SUPPORT = os.environ.get("SUPPORT", "Skyzo_musicbot") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "Skyzo_musicbot") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5702610439")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
