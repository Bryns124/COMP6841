import pymem
import time

LOCAL_PLAYER = 0x00509b74
HEALTH = 0xF8
RIFLE_AMMO = 0x150
PISTOL_AMMO = 0x13C

def infinitehealthammo():
    print("Infinite health and ammo has launched.")
    pm = pymem.Pymem('ac_client.exe')

    while True:
        time.sleep(0.01)

        local_player: int = pm.read_uint(LOCAL_PLAYER)

        health_address = local_player + HEALTH
        pm.write_int(health_address, 420)

        rifle_ammo_address = local_player + RIFLE_AMMO
        pm.write_int(rifle_ammo_address, 420)

        pistol_ammo_address = local_player + PISTOL_AMMO
        pm.write_int(pistol_ammo_address, 420)

if __name__ == "__main__":
    infinitehealthammo()