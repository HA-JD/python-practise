import requests

# 打开包含代理的文本文件
with open('IP代理池.txt', 'r') as fo:
    proxy_lines = fo.readlines()

# 初始化一个列表来存储正常工作的代理
working_proxies = []

# 遍历每行代理信息
for proxy_line in proxy_lines:
    # 将文本行解析为字典
    proxy_dict = eval(proxy_line)

    # 设置请求头（如果需要的话）
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71',
    }

    # 要访问的目标URL
    target_url = 'https://example.com'

    # 测试代理
    try:
        response = requests.get(target_url, headers=headers, proxies=proxy_dict, timeout=5)
        if response.status_code == 200:
            print(f"代理 {proxy_dict['HTTP']} 正常.")
            # 如果代理正常工作，将其添加到工作代理列表中
            working_proxies.append(proxy_line)
    except Exception as e:
        print(f"代理 {proxy_dict['HTTP']} 连接错误: {str(e)}")

# 将正常工作的代理保存到另一个文本文件
with open('有效IP代理池.txt', 'w') as fo:
    fo.writelines(working_proxies)

print(f"共有 {len(working_proxies)} 个有效代理已保存到有效IP代理池.txt 文件中。")
