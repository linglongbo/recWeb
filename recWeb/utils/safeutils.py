# 防止黑客使用return_to跳转至其他页面

from urllib.parse import urlparse, urljoin
from flask import request


def is_safe_url(target):
    ref_url = urlparse(request.host_url)  # 将url分成域名、参数。。。。
    test_url = urlparse(urljoin(request.host_url, target))
    # 判断域名相等
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc
