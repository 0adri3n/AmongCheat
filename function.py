import pymem, pymem.process
import time
pm = pymem.Pymem("Among Us.exe")
module = pymem.process.module_from_name(pm.process_handle, "UnityPlayer.dll").lpBaseOfDll

def GetPtrAdress(base, offsets):
    addr = pm.read_int(base)
    for i in offsets:
        if i != offsets[-1]:
            addr = pm.read_int(addr + i)
    return addr + offsets[-1]

def speedhack(speedvalue):
    pm.write_float(GetPtrAdress(module + 0x01449738, [0xC4, 0x548, 0x1C, 0x5C, 0x5C, 0x24, 0x8]), float(speedvalue))

