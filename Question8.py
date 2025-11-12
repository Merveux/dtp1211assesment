is_raining=False
has_umbrella=False
if is_raining and has_umbrella:
    print("Allowed to go out")
elif not is_raining and has_umbrella:
    print("Allowed to go out")
elif is_raining and not has_umbrella:
    print("Not Allowed to go out")
elif not is_raining and has_umbrella:
    print("Allowed to go out")
else:
    print("Allowed to go out")
