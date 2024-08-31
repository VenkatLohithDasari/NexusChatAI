import os
import json
import discord
from discord.ext import commands
from dotenv import load_dotenv
from context_manager.context_manager import ContextManager
from prompt_creator.prompt_creator import PromptCreator
from ai_api.together_ai import TogetherAI

load_dotenv()

context_manager = ContextManager()
prompt_creator = PromptCreator()
together_ai = TogetherAI(api_key=os.getenv("TOGETHER_API_KEY"))

intents = discord.Intents.default()
intents.message_content = True


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        await self.tree.sync()


bot = MyBot()

# load configuration settings
with open('config/config.json', 'r') as config_file:
    config = json.load(config_file)


@bot.event
async def on_ready():
    print(f"{bot.user} has conneected to Discord!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


@bot.tree.command(name="ping", description="Check if the bot is responsive")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user in message.mentions or message.reference:
        channel_id = message.channel.id
        context = context_manager.load_context(channel_id)

        user_display_name = message.author.display_name
        user_message = message.content
        custom_instructions = config.get("custom_instructions", None)
        ai_name = config.get("ai_name", "Assistant")

        prompt = prompt_creator.create_prompt(
            config["system_prompt"],
            context,
            user_display_name,
            user_message,
            custom_instructions,
            ai_name
        )

        async with message.channel.typing():
            ai_response = together_ai.generate_response(
                prompt,
                config
            )

        await message.reply(ai_response)

        context.append({"user": user_display_name, "message": user_message})
        context.append({"user": "T@ai_name@T", "message": ai_response})
        context_manager.save_context(channel_id, context)

token = os.getenv("DISCORD_TOKEN")

bot.run(token)
