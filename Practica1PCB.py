import os
import sys

def MostrarPCB(Pid,Etiqueta);
    Campos = [
        "Name",
        "State",
        "Pid",
        "PPid",
        "VmSize"
        "VmRS"
        "Voluntary_ctxt_switches",
    ]

    print(f"Mostrando PCB de {Etiqueta}")

    for campo in Campos:
        with open(f"/proc/{Pid}/status") as F:
            for Linea in F:
                if Linea.startswith(campo):
                    print(f"{Linea}")

print("Practica 1 - Inspeccion de PCB de padre e hijo")

print(f"PADRE PID {os.getpid()}")
MostrarPCB(os.getpid(), "PROCESO PADRE")

Pid = os.fork()

print("Creando Proceso Hijo")
Pid = os.fork()
print(f"Estado {Pid}")

if Pid == 0:
    print(f"SOY EL HJIO")
    print(f"[HIJO] PID {os.getpid()} ")
    print(f"[HIJO] PPID {os.getpid()} ")
    print(f"[HIJO] Mostrando mi PCB...")
    MostrarPCB(os.getpid(), "HIJO")

    sys.exit(0) #Finaliza el proceso

else:
    print(f"[PADRE] soy el padre de {Pid}")

os.waitpid(Pid,0) #Cosecha al hijo y libera su PCB

def MostrarEstado(Pid, Etiqueta):
    with open(f"/proc/{pid}/estatus") as F:
        for L