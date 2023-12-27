import wmi

w=wmi.WMI()

cpus=w.Win32_Processor()
for cpu in cpus:
#    print(cpu)
    print("CPU核心數:",cpu.NumberOfCores)
    print("CPU型號:",cpu.Name)
    
computer=w.Win32_ComputerSystem()[0]
#print(computer)
print("機器型號:",computer.model)
print("制造商:",computer.Manufacturer)

OS=w.Win32_OperatingSystem()[0]
#print(OS)
print("作業系統:",OS.Name)
print("序號:",OS.SerialNumber)

disks=w.Win32_DiskDrive()
for disk in disks:
    if disk.size is not None:
#        print(disk)
        print("硬碟製造商:",disk.Manufacturer)
        print("硬碟型號:",disk.Model)
        print("硬碟序號:",disk.SerialNumber)
        print("硬碟大小:",int(disk.Size)/(1024*1024*1024))

memorys=w.Win32_PhysicalMemory()
for memory in memorys:
#    print(memory)
    print("記憶體製造商:",memory.Manufacturer)
    print("記憶體大小:",int(memory.Capacity)/(1024*1024*1024))    

nics=w.Win32_NetworkAdapterConfiguration()
for nic in nics:
    if nic.MACAddress is not None and nic.IPAddress is not None:
#        print(nic)
        print(nic.Caption)
        print(nic.MACAddress)
        print(nic.IPAddress[0])
        print(nic.IPSubnet[0])
        