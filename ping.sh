#!/bin/bash
HOSTNAME=$(hostname -I | awk -F ' ' '{print }')
# 输出脚本开始信息
echo "脚本开始执行: $(date)"

# 处理命令行选项
if [[ $# -eq 0 ]]; then
    echo "请指定操作：start 或 stop"
    exit 1
fi

start_stop=$1

# 输出命令行选项
echo "接收到的选项: $start_stop"

# 用户输入start时执行
if [ "$start_stop" = "start" ]; then
  # 请求用户输入目标主机的IP地址
  echo "请输入目标物理机主机的IP地址:"
  read WL_REMOTE_HOST_IP
  echo "请输入目标虚拟机主机的IP地址:"
  read XN_REMOTE_HOST_IP
  echo "请输入网关IP地址:"
  read WG_REMOTE_HOST_IP

  # 定义输出文件前缀
  WL_OUTPUT_FILE_PREFIX="$HOSTNAME-$WL_REMOTE_HOST_IP-$(date +%Y%m%d)_"
  XN_OUTPUT_FILE_PREFIX="$HOSTNAME-$XN_REMOTE_HOST_IP-$(date +%Y%m%d)_"
  WG_OUTPUT_FILE_PREFIX="$HOSTNAME-$WG_REMOTE_HOST_IP-$(date +%Y%m%d)_"

  # 创建对应的目录
  mkdir -p "$HOSTNAME-$WL_REMOTE_HOST_IP"
  mkdir -p "$HOSTNAME-$XN_REMOTE_HOST_IP"
  mkdir -p "$HOSTNAME-$WG_REMOTE_HOST_IP"

  # 输出输出文件前缀
  echo "WL输出文件前缀: ${WL_OUTPUT_FILE_PREFIX}"
  echo "XN输出文件前缀: ${XN_OUTPUT_FILE_PREFIX}"
  echo "WG输出文件前缀: ${WG_OUTPUT_FILE_PREFIX}"

  # 检查是否已存在守护进程，避免重复启动
  #if [ -f "/tmp/${WL_OUTPUT_FILE_PREFIX}pid" ]; then
  #    echo "守护进程已在运行，请勿重复启动。"
  #    exit 1
  #fi

  # 将PID写入文件，用于标识守护进程
  echo $$ > "/tmp/${WL_OUTPUT_FILE_PREFIX}pid"

  # ...（其余代码不变）
 # 定义执行测试的函数
  monitor_with_ping() {
     # local hostname=$1
      local ip=$1
      local output_file_prefix="$2"
      local timestamp=$(date +%Y%m%d_%H%M%S)
      local output_file="${output_file_prefix}${timestamp}.txt"
      
      # 使用ping进行测试，这里使用-c 100进行100次测试
      ping_stats=$(ping -c 100 $ip)

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
  echo "网络监控（使用ping）开始于: $(date)" > "${WL_OUTPUT_FILE_PREFIX}summary.txt"

  # 作为守护进程每分钟执行一次测试
  (
    monitor_with_ping  "$WL_REMOTE_HOST_IP" "${WL_OUTPUT_FILE_PREFIX}"
    monitor_with_ping  "$XN_REMOTE_HOST_IP" "${XN_OUTPUT_FILE_PREFIX}"
    monitor_with_ping  "$WG_REMOTE_HOST_IP" "${WG_OUTPUT_FILE_PREFIX}"
  ) &
  pid=$!
  while true; do
      sleep 120
      if ! kill -0 $pid 2>/dev/null; then
          echo "守护进程已退出。"
          break
      fi
  done

  # 清理操作，当脚本正常退出时执行（但作为守护进程这行代码实际上不会执行到）
  kill -9 $(cat "/tmp/${WL_OUTPUT_FILE_PREFIX}pid")

else
  # 用户输入stop时，停止守护进程
  if [ -f "/tmp/${WL_OUTPUT_FILE_PREFIX}pid" ]; then
      kill -9 $(cat "/tmp/${WL_OUTPUT_FILE_PREFIX}pid")
     # rm -f "/tmp/${WL_OUTPUT_FILE_PREFIX}pid"
      echo "守护进程已停止。"
  else
      echo "守护进程未运行。"
  fi
fi

# 输出脚本结束信息
echo "脚本结束执行: $(date)"