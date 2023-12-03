import pymem, keyboard, time
import win32api

LOCAL_PLAYER = 0x509b74
FORCE_JUMP = 0x6B
HEALTH = 0xF8
ON_GROUND = 0x69

def bhop() -> None:
    print('Bhop has launched.')
    pm = pymem.Pymem('ac_client.exe')

    while True:
        time.sleep(0.01)

        # space bar
        if not win32api.GetAsyncKeyState(0x20):
            continue

        local_player: int = pm.read_uint(LOCAL_PLAYER)

        if not local_player:
            continue

        # is alive
        if not pm.read_int(local_player + HEALTH):
            continue

        # on ground
        if (pm.read_uint(local_player + ON_GROUND) == 1):
            pm.write_uint(local_player + FORCE_JUMP, 1)


if __name__ == '__main__':
    bhop()