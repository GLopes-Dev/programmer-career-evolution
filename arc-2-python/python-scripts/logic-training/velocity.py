velocity = float(input('Car Velocity: '))
if velocity > 80:
    print("\033[1;31mYou've got fined \033[m")
    print(f"You'll need to pay {'\033[4;32m'}¥{(velocity - 80) * 5:.2f} Yens. {'\033[m'}")
else:
    print('\033[1;32m Have a good day. Drive Safe! \033[m')