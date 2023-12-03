import pymem
import time
import win32api
import keyboard

ENTITY_LIST = 0x10f4f8
LOCAL_PLAYER = 0x509b74
HEALTH_OFFSET = 0xF8
CLIENT = 0x400000
ENTITY_SIZE = 0x4
FORCE_ATTACK = 0x224
TEAM_OFFSET = 0x32C
NAME_OFFSET = 0x225
DISPLAY_NAME = 0x101C38
GRENADES_OFFSET = 0x158


def get_character_entities(pm):
    # entity list base addr
    entity_list_base = pm.read_int(CLIENT + ENTITY_LIST)
    
    entities_data = {}
    # 16 for testing rn. need to find way to get entity count
    # skip first range since always empty
    for i in range(1, 16):
        try:
            entity_address = pm.read_int(entity_list_base + i * ENTITY_SIZE)
            health = pm.read_int(entity_address + HEALTH_OFFSET)
            team = pm.read_int(entity_address + TEAM_OFFSET)
            # name = pm.read_string(entity_address + NAME_OFFSET)
            if entity_address in entities_data:
                # If we already have this entity address recorded, skip it
                continue
            # skip invalid addresses
            try:
                name = pm.read_string(entity_address + NAME_OFFSET)
            except UnicodeDecodeError:
                # decoding error for entities with invalid names
                continue
            if team != 0 and team != 1:
                continue
            if health < -50 or health > 150:
                continue
            entity_data = {'name': name, 'health': health, 'team': team, 'address': entity_address}
            entities_data[i] = entity_data
        except pymem.exception.MemoryReadError as e:
            continue
    return entities_data

def get_entity_by_name(entities_info):
    return {info['name']: entity_num for entity_num, info in entities_info.items() if info['name']}

def get_player_team(entities):
    if len(entities) == 0:
        return None
    team_counts = {}
    # dict for num on each team
    for entity_num, entity_details in entities.items():
        team = entity_details['team']
        if team not in team_counts:
            team_counts[team] = 0
        team_counts[team] += 1

    # find team with less members
    min_team = min(team_counts, key=team_counts.get)
    player_team = min_team
    # print(f"Player team: {player_team}")
    # for entity_num, entity_details in entities.items():
    #     print(f"Entity {entity_num}: {entity_details}")

    return player_team

def triggerbot():
    print("Trigger has been launched")
    pm = pymem.Pymem("ac_client.exe")
    entities = get_character_entities(pm)
    entity_lookup_by_name = get_entity_by_name(entities)
    player_team = get_player_team(entities)

    can_shoot = False
    while True:
        time.sleep(0.01)
        local_player: int = pm.read_uint(LOCAL_PLAYER)
        current_name = pm.read_string(CLIENT + DISPLAY_NAME)
        pm.write_string(CLIENT + DISPLAY_NAME, "\0" * 20)
        
        # check if current name matches any known entity's name
        if current_name in entity_lookup_by_name:
            entity_num = entity_lookup_by_name[current_name]
            entity_details = entities[entity_num]
            team = entity_details['team']
            if team != player_team:
                can_shoot = True
            else:
                can_shoot = False
        else:
            can_shoot = False
            
        if can_shoot:
            pm.write_uint(local_player + FORCE_ATTACK, 1)
        else:
            pm.write_uint(local_player + FORCE_ATTACK, 0)

if __name__ == "__main__":
    triggerbot()
