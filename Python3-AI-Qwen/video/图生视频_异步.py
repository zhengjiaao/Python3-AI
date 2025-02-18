from http import HTTPStatus
# dashscope sdk >= 1.22.1
from dashscope import VideoSynthesis


def sample_async_call_i2v():
    # call async api, will return the task information
    # you can get task status with the returned task id.
    rsp = VideoSynthesis.async_call(model='wanx2.1-i2v-plus',
                                    prompt='一只猫在草地上奔跑',
                                    img_url='https://cdn.translate.alibaba.com/r/wanx-demo-1.png')
    print(rsp)
    if rsp.status_code == HTTPStatus.OK:
        print("task_id: %s" % rsp.output.task_id)
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (rsp.status_code, rsp.code, rsp.message))

    # get the task information include the task status.
    status = VideoSynthesis.fetch(rsp)
    if status.status_code == HTTPStatus.OK:
        print(status.output.task_status)  # check the task status
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (status.status_code, status.code, status.message))

    # wait the task complete, will call fetch interval, and check it's in finished status.
    rsp = VideoSynthesis.wait(rsp)
    print(rsp)
    if rsp.status_code == HTTPStatus.OK:
        print(rsp.output.video_url)
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (rsp.status_code, rsp.code, rsp.message))


if __name__ == '__main__':
    sample_async_call_i2v()
