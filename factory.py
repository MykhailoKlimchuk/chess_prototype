from chess.user import User


def create_default_figures(user) -> dict:
    """

    :param user:
    :return: {
        figure_id: figure_obj
    }
    """
    pass


def init_field(user_1, user_2):

    field = {}

    field.update(create_default_figures(user_1))
    field.update(create_default_figures(user_2))

    return field


def create_user() -> User:
    pass
