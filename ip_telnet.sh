#!/bin/bash

# 定义目标主机的IP地址
REMOTE_HOST_IP="192.168.1.100"

# 定义输出文件前缀
OUTPUT_FILE_PREFIX="network_monitor_ping_$(date +%Y%m%d)_"

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
    
    # 使用ping进行测试，这里使用-c 10进行10次测试
    ping_stats=$(ping -c 10 $REMOTE_HOST_IP)

    # 提取丢包率
    packet_loss=$(echo "$ping_stats" | grep -oP '\d+(?=% packet loss)')

    if [[ $packet_loss -gt 0 ]]; then
        # 存在丢包，输出详细信息
        echo "时间: $timestamp" >> "$output_file"
        echo "丢包率: $packet_loss%" >> "$output_file"
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
    sleep 60
done

# 清理操作，当脚本正常退出时执行（但作为守护进程这行代码实际上不会执行到）
rm -f "/tmp/${OUTPUT_FILE_PREFIX}pid"