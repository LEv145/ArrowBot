CREATE TABLE IF NOT EXISTS guilds (
    GuildID BIGINT PRIMARY KEY,
    Prefix VARCHAR(5) DEFAULT '!',
    LangBot VARCHAR(25),
    LangCom VARCHAR(25),
    EmbedColor VARCHAR(12)
);