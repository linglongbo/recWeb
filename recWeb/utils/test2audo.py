# import os
# from uuid import uuid4
# from aip import AipSpeech
# from aip import AipNlp
#
# # import settings
#
# """ 你的 APPID AK SK """
# APP_ID = '11617876'
# API_KEY = 'KqqpO9GclBimrcSNrSANPhUQ'
# SECRET_KEY = 'xc7IFW4w6DVtuNQlMkBX05Ulhx5Mm5zh'
#
# client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
# nlp_client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
#
# # 音频转为文本
# def audio2text(file_name):
#     file_path = os.path.join(settings.AUDIO_PCM_DIR, file_name)
#     cmd_str = f'ffmpeg -y -i {file_path} -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {file_path}.pcm'
#     os.system(cmd_str)
#     with open(f'{file_path}.pcm', 'rb') as f:
#         audio_context = f.read()
#     res = client.asr(audio_context, 'pcm', 16000, {
#         "dev_pid": 1537
#     })
#     print("res",res)
#     if res.get('err_no'):
#         return res
#     return res.get('result')[0]
#
# # 文本转为音频
# def text2audio(text):
#     file_name = f"{uuid4()}.mp3"
#     file_path = os.path.join(settings.AUDIO_DIR, file_name)
#     res = client.synthesis(text, 'zh', 1, {
#         "vol": 5,
#         'pit': 7,
#         "spd": 4,
#         "per": 4
#     })
#     if isinstance(res, dict):
#         return res
#     with open(file_path, 'wb') as f:
#         f.write(res)
#     return file_name
#
# # 词法的匹配分析
# def my_nlp(text):
#     print("text", nlp_client.simnet('你今年几岁了', text))
#     if nlp_client.simnet('你今年几岁了', text).get('score') >= 0.72:
#         return '我今年73了，不然84也行'
#     elif nlp_client.simnet('你叫什么名字', text).get('score') >= 0.72:
#         return '我的名字'
#     elif nlp_client.simnet('你在哪儿学习',text).get('score') >= 0.72:
#         return '我在老男孩教育'
#     else:
#         return '不知道你在说什么'
