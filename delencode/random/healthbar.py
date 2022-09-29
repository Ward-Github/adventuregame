from colorama import Fore

hp = 100

def healthbar(hp):
    health = hp // 10
    removed_health = (10 - health)
    health_bar = f'|{Fore.GREEN}'

    for i in range(health):
        health_bar += f'x'
    for i in range(removed_health):
        health_bar += f'{Fore.RED}x'

    health_bar += f'{Fore.WHITE}|'
    return health_bar

def healthbar_enemy(enemy_hp, enemy_total_hp):
    health = enemy_hp // 10
    enemy_hp_left = enemy_total_hp // 10
    removed_health = (enemy_hp_left - health)
    health_bar = f'|{Fore.GREEN}'

    for i in range(health):
        health_bar += f'x'
    for i in range(removed_health):
        health_bar += f'{Fore.RED}x'

    health_bar += f'{Fore.WHITE}|'
    return health_bar