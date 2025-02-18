from http import HTTPStatus
from urllib.parse import urlparse, unquote
from pathlib import PurePosixPath
import requests
from dashscope import ImageSynthesis
import os

prompt = "一棵参天大树"
sketch_image_url = "https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6609471071/p743851.jpg"
model = "wanx-sketch-to-image-lite"
task = "image2image"


print('----sync call, please wait a moment----')
rsp = ImageSynthesis.call(api_key=os.getenv("DASHSCOPE_API_KEY"),
                          model=model,
                          prompt=prompt,
                          n=1,
                          style='<watercolor>',
                          size='768*768',
                          sketch_image_url=sketch_image_url,
                          task=task)
print('response: %s' % rsp)
if rsp.status_code == HTTPStatus.OK:
    print(rsp.output)
    # save file to current directory
    for result in rsp.output.results:
        file_name = PurePosixPath(unquote(urlparse(result.url).path)).parts[-1]
        with open('./%s' % file_name, 'wb+') as f:
            f.write(requests.get(result.url).content)
else:
    print('sync_call Failed, status_code: %s, code: %s, message: %s' %
          (rsp.status_code, rsp.code, rsp.message))