# -*- coding: utf-8 -*-
import oss2
import time

AccessKeyId = '你的AccessKey'
AccessKeySecret = '你的AccessKey密码'
Endpoint = 'oss-cn-beijing.aliyuncs.com'
InternalEndpoint = 'oss-cn-beijing-internal.aliyuncs.com'


def upload_oss(bucket_name, file_name, bytes_content):
    """
    :param bucket_suffix: 区分测试环境和线上环境
    :param file_name: 会自动添加时间戳
    :param bytes_content: 二进制的文件内容
    :return: 外网可以访问的url
    """
    auth = oss2.Auth(AccessKeyId, AccessKeySecret)
    bucket = oss2.Bucket(auth, Endpoint, bucket_name)
    file_path = 'dynamic/' + str(int(time.time())) + '_' + file_name
    result = bucket.put_object(file_path, bytes_content)
    if result.status == 200:
        return 'http://' + bucket_name + '.oss-cn-beijing.aliyuncs.com/' + file_path
    else:
        return None
