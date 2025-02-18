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


def async_call():
    print('----create task----')
    task_info = create_async_task()
    print('----wait task done then save image----')
    wait_async_task(task_info)


# 创建异步任务
def create_async_task():
    rsp = ImageSynthesis.async_call(model=model,
                                    prompt=prompt,
                                    n=1,
                                    size='1024*1024',
                                    task=task,
                                    extra_input=extra_input)
    print(rsp)
    if rsp.status_code == HTTPStatus.OK:
        print(rsp.output)
    else:
        print('create_async_task Failed, status_code: %s, code: %s, message: %s' %
              (rsp.status_code, rsp.code, rsp.message))
    return rsp


# 等待异步任务结束
def wait_async_task(task):
    rsp = ImageSynthesis.wait(task)
    print(rsp)
    if rsp.status_code == HTTPStatus.OK:
        print(rsp.output.task_status)
        # save file to current directory
        for result in rsp.output.results:
            file_name = PurePosixPath(unquote(urlparse(result.url).path)).parts[-1]
            with open('./%s' % file_name, 'wb+') as f:
                f.write(requests.get(result.url).content)
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (rsp.status_code, rsp.code, rsp.message))


if __name__ == '__main__':
    async_call()
