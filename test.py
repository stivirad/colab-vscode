import platform
import psutil
import os

def system_info():
    info = {
        "OS": platform.system(),
        "OS_version": platform.version(),
        "CPU_cores": psutil.cpu_count(logical=True),
        "RAM_GB": round(psutil.virtual_memory().total / 1e9, 2),
        "RUN_ENV": "COLAB" if os.path.exists("/content") else "LOCAL"
    }
    return info

if __name__ == "__main__":
    info = system_info()
    for k, v in info.items():
        print(f"{k}: {v}")

    # output SOLO locale / colab, NON Git
    with open("output_test.txt", "w") as f:
        for k, v in info.items():
            f.write(f"{k}: {v}\n")

    print("Output scritto in output_test.txt")
