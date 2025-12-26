import platform
import psutil

with open("output_test.txt", "w") as f:
    f.write("=== INFO SISTEMA ===\n")
    f.write(f"Sistema operativo: {platform.system()}\n")
    f.write(f"CPU: {platform.processor()}\n")
    f.write(f"Core CPU: {psutil.cpu_count(logical=True)}\n")
    f.write(f"RAM totale (GB): {round(psutil.virtual_memory().total / 1e9, 2)}\n")
    f.write("\n=== TEST SCRIPT ===\n")
    f.write("Repo collegato correttamente\n")

print("Test completato. Output scritto in output_test.txt")
