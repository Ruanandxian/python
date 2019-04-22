import psutil
print(psutil.cpu_count())#cpu逻辑数量
print(psutil.cpu_count(logical=False))#cpu物理核心
print(psutil.cpu_times())#cpu的用户/系统/空闲时间

#cpu使用率，每秒刷新一次
for x in range(10):
	print(psutil.cpu_percent(interval=1,percpu=True))

#获取物理内存和内存交换信息
print(psutil.virtual_memory())
print(psutil.swap_memory())

#磁盘操作
print(psutil.disk_partitions())#磁盘分区
print(psutil.disk_usage('/'))#磁盘使用情况
print(psutil.disk_io_counters())#磁盘IO


#网路操作
print(psutil.net_io_counters())#获取网络读写字节/包的个数
print(psutil.net_if_addrs())#获取网络接口信息
print(psutil.net_connections())#获取现在的网络连接信息


#进程操作
print(psutil.pids())#所有的进程
p=psutil.Process(4872)#获取指定的进程ID=4872
print(p.name())#进程名字 pycharm64.exe
print(p.exe())#进程路径  D:\pycharm\PyCharm 2018.1.4\bin\pycharm64.exe'
print(p.cwd())#C:\Users\Administrator\Desktop
print(p.cmdline())#进程启动的命令行 ['D:\\pycharm\\PyCharm 2018.1.4\\bin\\pycharm64.exe']
print(p.ppid())#父进程ID   2424
print(p.parent())#父进程   psutil.Process(pid=2424, name='explorer.exe', started='22:49:38')
print(p.children())#子进程列表  [psutil.Process(pid=4636, name='fsnotifier64.exe', started='22:52:17'), psutil.Process(pid=4976, name='python.exe', started='00:48:46'), psutil.Process(pid=3264, name='python.exe', started='00:49:31')]
print(p.status())#进程状态   running
print(p.username())#进程用户名   PC-20170616VSWH\Administrator
print(p.create_time())#进程创建时间   1532011918.0
print(p.terminal())#进程终端
print(p.cpu_times())#进程使用的cpu时间
print(p.memory_info())#进程使用的内存
print(p.open_files())#进程打开的文件
print(p.connections())#进程相关的网络连接
print(p.threads())#所有的进程信息
print(p.environ())#进程的环境变量
#print(p.terminate())#进程自己结束


