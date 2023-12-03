import pymem, keyboard, time
import win32api

LOCAL_PLAYER = 0x509b74
FORCE_JUMP = 0x6B
HEALTH = 0xF8
ON_GROUND = 0x69
FORCE_ATTACK = 0x224
Y_VIEW = 0x44

def bhop() -> None:
    print('Bhop has launched.')
    pm = pymem.Pymem('ac_client.exe')

    # hack loop
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
        if win32api.GetAsyncKeyState(0x20) and win32api.GetAsyncKeyState(0x01):
            pm.write_uint(local_player + FORCE_JUMP, 6)
            pm.write_uint(local_player + Y_VIEW, -90)
            # pm.write_uint(local_player + FORCE_ATTACK, 1092831209)


if __name__ == '__main__':
    bhop()