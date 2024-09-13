---

# Encourage Bot 🤖 - Your Personal Motivation Assistant

**Encourage Bot** is a simple yet powerful Discord bot built using Python, designed to uplift and motivate users with daily encouragement. The bot is hosted on Replit and offers several features, including inspiring quotes, personalized motivation, and easy management of your own motivational messages. Whether you're looking for a quick boost or want to share positivity, Encourage Bot is here for you!

## Features ✨

- **Inspire:** Get an inspirational quote with the command `$inspire`.
- **New Motivation:** Add your own motivational quotes with `$new <your message>`.
- **List Motivations:** View all stored motivational messages with `$list`.
- **Delete Motivation:** Remove a specific motivational message with `$delete <index>`.

## Commands 🛠️

| Command         | Description                                                  |
| --------------- | ------------------------------------------------------------ |
| `$hello`        | Responds with "Hello!" to greet the user.                     |
| `$inspire`      | Sends a random inspirational quote.                           |
| `$new <message>`| Adds a new custom motivational message to the list.           |
| `$list`         | Displays all stored custom motivational messages.             |
| `$delete <index>`| Deletes a custom motivational message by its index in the list. |

## Getting Started 🚀

### Prerequisites

- **Python 3.8+**
- **Discord Account**
- **Discord Bot Token**: [How to create a Discord Bot](https://discordpy.readthedocs.io/en/stable/discord.html)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/encourage-bot.git
   ```
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - In Replit or locally, set the `TOKEN` environment variable to your Discord bot token.
   - In Replit: Go to the Secrets tab and add a secret with key `TOKEN` and value as your bot's token.

4. Run the bot:
   ```bash
   python main.py
   ```

## Usage 🎯

- Invite the bot to your Discord server with appropriate permissions.
- Use the commands mentioned above to interact with the bot and get daily motivation!

## Permissions 🔑

Make sure to give the bot the following permissions for it to function properly:
- **Send Messages**
- **Read Messages**
- **Manage Messages** (for deleting messages)
- **Embed Links** (for sending formatted quotes)

## Development 🛠️

Feel free to contribute to this project! If you'd like to add new features or improve existing functionality, here's how you can get started:

1. Fork this repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact 📬

- **Creator:** Hrishabh Dubey
- **Email:** rishabh6398@gmail.com
- **LinkedIn:** [Hrishabh Dubey](https://www.linkedin.com/in/hrishabhdubey/)

---
