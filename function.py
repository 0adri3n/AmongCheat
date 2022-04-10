import pymem, pymem.process
import time
pm = pymem.Pymem("Among Us.exe")
module = pymem.process.module_from_name(pm.process_handle, "GameAssembly.dll").lpBaseOfDll
module2 = pymem.process.module_from_name(pm.process_handle, "UnityPlayer.dll").lpBaseOfDll

def GetPtrAdress(base, offsets):
    addr = pm.read_int(base)
    for i in offsets:
        if i != offsets[-1]:
            addr = pm.read_int(addr + i)
    return addr + offsets[-1]

def speedhack(speedvalue):
    pm.write_float(GetPtrAdress(module2 + 0x0147642C, [0x88, 0x524, 0x50, 0x4, 0x5C, 0x24, 0x8]), float(speedvalue))

