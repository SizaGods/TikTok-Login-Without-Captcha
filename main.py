import requests
import threading
import random
import time,secrets,binascii,os,uuid
from urllib.parse import urlencode
from MedoSigner import Argus,Gorgon, md5,Ladon


def xor(string: str) -> str:
    return "".join([hex(ord(_) ^ 5)[2:] for _ in string]) 
    





def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 567753, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int =2, platform: int = 19, unix: int = None):
        x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload != None else None
        data=payload
        if not unix: unix = int(time.time())
        return Gorgon(params, unix, payload, cookie).get_value() | { "x-ladon"   : Ladon.encrypt(unix, license_id, aid),"x-argus"   : Argus.get_sign(params, x_ss_stub, unix,platform        = platform,aid             = aid,license_id      = license_id,sec_device_id   = sec_device_id,sdk_version     = sdk_version_str, sdk_version_int = sdk_version)}
data = {
  'password': xor(input("Enter Your Password : ")),
  'account_sdk_source': "app",
  'multi_login': "1",
  'mix_mode': "1",
  'username': xor(input("Enter Your Username : "))
}

cookies = {
    'odin_tt': '96136c5fc2afb325d059d66883b7d9e598feccaf1e06578da0a5db29f052a545b50dac7a55ddf2b83ffdc5fb6034c8428beca6ba52bac991c4586270e8de66706f3fbb861a3f3a97e4a2810255b91b45',
    'passport_csrf_token': '7f94b773e73e646ac9902804ead86469',
    'passport_csrf_token_default': '7f94b773e73e646ac9902804ead86469',
}
m=sign(params='passport-sdk-version=19&iid=7444795544621369143&device_id=7444794513535862327&ac=mobile&channel=googleplay&aid=567753&app_name=tiktok_studio&version_code=320905&version_name=32.9.5&device_platform=android&os=android&ab_version=32.9.5&ssmix=a&device_type=Redmi%20Note%208%20Pro&device_brand=Redmi&language=ar&os_api=30&os_version=11&openudid=0f081bbd6466a90a&manifest_version_code=320905&resolution=1080*2220&dpi=440&update_version_code=320905&_rticket=1733376612058&is_pad=0&app_type=normal&sys_region=EG&mcc_mnc=42103&timezone_name=Asia/Aden&app_language=ar&carrier_region=YE&ac2=lte&uoo=1&op_region=YE&timezone_offset=10800&build_number=32.9.5&host_abi=arm64-v8a&locale=ar&region=EG&ts=1733376611&cdid=9bd05fba-315b-4ff7-a1f6-097166023125&support_webview=1&device_redirect_info=e9vryhH5ZXYycA9Ndu4Qlvl8-CaCSX6MhOGbkQ2jgtuLTEhnfHG1kF1lR1liwC_Lvf75z1BP-Yl__f9XG1V9VM2o4mWpu-6xRKz9x102gz3bW5MQ_lBiOX2xDs90e1d3PJI8FFKYtVjrE8TDEsZFGpcjm5-GUrjKY00z1kPVmJ8&cronet_version=5828ea06_2024-03-28&ttnet_version=4.2.137.58-tiktok&use_store_region_cookie=1',payload=urlencode(data),cookie=urlencode(cookies))
headers = {
'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': "com.ss.android.tt.creator/370301 (Linux; U; Android 11; ar; Redmi Note 8 Pro; Build/RP1A.200720.011; Cronet/TTNetVersion:f6248591 2024-09-11 QuicVersion:182d68c8 2024-05-28)",'x-argus': m["x-argus"],
          'x-gorgon': m["x-gorgon"],
          'x-khronos': m["x-khronos"],
          'x-ladon': m["x-ladon"],}
          
response = requests.post(
    'https://api16-normal-c-alisg.tiktokv.com/passport/user/login/?passport-sdk-version=19&iid=7444795544621369143&device_id=7444794513535862327&ac=mobile&channel=googleplay&aid=1164&app_name=tiktok_studio&version_code=320905&version_name=32.9.5&device_platform=android&os=android&ab_version=32.9.5&ssmix=a&device_type=Redmi%20Note%208%20Pro&device_brand=Redmi&language=ar&os_api=30&os_version=11&openudid=0f081bbd6466a90a&manifest_version_code=320905&resolution=1080*2220&dpi=440&update_version_code=320905&_rticket=1733376612058&is_pad=0&app_type=normal&sys_region=EG&mcc_mnc=42103&timezone_name=Asia/Aden&app_language=ar&carrier_region=YE&ac2=lte&uoo=1&op_region=YE&timezone_offset=10800&build_number=32.9.5&host_abi=arm64-v8a&locale=ar&region=EG&ts=1733376611&cdid=9bd05fba-315b-4ff7-a1f6-097166023125&support_webview=1&device_redirect_info=e9vryhH5ZXYycA9Ndu4Qlvl8-CaCSX6MhOGbkQ2jgtuLTEhnfHG1kF1lR1liwC_Lvf75z1BP-Yl__f9XG1V9VM2o4mWpu-6xRKz9x102gz3bW5MQ_lBiOX2xDs90e1d3PJI8FFKYtVjrE8TDEsZFGpcjm5-GUrjKY00z1kPVmJ8&cronet_version=5828ea06_2024-03-28&ttnet_version=4.2.137.58-tiktok&use_store_region_cookie=1',
    cookies=cookies,
    headers=headers,
    data=data,
)
print(response.text)
