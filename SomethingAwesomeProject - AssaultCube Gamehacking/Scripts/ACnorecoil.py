import pymem
import time
import win32api

LOCAL_PLAYER = 0x509b74
HEALTH = 0xF8
RIFLE_FIRERATE = 0x178
PISTOLE_FIRERATE = 0x164
Y_VIEW = 0x44

def norecoil() -> None:
    print("No recoil has been launched.")
    pm = pymem.Pymem('ac_client.exe')

    while True:
        time.sleep(0.01)
        if not win32api.GetAsyncKeyState(0x01):
            continue

        local_player: int = pm.read_uint(LOCAL_PLAYER)

        if not local_player:
            continue

        if not pm.read_int(local_player + HEALTH):
            continue

        if pm.read_uint(local_player + RIFLE_FIRERATE) > 0:
            current_y = pm.read_float(local_player + Y_VIEW)
            recoil_amount = 0.28
            new_y = current_y - recoil_amount
            pm.write_float(local_player + Y_VIEW, new_y)

if __name__ == '__main__':
    norecoil()
