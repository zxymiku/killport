import psutil
def close_app_using_port(port):
    for proc in psutil.process_iter(['pid', 'name', 'connections']):
        for conn in proc.info.get('connections', []):
            if conn.get('laddr') and conn['laddr'][1] == port:
                print(f"Found process {proc.info['pid']} ({proc.info['name']}) using port {port}.")
                print("Terminating the process...")
                try:
                    proc.terminate()
                except psutil.NoSuchProcess:
                    pass
                break

if __name__ == "__main__":
    port_to_close = input("输入要关闭的端口号")#输入要关闭的端口号
    close_app_using_port(port_to_close)
    print("Done.")