import sys

if len(sys.argv) < 2:
    print("Iltimos argument kiriting!")
    sys.exit(1)
    # Xato kodi bilan chiqish
else:
    print("Arguments: ", sys.argv[1:])
    sys.exit(0)
    # Muvaffaqiyatli yakunlanish
