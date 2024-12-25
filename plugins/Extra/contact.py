from pyrogram import Client, filters, enums
from info import ADMINS

OWNER = 6666362904

#Send message to admin
@Client.on_message(filters.command('admin'))
async def admin_send(client, message):
    try:
        # the user ID
        admin_id = int(OWNER)  # Convert to integer
        
        # Ask for the message to send
        PM_MESSAGE = await client.ask(chat_id=message.from_user.id, text="Now Send Me The Message To Be Sent")
        
        userid = message.from_user.id
        DEFAULT_TXT = """YOU HAVE A MESSAGE FROM USER ID <code>{user}</code>\n\n"""
        
        # Format the user ID into the default text
        USER_TXT = DEFAULT_TXT.format(user=userid)
        
        # Combine the default text with the user's message
        pm_text = USER_TXT + PM_MESSAGE.text
        
        # Send the message to the admin
        await client.send_message(chat_id=admin_id, text=pm_text)
        fs = 0

    except ValueError:
        await client.send_message(chat_id=message.from_user.id, text="Something wrong Try again later")
        fs = 1
    except Exception as e:
        await client.send_message(chat_id=message.from_user.id, text=f"An error occurred: {str(e)}")
        fs = 1
    if fs != 1:
        await client.send_message(chat_id=message.from_user.id, text="Message Send to Admin")

#Send message to a single user
@Client.on_message(filters.command('pm') & filters.user(ADMINS))
async def pm_send(client, message):
    try:
        # Ask for the user ID
        pm_user = await client.ask(chat_id=message.from_user.id, text="Now Send Me The User ID")
        pm_user_id = int(pm_user.text)  # Convert to integer
        
        # Ask for the message to send
        PM_MESSAGE = await client.ask(chat_id=message.from_user.id, text="Now Send Me The Message To Be Sent")
        pm_text = PM_MESSAGE.text
        
        # Send the message to the specified user
        await client.send_message(chat_id=pm_user_id, text=pm_text)
        val = 0

    except ValueError:
        await client.send_message(chat_id=message.from_user.id, text="The User ID must be a number.")
        val = 1
    except Exception as e:
        await client.send_message(chat_id=message.from_user.id, text=f"An error occurred: {str(e)}")
        val = 1
    if val != 1:
        await client.send_message(chat_id=message.from_user.id, text="Message Send To User Successfully")