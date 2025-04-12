
---
<h1 align="center">Spacerace Bot</h1>


<p align="center">
<strong>Boost your productivity with Spacerace Bot – your friendly automation tool that handles key tasks with ease!</strong>
</p>

<p align="center">
<a href="https://github.com/livexords-nw/spacerace-bot/actions">
<img src="https://img.shields.io/github/actions/workflow/status/livexords-nw/spacerace-bot/ci.yml?branch=main" alt="Build Status" />
</a>
<a href="https://github.com/livexords-nw/spacerace-bot/releases">
<img src="https://img.shields.io/github/v/release/livexords-nw/spacerace-bot" alt="Latest Release" />
</a>
<a href="https://github.com/livexords-nw/spacerace-bot/blob/main/LICENSE">
<img src="https://img.shields.io/github/license/livexords-nw/spacerace-bot" alt="License" />
</a>
<a href="https://t.me/livexordsscript">
<img src="https://img.shields.io/badge/Telegram-Join%20Group-2CA5E0?logo=telegram&style=flat" alt="Telegram Group" />
</a>
</p>

---

## 🚀 About the Bot

Spacerace Bot is your automation buddy designed to simplify daily operations. This bot takes over repetitive tasks so you can focus on what really matters. With Spacerace Bot, you get:

- **🕹️ Auto Solve Mission:**  
  Automatically solve missions by reading your query file and submitting answers for you.
- **🎁 Auto Open Lootbox:**  
  Automatically check for and open your available lootboxes to claim rewards.
- **Multi Account Support 👥:**  
  Manage multiple accounts effortlessly with built-in multi account support.
- **Thread System 🧵:**  
  Run tasks concurrently with configurable threading options to improve overall performance and speed.
- **Configurable Delays ⏱️:**  
  Fine-tune delays between account switches and loop iterations to match your specific workflow needs.
- **Support Proxy 🔌:**  
  Use HTTP/HTTPS proxies to enhance your multi-account setups.

Spacerace Bot is built with flexibility and efficiency in mind – it's here to help you automate your operations and boost your productivity!

---

## 🌟 Version Updates

**Current Version: v1.0.2**

### v1.0.2 - Latest Update

- Addition of answers for mission 39
- The answer system has been updated so there's no need to run `git pull` anymore to update answers, as it is now linked directly to the bot's repository

---

## 📝 Register

Before you start using Spacerace Bot, make sure to register your account.  
Click the link below to get started:

[🔗 Register for Spacerace Bot](https://spacerace.entity.global/?referral=IEZYOMME)

---

## ⚙️ Configuration

### Main Bot Configuration (`config.json`)

```json
{
  "lootbox": true,
  "mission": true,
  "thread": 1,
  "proxy": false,
  "delay_account_switch": 10,
  "delay_loop": 3000
}
```

| **Setting**            | **Description**                                | **Default Value** |
| ---------------------- | ---------------------------------------------- | ----------------- |
| `mission`              | Enable auto mission solving functionality.     | `true`            |
| `lootbox`              | Enable auto lootbox opening functionality.     | `true`            |
| `thread`               | Number of threads to run concurrently.         | `1`               |
| `proxy`                | Enable proxy usage for multi-account setups.   | `false`           |
| `delay_account_switch` | Delay (in seconds) between switching accounts. | `10`              |
| `delay_loop`           | Delay (in seconds) before the next loop.       | `3000`            |

---

## 📅 Requirements

- **Minimum Python Version:** `Python 3.9+`
- **Required Libraries:**
  - colorama
  - requests
  - fake-useragent
  - brotli
  - chardet
  - urllib3

These are installed automatically when running:

```bash
pip install -r requirements.txt
```

---

## 📅 Installation Steps

### Main Bot Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/livexords-nw/spacerace-bot.git
   ```

2. **Navigate to the Project Folder**

   ```bash
   cd spacerace-bot
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Your Query**

   Create a file named `query.txt` with your query data in the following format:  
   **email|password**.

5. **Set Up Proxy (Optional)**  
   To use a proxy, create a `proxy.txt` file and add proxies in the format:

   ```
   http://username:password@ip:port
   ```

   _Only HTTP and HTTPS proxies are supported._

6. **Run Bot**

   ```bash
   python main.py
   ```

---

### 🔹 Want Free Proxies?

You can obtain free proxies from [Webshare.io](https://www.webshare.io/).

---

## 📂 Project Structure

```
spacerace-bot/
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI workflow for automated checks/deploys
├── config.json                 # Main configuration file for the bot
├── query.txt                   # Contains query data to be processed
├── proxy.txt                   # (Optional) Proxy list (HTTP/HTTPS) to use for multi-account support
├── query_answer.txt           # List of answers for each mission question (e.g., Mission 1: A B C)
├── main.py                     # Main Python script (entry point of the bot)
├── requirements.txt            # Python dependencies required to run the bot
├── LICENSE                     # License for the project
└── README.md                   # Documentation and feature list
```

---

## 🛠️ Contributing

This project is developed by **Livexords**.  
If you have ideas, questions, or want to contribute, please join our Telegram group for discussions and updates.  
For contribution guidelines, please consider:

- **Code Style:** Follow standard Python coding conventions.
- **Pull Requests:** Test your changes before submitting a PR.
- **Feature Requests & Bugs:** Report and discuss via our Telegram group.

<div align="center">
  <a href="https://t.me/livexordsscript" target="_blank">
    <img src="https://img.shields.io/badge/Join-Telegram%20Group-2CA5E0?logo=telegram&style=for-the-badge" height="25" alt="Telegram Group" />
  </a>
</div>

---

## 📖 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for more details.

---

## 🔍 Usage Example

After installation and configuration, simply run:

```bash
python main.py
```

You should see output indicating the bot has started its operations. For further instructions or troubleshooting, please check our Telegram group or open an issue in the repository.

---

## 📣 Community & Support

For support, updates, and feature requests, join our Telegram group.  
This is the central hub for all discussions related to Spacerace Bot, including roadmap ideas and bug fixes.

---
