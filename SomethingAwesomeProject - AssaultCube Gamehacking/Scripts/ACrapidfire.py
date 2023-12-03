import pymem, keyboard, time
import win32api

LOCAL_PLAYER = 0x509b74
HEALTH = 0xF8
RIFLE_FIRERATE = 0x178
PISTOLE_FIRERATE = 0x164

def rapidfire() -> None:
    print("Rapid fire has been launched.")
    pm = pymem.Pymem('ac_client.exe')

    while True:
        time.sleep(0.01)
        # left-click
        if not win32api.GetAsyncKeyState(0x01):
            continue

        local_player: int = pm.read_uint(LOCAL_PLAYER)

        if not local_player:
            continue

        # is alive
        if not pm.read_int(local_player + HEALTH):
            continue
        
        if pm.read_uint(local_player + RIFLE_FIRERATE) == 120:
            pm.write_uint(local_player + RIFLE_FIRERATE, 60)
        
        # pistol kinda useless though
        if pm.read_uint(local_player + PISTOLE_FIRERATE) == 160:
            pm.write_uint(local_player + RIFLE_FIRERATE, 60)

if __name__ == '__main__':
    rapidfire()