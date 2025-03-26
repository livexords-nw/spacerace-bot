---

<h1 align="center">Spacerace Bot</h1>

<p align="center">Boost your productivity with Spacerace Bot – your friendly automation tool that handles key tasks with ease! 🚀</p>

---

## 🚀 About the Bot

Spacerace Bot is your automation buddy designed to simplify daily operations. This bot takes over repetitive tasks so you can focus on what really matters. With Spacerace Bot, you get:

- **👥 Multi Account Support:**  
  Manage multiple accounts with ease.

- **🧵 Thread System:**  
  Execute tasks concurrently using configurable threads.

- **⏱️ Configurable Delays:**  
  Adjust delays between account switches and loop cycles to suit your operational tempo.

- **🕹️ Auto Solve Mission:**  
  Automatically solve missions by reading your query file and submitting answers for you.

- **🎁 Auto Open Lootbox:**  
  Automatically check for and open your available lootboxes to claim rewards.

- **🔌 Support Proxy:**  
  Use HTTP/HTTPS proxies to enhance your multi-account setups.

Spacerace Bot is built with flexibility and efficiency in mind – it's here to help you automate your operations and boost your productivity!

---

## 🌟 Version Updates

**Current Version: v1.0.0**

### v1.0.0 - Initial Release

- 👥 **Multi Account Support:** Manage multiple accounts with ease.
- 🧵 **Thread System:** Execute tasks concurrently using configurable threads.
- ⏱️ **Configurable Delays:** Adjust delays between account switches and loop cycles.
- 🕹️ **Auto Solve Mission:** Automatically process and solve missions using your query file.
- 🎁 **Auto Open Lootbox:** Efficiently check for and open lootboxes to claim rewards.
- 🔌 **Support Proxy:** Use proxies to manage your connections effectively.

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

| **Setting**            | **Description**                                   | **Default Value** |
| ---------------------- | ------------------------------------------------- | ----------------- |
| `mission`              | Enable auto mission solving functionality. 🕹️     | `true`            |
| `lootbox`              | Enable auto lootbox opening functionality. 🎁     | `true`            |
| `thread`               | Number of threads to run concurrently. 🧵         | `1`               |
| `proxy`                | Enable proxy usage for multi-account setups. 🔌   | `false`           |
| `delay_account_switch` | Delay (in seconds) between switching accounts. ⏱️ | `10`              |
| `delay_loop`           | Delay (in seconds) before the next loop. ⏱️       | `3000`            |

**Note:**  
The query format for login is: **email|password**

---

## 📥 Installation Steps

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
   **email|password**

5. **Set Up Proxy (Optional)**  
   To use a proxy, create a file named `proxy.txt` and add proxies in the format:

   ```
   http://username:password@ip:port
   ```

   - Only HTTP and HTTPS proxies are supported.

6. **Run Bot**

   ```bash
   python main.py
   ```

---

### 🔹 Want Free Proxies?

You can obtain free proxies from [Webshare.io](https://www.webshare.io/).

---

## 🛠️ Contributing

This project is developed by **Livexords**. If you have ideas, questions, or want to contribute, please reach out!

<div align="center">
  <a href="https://t.me/livexordsscript" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Livexords&logo=telegram&label=&color=2CA5E0&logoColor=white&style=for-the-badge" height="25" alt="Telegram Logo" />
  </a>
</div>

---
