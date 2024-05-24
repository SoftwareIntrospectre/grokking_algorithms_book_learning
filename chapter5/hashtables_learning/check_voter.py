voted = {}

def check_voter(name):
    if name in voted:
        print(f"Kick {name} out! Already voted.")
    else:
        voted[name] = True
        print(f"Let {name} vote! Not voted yet.")

check_voter("Tom")
check_voter("Mike")
check_voter("Mike")
