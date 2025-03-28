#导入telnetlin库
import telnetlib

def telnet_ports(path):
    #打开llb_ports并赋值为file
    with open(path, 'r') as file:
        #遍历file文件中的每一行
        for line in file:
            #去除行尾的换行符，并以,为分隔符将行分割城host，port
            host, port = line.strip().split(',')
            #将端口装换位
            # 整数类型
            port = int(port)
            #调用test_telnet函数来测试状态，如果test_telnet函数返回True，表示端口是开放的。
            if test_telnet(host, port):
                print(f"端口 {port} 在 {host} 上是开放的")
            #如果test_telnet函数返回False，表示端口是关闭的。
            else:
                print(f"端口 {port} 在 {host} 上是关闭的")

def test_telnet(host, port, timeout=1):
    try:
        # 创建一个telnet对象，尝试连接到指定的主机和端口，超时时间设置为1秒。
        connection = telnetlib.Telnet(host, port, timeout)
        # 尝试读取一些数据，确认连接成功
        connection.close()
        return True
    #如果尝试连接时出现任何异常，捕获该异常。
    except Exception as e:
        return False

if __name__ == '__main__':
    try:
        # 调用telnet_ports函数并传入文件路径,建议提供绝对路径
        path = '此处填写文件路径'
        telnet_ports(path)
        print(f"尝试打开文件：{path}")
    except Exception as e:
        print(f"发生错误：{str(e)}")
