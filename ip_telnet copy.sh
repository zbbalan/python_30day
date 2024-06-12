#!/bin/bash
echo "请输入目标物理机主机的IP地址:"
read WL_REMOTE_HOST_IP

echo "请输入目标虚拟机主机的IP地址:"
read XN_REMOTE_HOST_IP


# 定义目标主机的IP地址
#WL_REMOTE_HOST_IP="192.168.1.100"
HOSTNAME=$(hostname -I | awk -F ' ' '{print $1}')
mkdir $HOSTNAME-$WL_REMOTE_HOST_IP
mkdir $HOSTNAME-$XN_REMOTE_HOST_IP
# 定义输出文件前缀
OUTPUT_FILE_PREFIX="$HOSTNAME-$WL_REMOTE_HOST_IP-$(date +%Y%m%d)_"
OUTPUT_FILE_PREFIX="$HOSTNAME-$XN_REMOTE_HOST_IP-$(date +%Y%m%d)_"
# 检查是否已存在守护进程，避免重复启动
if [ -f "/tmp/${OUTPUT_FILE_PREFIX}pid" ]; then
    echo "守护进程已在运行，请勿重复启动。"
    exit 1
fi

# 将PID写入文件，用于标识守护进程
echo $$ > "/tmp/${OUTPUT_FILE_PREFIX}pid"

# 定义执行测试的函数
monitor_with_ping() {
    local timestamp=$(date +%Y%m%d_%H%M%S)
    local output_file="${OUTPUT_FILE_PREFIX}${timestamp}.txt"
    
    # 使用ping进行测试，这里使用-c 100进行100次测试
    ping_stats=$(ping -c 100 $WL_REMOTE_HOST_IP)

    # 提取丢包率
    packet_loss=$(echo "$ping_stats" | grep -oP '\d+(?=% packet loss)')
    avg_latency=$(echo "$ping_stats" | grep -oP avg | awk -F '[= ]+' '{print $3}' | awk -F '/' '{print $2}')
    max_latency=$(echo "$ping_stats" | grep -oP max | awk -F '[= ]+' '{print $3}' | awk -F '/' '{print $3}')
    if [[ $packet_loss -gt 0 ]]; then
        # 存在丢包，输出详细信息
        echo "时间: $timestamp" >> "$output_file"
        echo "丢包率: $packet_loss%" >> "$output_file"
        echo "平均延迟: $avg_latency ms" >> "$output_file"
        echo "最大延迟: $max_latency ms" >> "$output_file"
        echo "$ping_stats" >> "$output_file"
    elif [[ ! -z "$packet_loss" ]]; then
        # 没有丢包，仅输出时间戳
        echo "$timestamp: 无丢包" >> "$output_file"
    fi
    echo "测试结果已保存至: $output_file"
}

# 初始化日志文件
echo "网络监控（使用ping）开始于: $(date)" > "${OUTPUT_FILE_PREFIX}summary.txt"

# 作为守护进程每分钟执行一次测试
while true; do
    monitor_with_ping
    sleep 120
done

# 清理操作，当脚本正常退出时执行（但作为守护进程这行代码实际上不会执行到）
kill -9 $(cat "/tmp/${OUTPUT_FILE_PREFIX}pid")
