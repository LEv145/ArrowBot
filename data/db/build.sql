CREATE TABLE IF NOT EXISTS guilds (
    GuildID integer PRIMARY KEY,
    Prefix text DEFAULT '!',
    LangBot text,
    LangCom text,
    EmbedColor text
);