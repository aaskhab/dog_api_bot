from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    admin_id: int

    @staticmethod
    def from_env(env: Env):
        token = env.str('BOT_TOKEN')
        admin_id = env.int('ADMIN_ID')

        return TgBot(token=token, admin_id=admin_id)
    

@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None):

    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot.from_env(env))