import qiniu
from flask import Blueprint, request, make_response, jsonify
from utils import restful, zlcache
from io import BytesIO
from utils.captcha import Captcha

bp = Blueprint("common", __name__, url_prefix='/c')  # cms为蓝图名称、subdomain为子域名


@bp.route('/captcha/')
def graph_captcha():
    text, image = Captcha.gene_graph_captcha()
    zlcache.set(text.lower(), text.lower())  # 存储到memcached
    out = BytesIO()
    image.save(out, 'png')
    out.seek(0)  # 将文件指针设置为0
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    return resp


@bp.route('/uptoken/')
def uptoken():
    access_key = 'A82nBaNWAlj2pQcazU0IAdeVZUTm9zGK4N42OPIb'
    secret_key = 'ZVxmpdbLeFmJiU9f-234qG7onPh8HSXlwe95HtFB'

    q = qiniu.Auth(access_key, secret_key)

    bucket = 'rcptest2'
    token = q.upload_token(bucket)
    return jsonify({'uptoken': token})
