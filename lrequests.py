#encoding: utf-8
'''了解，requests
'''
import requests
import ujson
import inspect

FILENAME = "f143326b20647259d0e7551d322e5d03"

def requests_post(url, data):
    req = requests.post(url, data=ujson.dumps(data))
    print inspect.stack()[1][3], req.status_code

def send_upload_info():
    data = {
        "filename": FILENAME,
        "realname": "韩国语基础第14课(韩语发音语音学习)（流畅）.f4v.MP4",
        "md5": "71d6a41c7d38e2cd2deda2b66d9d42eb",
        "filesize": "63604284",
        "uploaded_bytes": 63604284,
        "path": "/mnt/vupload/25/%s.MP4" % FILENAME,
        "uid": "5746800",
        "start_time": 1447325080,
        "end_time": 1447325155,
        "user_ip": "183.131.11.57",
        "server_id": 14
    }

    requests_post('http://localhost/api/video/upload/info', data)

def send_encoding_start():
    data = {
        "file_path": "/mnt/vupload/47/%s.mp4" % FILENAME,
        "uploaded_bytes": 55333656,
        "file_size": "55333656",
        "part_prefix": "/mnt/vupload/47/%s" % FILENAME,
        "upload_prefix": "/47/%s" % FILENAME,
        "download_prefix": "http://172.17.2.24/vupload/47/%s" % FILENAME,
        "download_file": "http://172.17.2.24/vupload/47/%s.mp4" % FILENAME,
        "userid": "5746800",
        "filename": FILENAME,
        "hash": FILENAME,
        "start_time": 1447325139,
        "user_ip": "183.131.11.57",
        "real_name": "【Failed】05_传智播客Android视频教程_项目的目录结构与安装及启动过程分析.avi.mp4",
        "end_time": 1447325138,
        "md5": "fbe02cbe2d3f730a25a8853a8454745c",
        "server_id": 14
    }

    requests_post('http://localhost/api/video/encoding/start', data)

def send_encoding_done():
    data = {
        "file_path": "/mnt/vupload/8c/%s.flv" % FILENAME,
        "uploaded_bytes": 442353096,
        "file_size": "442353096",
        "part_prefix": "/mnt/vupload/8c/",
        "upload_prefix": "/8c/%s" % FILENAME,
        "download_prefix": "http://172.17.2.24/vupload/8c/%s" % FILENAME,
        "download_file": "http://172.17.2.24/vupload/8c/%s.flv" % FILENAME,
        "userid": "5746800",
        "filename": FILENAME,
        "hash": FILENAME,
        "start_time": 1447325068,
        "user_ip": "183.131.11.57",
        "real_name": "【Failed】20140214.湖南卫视HD.2014元宵喜乐会.华晨宇.开到荼靡.HDTV.1080i.H264-CL.ts.flv",
        "end_time": 1447325428,
        "md5": "f681c4f168e8ad37527f93db42444641",
        "server_id": 14
    }

    requests_post('http://localhost/api/video/encoding/done', data)

def send_encoding_callmain_done():
    data = {
        "seg_count": 'null',
        "filename": FILENAME,
        "flv": {
            "segments_info": {
                "1": {
                    "info": {
                        "duration": "446587",
                        "size": 109914369,
                        "name": "f143326b20647259d0e7551d322e5d03_joined_OD.flv",
                        "md5": "ebfb0c0571df4b2b5d1567931c43a09e"
                    },
                    "rc": {
                        "code": 0
                    }
                }
            },
            "encode_done_rc": {
                "code": 0
            },
            "rc": True
        },
        "hdmp4": {
            "segments_info": {
                "1": {
                    "info": {
                        "duration": "446581",
                        "size": 74619944,
                        "name": "f143326b20647259d0e7551d322e5d03_part000_HD_joined.mp4",
                        "md5": "95b77e9a2099883f651adb7bec71bf30"
                    },
                    "rc": {
                        "code": 0
                    }
                }
            },
            "encode_done_rc": {
                "code": 0
            },
            "rc": True
        },
        "mp4": {
            "segments_info": {
                "1": {
                    "info": {
                        "duration": "446581",
                        "size": 34307491,
                        "name": "f143326b20647259d0e7551d322e5d03_joined_SD.mp4",
                        "md5": "c96f3850fbcde8634760cc95e5df4faa"
                    },
                    "rc": {
                        "code": 0
                    }
                }
            },
            "encode_done_rc": {
                "code": 0
            },
            "rc": True
        },
        "rc": 0,
        "msg": "success",
        "total_success": True,
        "server_id": 14
    }

    requests_post('http://localhost/api/video/encoding/callmain/done', data)

