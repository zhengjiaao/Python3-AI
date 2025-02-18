from http import HTTPStatus
from urllib.parse import urlparse, unquote
from pathlib import PurePosixPath
import requests
from dashscope import ImageSynthesis

prompt = "一只狗戴着红色眼镜"
model = "wanx-x-painting"
task = "image2image"
extra_input = {
    "base_image_url": "http://synthesis-source.oss-accelerate.aliyuncs.com/lingji/validation/mask2img/demo/source3.jpg",
    "mask_image_url": "http://synthesis-source.oss-accelerate.aliyuncs.com/lingji/validation/mask2img/demo/glasses.png"
}


def call():
    print('----sync call, please wait a moment----')
    rsp = ImageSynthesis.call(model=model,
                              prompt=prompt,
                              n=1,
                              size='1024*1024',
                              task=task,
                              extra_input=extra_input)
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


if __name__ == '__main__':
    call()
