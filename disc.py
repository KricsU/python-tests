import discord
import asyncio
import sys

async def obtener_url_de_invitacion(server_id, token):
    intents = discord.Intents.default()
    intents.guilds = True
    intents.invites = True
    bot = discord.Client(intents=intents)

    async def get_invite_url():
        try:
            await bot.start(token)
            guild = bot.get_guild(int(server_id))
            if guild:
                invite = await guild.text_channels[0].create_invite(max_age=300)  # 300 segundos
                print("Invite URL:", invite.url)
            else:
                print("No se encontró el servidor con la ID proporcionada.")
        except discord.LoginFailure:
            print("Error: Token de Discord incorrecto.")
        except discord.HTTPException as e:
            print(f"Error al conectar con Discord: {e}")
        finally:
            await bot.close()

    await get_invite_url()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python invite_url.py <ID_DEL_SERVIDOR> <TOKEN_DEL_BOT>")
        sys.exit(1)

    server_id = sys.argv[1]
    token = sys.argv[2]

    asyncio.run(obtener_url_de_invitacion(server_id, token))
