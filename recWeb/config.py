import os

SECRET_KEY = os.urandom(24)

DEBUG = True

DB_USERNAME = 'root'
DB_PASSWORD = '299086'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'zlbbs'


# PERMANENT_SESSION_LIFETIME =

DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False


CMS_USER_ID = 'WANGJIANBO'
FRONT_USER_ID = 'wangjianbo'

MAIL_SERVER = 'smtp.qq.com'
MAIL_PROT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = "2990863838@qq.com"
MAIL_PASSWORD = "chvauipurvmmdeai"
MAIL_DEFAULT_SENDER = "2990863838@qq.com"
MAIL_DEBUG = True

# MAIL_SERVER: 'smtp.qq.com'
# MAIL_PORT: 465
# # MAIL_USE_TLS: True
# MAIL_USE_SSL: True
# # MAIL_DEBUG : 默认为 app.debug
# MAIL_USERNAME: "2990863838@qq.com"
# MAIL_PASSWORD: "chvauipurvmmdeai"
# MAIL_DEFAULT_SENDER: "2990863838@qq.com"


# 短信应用 SDK AppID
appid = 1400378659  # SDK AppID 以1400开头
# 短信应用 SDK AppKey
appkey = "6fd89c3000c31b1af86d1c5e418abc7c"
# 需要发送短信的手机号码
phone_numbers = ["15031995733"]
# 短信模板ID，需要在短信控制台中申请
template_id = 621103  # NOTE: 这里的模板 ID`7839`只是示例，真实的模板 ID 需要在短信控制台中申请
# 签名
sms_sign = "智慧菜谱"  # NOTE: 签名参数使用的是`签名内容`，而不是`签名ID`。这里的签名"腾讯云"只是示例，真实的签名需要在短信控制台中申请

# 上传到本地
UEDITOR_UPLOAD_PATH = os.path.join(os.path.dirname(__file__),'images')
# Ueditor、七牛云的相关配置
UEDITOR_UPLOAD_TO_QINIU = True
UEDITOR_QINIU_ACCESS_KEY = "A82nBaNWAlj2pQcazU0IAdeVZUTm9zGK4N42OPIb"
UEDITOR_QINIU_SECRET_KEY = "ZVxmpdbLeFmJiU9f-234qG7onPh8HSXlwe95HtFB"
UEDITOR_QINIU_BUCKET_NAME = "rcptest2"
UEDITOR_QINIU_DOMAIN = "http://qb82es7xg.bkt.clouddn.com/"

# flask-paginate的相关配置
PER_PAGE = 5

# celery相关的配置
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"

