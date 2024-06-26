source_file = "demo.txt"
final_file = "result.txt"
zb_urls_limit = 10
response_time_weight = 0.5
resolution_weight = 0.5
open_sort = True
# 1: 显示默认值，线路1 线路2，2：显示视频分辨率，如:1080x720
xianlu_type = 1
# ffmpeg解析视频时间，单位秒
ffmpeg_time = 10
# key: 地区，在http://tonkiang.us网站上搜索的关键词
# value: 订阅url，在https://github.com/xisohi/IPTV-Multicast-source中找自己想要的
search_dict = {
    "安徽": "https://chinaiptv.pages.dev/anhui/anhui.txt",
    "重庆": "https://chinaiptv.pages.dev/chongqing/chongqing.txt",
    "四川": "https://chinaiptv.pages.dev/sichuan/sichuan.txt",
    "北京": "https://chinaiptv.pages.dev/beijing/beijing.txt",
    "江苏": "https://chinaiptv.pages.dev/jiangsu/jiangsu.txt",
    "天津": "https://chinaiptv.pages.dev/tianjin/tianjin.txt",
    "湖北": "https://chinaiptv.pages.dev/hubei/hubei.txt",
    "江西": "https://chinaiptv.pages.dev/jiangxi/jiangxi.txt",
    "湖南": "https://chinaiptv.pages.dev/hunan/hunan.txt",
    "贵州": "https://chinaiptv.pages.dev/guizhou/guizhou.txt",
    "福建": "https://chinaiptv.pages.dev/fujian/fujian.txt",
    "广东": "https://chinaiptv.pages.dev/guangdong/guangdong.txt",
    "河南": "https://chinaiptv.pages.dev/henan/henan.txt",
    "内蒙古": "https://chinaiptv.pages.dev/neimenggu/neimenggu.txt",
    "云南": "https://chinaiptv.pages.dev/yunnan/yunnan.txt",
}
# 在http://tonkiang.us网站上搜索的源的页数
search_page_num = 5
# 忽略的关键词，比如在demo.txt中配置广东珠江,但在订阅中只有广东珠江高清,就需要忽略掉"高清"
search_ignore_key = ["高清", "4K"]
# crawl_type的默认值为1-只爬取http://tonkiang.us上组播源；2-只爬取crawl_urls中配置的网站；3-全部
crawl_type = "1"
# 收集其他大佬url中的直播源
crawl_urls = [
    "https://mirror.ghproxy.com/raw.githubusercontent.com/plplpopp/iptv/main/result.txt"
]
# ipv6源检测有效性的代理地址，用于不支持ipv6网络的主机，若网络支持ipv6，这里填空""
ipv6_proxy = "http://www.ipv6proxy.net/go.php?u=" #此代理用于github，国内不一定能用
# ftp上传result.txt文件
ftp_host = ""
ftp_port = ""
ftp_user = ""
ftp_pass = ""
ftp_remote_file = ""

# 凯速网上传文件配置
ks_token = ""
ks_file_id = "0"  # 文件目录id，0为根目录
ks_file_name = ""
