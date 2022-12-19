from chess.factory import init_field, create_user


def main():
    user_1 = create_user()
    user_2 = create_user()

    init_field(user_1, user_2)

    while True:
        # game loop
        pass
