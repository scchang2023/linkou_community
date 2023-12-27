import psutil
import datetime
 
cpu_count=psutil.cpu_count(logical=False)
cpu_util=psutil.cpu_percent(1)
print("CPU核心數:",cpu_count)
print("CPU使用率:",cpu_util,"%")

free=round(psutil.virtual_memory().free/(1024.0*1024.0*1024.0),2)
total=round(psutil.virtual_memory().total/(1024.0*1024.0*1024.0),2)
memory_usage=(total-free)/total
print("記憶體大小:",total)
print("剩餘記憶體:",free)
print("記憶體使用率:",int(memory_usage*100),"%")

uptime=psutil.boot_time()
print("系統開機時間:",datetime.datetime.fromtimestamp(uptime).strftime("%Y-%m-%d %H:%M:%S"))

users=psutil.users()
print("目前有%d位使用者"%len(users))
for user in users:
    print("\t使用者帳號為:",user.name)

net=psutil.net_io_counters()
bytes_recv=net.bytes_recv/1024/1024
bytes_sent=net.bytes_sent/1024/1024
print("網卡接收流量 %.2f Mb,網卡發送流量 %.2f Mb" % (bytes_recv,bytes_sent))

disks=psutil.disk_partitions()
for disk in disks:
    if disk.fstype!="":
        usage=psutil.disk_usage(disk.device)
        print("磁碟:",disk.mountpoint)
        print ("\t總容量："+str(int(usage.total/(1024.0*1024.0*1024.0)))+"G")
        print ("\t已用容量："+str(int(usage.used/(1024.0*1024.0*1024.0)))+"G")
        print ("\t可用容量："+str(int(usage.free/(1024.0*1024.0*1024.0)))+"G")

for pid in psutil.pids():
    p=psutil.Process(pid)
    print("名稱 %-10s  記憶體使用率 %-6s 狀態 %-10s"%(p.name(),p.memory_percent(),p.status()))