import time
from pywifi import const
import pywifi

# 获取网卡
def get_card():
    wifi = pywifi.PyWiFi()
    card = wifi.interfaces()[0]
    card.disconnect()
    time.sleep(1)
    status = card.status()
    if status not in [const.IFACE_DISCONNECTED, const.IFACE_CONNECTED]:
        print("网卡未处于断开状态")
        return False
    return card
# 扫描WiFi列表
def scan_wifi(card):
    print("开始扫描附近的WiFi...")
    card.scan()
    time.sleep(15)
    wifi_list = card.scan_results()
    print("数量：",len(wifi_list))
    index = 1
    for wifi_info in wifi_list:
        print(f"{index}.SSID: {wifi_info.ssid}")
        index = index + 1
    return wifi_list
if __name__ == '__main__':
    card = get_card()
    scan_wifi(card)