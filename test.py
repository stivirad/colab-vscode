# CPU e RAM
import psutil
import platform

print("Sistema operativo:", platform.system())
print("CPU:", platform.processor())
print("Core CPU:", psutil.cpu_count(logical=True))
print("RAM totale (GB):", round(psutil.virtual_memory().total / 1e9, 2))

# GPU NVIDIA
!nvidia-smi