print(psutil.test())#模拟ps命令的效果
#USER         PID %MEM     VSZ     RSS TTY           START    TIME  COMMAND
#SYSTEM         0    ?       ?      24 ?             Jul19   36:25  System Idle Process
#SYSTEM         4    ?     112     368 ?             Jul19   00:45  System
#             360    ?     540    1172 ?             Jul19   00:00  smss.exe
#             536  0.2   16964   20768 ?             Jul19   00:01  svchost.exe
#             560  0.5   23088   38840 ?             Jul19   00:07  svchost.exe
#             580  2.2  190000  182748 ?             Jul19   00:32  svchost.exe
#             584  0.1    2460    5356 ?             Jul19   00:00  csrss.exe
#             656  0.1    1780    5388 ?             Jul19   00:00  wininit.exe
#             680  0.4    3060   31072 ?             Jul19   00:12  csrss.exe
#             684  0.3   11356   22296 ?             Jul19   00:05  svchost.exe
#             724  0.1    5936   10508 ?             Jul19   00:01  services.exe
#             740  0.1    4748   12256 ?             Jul19   00:03  lsass.exe
#             748  0.1    2556    4316 ?             Jul19   00:00  lsm.exe
#             808  0.1    3448    8380 ?             Jul19   00:00  winlogon.exe
#             904  0.1    5012   10104 ?             Jul19   00:06  svchost.exe
#             980  0.1    4720    9304 ?             Jul19   00:00  svchost.exe
#            1120  0.2    8640   16124 ?             Jul19   00:00  svchost.exe
#            1168  0.1    2612    7644 ?             Jul19   00:00  igfxCUIService.exe
#            1200  0.1    1640    4840 ?             Jul19   00:00  hpservice.exe
#            1228    ?    1176    3840 ?             Jul19   00:00  pcmastersvc.exe
#            1312  0.1    6476    6332 ?             Jul19   00:00  RtkAudioService64.exe
#            1372  0.2   15428   13000 ?             Jul19   00:00  RAVBg64.exe
#            1396  0.1    2252    6696 ?             Jul19   00:00  btwdins.exe
#            1408  0.3   13224   23344 ?             Jul19   00:01  ZhuDongFangYu.exe
#            1464  0.2   12140   16176 ?             Jul19   00:01  svchost.exe
#            1640  0.1    2060    5376 ?             Jul19   00:00  wlanext.exe
#            1648  0.2   14212   20272 ?             Jul19   00:00  AuthenMngService.exe
#            1656    ?    1188    3232 ?             Jul19   00:00  conhost.exe
#Administra  1740  0.7   50420   60052 ?             00:45   00:01  python.exe
#            1916  0.1    4368    7636 ?             Jul19   00:00  iNodeMon.exe
#            1980  0.2    7184   13820 ?             Jul19   00:00  spoolsv.exe
#            2008  0.2   14284   20128 ?             Jul19   00:01  svchost.exe
#            2080  0.2   10176   13832 ?             Jul19   00:00  IpOverUsbSvc.exe
#            2268  0.2   17216   17208 ?             Jul19   00:00  QQProtect.exe
#Administra  2312    ?    2932    2660 ?             Jul19   00:00  AccelerometerSt.exe
#            2324  0.1    2076    5872 ?             Jul19   00:00  svchost.exe
#            2348  0.1    1852    4972 ?             Jul19   00:00  SynTPEnhService.exe
#Administra  2416  0.2   10692   17808 ?             Jul19   00:00  SynTPEnh.exe
#Administra  2424  0.9   51240   78180 ?             Jul19   00:11  explorer.exe
#            2484  0.1    3660    7880 ?             Jul19   00:00  vmware-usbarbitrator64.exe
#Administra  2572  0.3   31460   27124 ?             Jul19   00:21  dwm.exe
#            2636  0.1    7516   10592 ?             Jul19   00:00  vmnetdhcp.exe
#            2664  0.1    2000    6040 ?             Jul19   00:00  vmnat.exe
#            2720  0.1    7628   11668 ?             Jul19   00:00  vmware-authd.exe
#Administra  2764  0.7   50652   60196 ?             00:41   00:01  python.exe
#            2772  0.1    2296    4968 ?             00:42   00:00  svchost.exe
#Administra  2856  0.1    1944    4920 ?             Jul19   00:00  SynTPHelper.exe
#            3176  0.1    1712    5376 ?             Jul19   00:00  alg.exe
#            3228  0.2   26676   18612 ?             Jul19   00:00  PresentationFontCache.exe
#SYSTEM      3380  0.1    2672    6644 ?             00:47   00:00  SearchFilterHost.exe
#Administra  3508  0.1    2204    6628 ?             Jul19   00:00  rundll32.exe
#            3596  0.1    2860    7104 ?             Jul19   00:00  svchost.exe
#            3640  0.2    7016   14716 ?             Jul19   00:01  svchost.exe
#Administra  3700    ?    1704    4112 ?             00:46   00:00  conhost.exe
#Administra  3792    ?    1708    4104 ?             00:48   00:00  conhost.exe
#Administra  3832  0.1   13600   11084 ?             Jul19   00:00  RtkNGUI64.exe
#Administra  3844  0.1    2636    6572 ?             Jul19   00:00  ctfmon.exe
#Administra  3880  0.1    5532   12076 ?             Jul19   00:00  MSOSYNC.EXE
#Administra  4000  0.3    7608   27496 ?             Jul19   00:00  igfxHK.exe
#Administra  4016  0.7   51060   60280 ?             00:46   00:01  python.exe
#            4036  0.6   49692   47864 ?             Jul19   00:06  SearchIndexer.exe
#Administra  4060  0.1    4512   10880 ?             Jul19   00:00  igfxEM.exe
#Administra  4160    ?    1712    4116 ?             00:45   00:00  conhost.exe
#Administra  4244    ?    1712    4112 ?             00:41   00:00  conhost.exe
#            4424  0.1    3312    7592 ?             00:43   00:00  SearchProtocolHost.exe
#Administra  4544    ?    1712    4112 ?             00:43   00:00  conhost.exe
#Administra  4600    ?    1708    4096 ?             Jul19   00:00  conhost.exe
#Administra  4636    ?    2696    3884 ?             Jul19   00:00  fsnotifier64.exe
#Administra  4976  0.7   49472   58692 ?             00:48   00:01  python.exe
#Administra  5112  0.7   50744   60352 ?             00:43   00:01  python.exe)