def send_storage_start():
    datas = [
        {
            "cid": "5111722",
            "filename": "f143326b20647259d0e7551d322e5d03_joined_OD.flv",
            "format": "hdmp4",
            "log_id": "3333674",
            "vp": "14",
            "server_id": 14
        },
        {
            "cid": "5111722",
            "filename": "f143326b20647259d0e7551d322e5d03_part000_HD_joined.mp4",
            "format": "hdmp4",
            "log_id": "3333674",
            "vp": "14",
            "server_id": 14
        },
        {
            "cid": "5111722",
            "filename": "f143326b20647259d0e7551d322e5d03_joined_SD.mp4",
            "format": "hdmp4",
            "log_id": "3333674",
            "vp": "14",
            "server_id": 14
        }
    ]

    for data in datas:
        requests_post('http://localhost/api/video/storage/start', data)

def send_storage_done():
    datas = [
        {
            "rc": {
                "code": 0,
                "msg": "success"
            },
            "filename": "f143326b20647259d0e7551d322e5d03_joined_OD.flv",
            "src_file": "/mnt/vupload/ec/ece909bc5035d4a5c5307fcc085d7c89/f143326b20647259d0e7551d322e5d03_joined_OD.flv",
            "target_file": "/data/vg0/50/61/5111722-14-hd.mp4",
            "server_id": 14
        },
        {
            "rc": {
                "code": 0,
                "msg": "success"
            },
            "filename": "f143326b20647259d0e7551d322e5d03_part000_HD_joined.mp4",
            "src_file": "/mnt/vupload/ec/ece909bc5035d4a5c5307fcc085d7c89/f143326b20647259d0e7551d322e5d03_part000_HD_joined.mp4",
            "target_file": "/data/vg0/50/61/5111722-14-hd.mp4",
            "server_id": 14
        },
        {
            "rc": {
                "code": 0,
                "msg": "success"
            },
            "filename": "f143326b20647259d0e7551d322e5d03_joined_SD.mp4",
            "src_file": "/mnt/vupload/ec/ece909bc5035d4a5c5307fcc085d7c89/f143326b20647259d0e7551d322e5d03_joined_SD.mp4",
            "target_file": "/data/vg0/50/61/5111722-14-hd.mp4",
            "server_id": 14
        }
    ]

    for data in datas:
        requests_post('http://localhost/api/video/storage/done', data)

def send_storage_callmain_done():
    datas = [
        {
            "filename": "f143326b20647259d0e7551d322e5d03_joined_OD.flv",
            "params": {
                "log_id": "3333674",
                "server": 14,
                "format": "hdmp4",
                "vp": "14",
                "state": "DONE",
                "path": "/vg0/50/61/5111722-14-hd.mp4",
                "md5": 'null'
            },
            "cid": "5111722",
            "rc": {
                "code": -404,
                "message": "Document is not exists.",
                "ts": 1447325168
            },
            "server_id": 14
        },
        {
            "filename": "f143326b20647259d0e7551d322e5d03_part000_HD_joined.mp4",
            "params": {
                "log_id": "3333674",
                "server": 14,
                "format": "hdmp4",
                "vp": "14",
                "state": "DONE",
                "path": "/vg0/50/61/5111722-14-hd.mp4",
                "md5": 'null'
            },
            "cid": "5111722",
            "rc": {
                "code": -404,
                "message": "Document is not exists.",
                "ts": 1447325168
            },
            "server_id": 14
        },
        {
            "filename": "f143326b20647259d0e7551d322e5d03_joined_SD.mp4",
            "params": {
                "log_id": "3333674",
                "server": 14,
                "format": "hdmp4",
                "vp": "14",
                "state": "DONE",
                "path": "/vg0/50/61/5111722-14-hd.mp4",
                "md5": 'null'
            },
            "cid": "5111722",
            "rc": {
                "code": -404,
                "message": "Document is not exists.",
                "ts": 1447325168
            },
            "server_id": 14
        }
    ]

    for data in datas:
        requests_post('http://localhost/api/video/storage/callmain/done', data)


if __name__ == '__main__':
    send_upload_info()
    send_encoding_start()
    #send_encoding_done()
    #send_encoding_callmain_done()
    #send_storage_start()
    #send_storage_done()
    #send_storage_callmain_done()
