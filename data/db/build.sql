CREATE TABLE IF NOT EXISTS guilds (
    GuildID integer PRIMARY KEY,
    Prefix text DEFAULT !,
    LangBot text DEFAULT english,
    LangCom text DEFAULT english,
    EmbedColor text 0x108318
);