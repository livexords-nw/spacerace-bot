from datetime import datetime
import time
from colorama import Fore
import requests
import random
from fake_useragent import UserAgent
import asyncio
import json
import gzip
import brotli
import zlib
import chardet
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class spacerace:
    BASE_URL = "https://api-spacerace.entity.global:4001/"
    HEADERS = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9,id;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Host": "api-spacerace.entity.global:4001",
        "Origin": "https://spacerace.entity.global",
        "Referer": "https://spacerace.entity.global/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"' 
    }

    def __init__(self):
        self.query_list = self.load_query("query.txt")
        self.token = None
        self.config = self.load_config()
        self.session = self.sessions()

    def banner(self) -> None:
        """Displays the banner for the bot."""
        self.log("🎉 Spacerace Free Bot", Fore.CYAN)
        self.log("🚀 Created by LIVEXORDS", Fore.CYAN)
        self.log("👥 Contributors: @raecheliana", Fore.CYAN)
        self.log("📢 Channel: t.me/livexordsscript\n", Fore.CYAN)

    def log(self, message, color=Fore.RESET):
        safe_message = message.encode("utf-8", "backslashreplace").decode("utf-8")
        print(
            Fore.LIGHTBLACK_EX
            + datetime.now().strftime("[%Y:%m:%d ~ %H:%M:%S] |")
            + " "
            + color
            + safe_message
            + Fore.RESET
        )
        
    def sessions(self):
        session = requests.Session()
        retries = Retry(total=3,
                        backoff_factor=1,
                        status_forcelist=[500, 502, 503, 504, 520])
        session.mount('https://', HTTPAdapter(max_retries=retries))
        return session

    def decode_response(self, response):
        """
        Mendekode response dari server secara umum.

        Parameter:
            response: objek requests.Response

        Mengembalikan:
            - Jika Content-Type mengandung 'application/json', maka mengembalikan objek Python (dict atau list) hasil parsing JSON.
            - Jika bukan JSON, maka mengembalikan string hasil decode.
        """
        # Ambil header
        content_encoding = response.headers.get('Content-Encoding', '').lower()
        content_type = response.headers.get('Content-Type', '').lower()

        # Tentukan charset dari Content-Type, default ke utf-8
        charset = 'utf-8'
        if 'charset=' in content_type:
            charset = content_type.split('charset=')[-1].split(';')[0].strip()

        # Ambil data mentah
        data = response.content

        # Dekompresi jika perlu
        try:
            if content_encoding == 'gzip':
                data = gzip.decompress(data)
            elif content_encoding in ['br', 'brotli']:
                data = brotli.decompress(data)
            elif content_encoding in ['deflate', 'zlib']:
                data = zlib.decompress(data)
        except Exception:
            # Jika dekompresi gagal, lanjutkan dengan data asli
            pass

        # Coba decode menggunakan charset yang didapat
        try:
            text = data.decode(charset)
        except Exception:
            # Fallback: deteksi encoding dengan chardet
            detection = chardet.detect(data)
            detected_encoding = detection.get("encoding", "utf-8")
            text = data.decode(detected_encoding, errors='replace')

        # Jika konten berupa JSON, kembalikan hasil parsing JSON
        if 'application/json' in content_type:
            try:
                return json.loads(text)
            except Exception:
                # Jika parsing JSON gagal, kembalikan string hasil decode
                return text
        else:
            return text

    def load_config(self) -> dict:
        """
        Loads configuration from config.json.

        Returns:
            dict: Configuration data or an empty dictionary if an error occurs.
        """
        try:
            with open("config.json", "r") as config_file:
                config = json.load(config_file)
                self.log("✅ Configuration loaded successfully.", Fore.GREEN)
                return config
        except FileNotFoundError:
            self.log("❌ File not found: config.json", Fore.RED)
            return {}
        except json.JSONDecodeError:
            self.log(
                "❌ Failed to parse config.json. Please check the file format.",
                Fore.RED,
            )
            return {}

    def load_query(self, path_file: str = "query.txt") -> list:
        """
        Loads a list of queries from the specified file.

        Args:
            path_file (str): The path to the query file. Defaults to "query.txt".

        Returns:
            list: A list of queries or an empty list if an error occurs.
        """
        self.banner()

        try:
            with open(path_file, "r") as file:
                queries = [line.strip() for line in file if line.strip()]

            if not queries:
                self.log(f"⚠️ Warning: {path_file} is empty.", Fore.YELLOW)

            self.log(f"✅ Loaded {len(queries)} queries from {path_file}.", Fore.GREEN)
            return queries

        except FileNotFoundError:
            self.log(f"❌ File not found: {path_file}", Fore.RED)
            return []
        except Exception as e:
            self.log(f"❌ Unexpected error loading queries: {e}", Fore.RED)
            return []

    def login(self, index: int) -> None:
        # Mulai proses login
        self.log("🔐 Attempting to log in...", Fore.GREEN)

        # Validasi index token
        if index >= len(self.query_list):
            self.log("❌ Invalid login index. Please check again.", Fore.RED)
            return

        # Dapatkan token dari list dan pisahkan berdasarkan '|' untuk mendapatkan email dan password
        token = self.query_list[index]
        try:
            email, password = token.split("|", 1)
            # Hanya tampilkan 4 karakter terdepan untuk email dan password
            self.log(f"📋 Using email: {email[:4]}{'*' * (len(email) - 4) if len(email) > 4 else ''}", Fore.CYAN)
            self.log(f"🔑 Using password: {password[:4]}{'*' * (len(password) - 4) if len(password) > 4 else ''}", Fore.CYAN)
        except Exception as e:
            self.log("❌ Token format invalid. Expected format 'email|password'", Fore.RED)
            return

        # Buat payload untuk login
        payload = {"email": email, "password": password}
        # Otomatis menambahkan {self.BASE_URL} di depan endpoint auth/login
        login_url = f"{self.BASE_URL}auth/login"
        self.log("📡 Sending login request...", Fore.CYAN)
        try:
            response = requests.post(login_url, headers=self.HEADERS, json=payload)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            self.log(f"❌ Failed to send login request: {e}", Fore.RED)
            try:
                self.log(f"📄 Response content: {response.text}", Fore.RED)
            except Exception:
                pass
            return
        except Exception as e:
            self.log(f"❌ Unexpected error during login: {e}", Fore.RED)
            try:
                self.log(f"📄 Response content: {response.text}", Fore.RED)
            except Exception:
                pass
            return

        # Proses respon login
        if response.status_code == 201:
            data = self.decode_response(response)
            if "accessToken" not in data:
                self.log("❌ Login failed: accessToken not found in response", Fore.RED)
                return
            self.token = data["accessToken"]
            self.log("✅ Login successful! Token retrieved", Fore.GREEN)
        else:
            self.log(f"❌ Login request failed with status code {response.status_code}", Fore.RED)
            return

        # Request informasi user dengan endpoint auth/user
        user_url = f"{self.BASE_URL}auth/user"
        headers = {**self.HEADERS, "authorization": f"Bearer {self.token}"}
        self.log("📡 Fetching user information...", Fore.CYAN)
        try:
            user_response = requests.get(user_url, headers=headers)
            user_response.raise_for_status()
            user_data = self.decode_response(user_response)
            self.log("✅ User information retrieved successfully", Fore.GREEN)
        except requests.exceptions.RequestException as e:
            self.log(f"❌ Failed to fetch user information: {e}", Fore.RED)
            try:
                self.log(f"📄 Response content: {user_response.text}", Fore.RED)
            except Exception:
                pass
            return
        except Exception as e:
            self.log(f"❌ Unexpected error while fetching user information: {e}", Fore.RED)
            try:
                self.log(f"📄 Response content: {user_response.text}", Fore.RED)
            except Exception:
                pass
            return

        # Menampilkan informasi user penting secara user friendly
        important_keys = ["id", "email", "personalReferralCode", "isEmailConfirmed", "username"]
        self.log("👤 Important User Data:", Fore.CYAN)
        for key in important_keys:
            self.log(f"    • {key.capitalize()}: {user_data.get(key, 'N/A')}", Fore.CYAN)
            
    def mission(self) -> None:
        # Header dengan authorization yang benar
        headers = {**self.HEADERS, "authorization": f"Bearer {self.token}"}

        # Ambil daftar misi aktif
        self.log("🚀 Fetching active missions...", Fore.CYAN)
        try:
            active_response = requests.get(f"{self.BASE_URL}missions/active", headers=headers)
            active_response.raise_for_status()
            active_missions = self.decode_response(active_response)
            self.log("✅ Active missions retrieved successfully", Fore.GREEN)
        except Exception as e:
            self.log(f"❌ Failed to fetch active missions: {e}", Fore.RED)
            return

        # Ambil daftar misi yang sudah diselesaikan
        self.log("🚀 Fetching completed missions...", Fore.CYAN)
        try:
            completed_response = requests.get(f"{self.BASE_URL}users/missions", headers=headers)
            completed_response.raise_for_status()
            completed_missions = self.decode_response(completed_response)
            self.log("✅ Completed missions retrieved successfully", Fore.GREEN)
        except Exception as e:
            self.log(f"❌ Failed to fetch completed missions: {e}", Fore.RED)
            return

        # Baca file jawaban query_answer.txt sekali saja
        self.log("📄 Reading answer file...", Fore.CYAN)
        try:
            with open("query_answer.txt", "r") as f:
                answer_lines = f.readlines()
        except Exception as e:
            self.log(f"❌ Failed to read query_answer.txt: {e}", Fore.RED)
            return

        # Ambil id misi yang sudah selesai untuk pengecekan
        completed_ids = [m.get("mission", {}).get("id") for m in completed_missions if m.get("mission")]

        # Loop melalui semua misi aktif berdasarkan index
        for idx, mission in enumerate(active_missions):
            mission_id = mission.get("id")
            self.log(f"📋 Processing Mission {idx+1}: {mission.get('title', 'N/A')}", Fore.CYAN)

            # Jika misi sudah selesai, skip
            if mission_id in completed_ids:
                self.log(f"ℹ️ Mission {idx+1} already completed. Skipping.", Fore.YELLOW)
                continue

            # Cari jawaban untuk Mission {idx+1} di file
            prefix = f"Mission {idx+1}:"
            mission_line = None
            for line in answer_lines:
                if line.strip().startswith(prefix):
                    mission_line = line.strip()
                    break
            if not mission_line:
                self.log(f"❌ No answer found for Mission {idx+1}. Skipping.", Fore.RED)
                continue

            # Ekstrak jawaban (contoh: "C B A ..." menjadi list ['C', 'B', 'A', ...])
            try:
                answers_part = mission_line.split(":", 1)[1].strip()
                answer_letters = answers_part.split()
                self.log(f"📋 Found answers for Mission {idx+1}: {answer_letters}", Fore.CYAN)
            except Exception as e:
                self.log(f"❌ Failed to parse answers for Mission {idx+1}: {e}", Fore.RED)
                continue

            # Mapping huruf ke posisi: A->1, B->2, C->3, D->4
            letter_to_position = {"A": 1, "B": 2, "C": 3, "D": 4}
            try:
                answer_positions = [letter_to_position[letter.upper()] for letter in answer_letters]
            except Exception as e:
                self.log(f"❌ Invalid answer letter in Mission {idx+1}: {e}", Fore.RED)
                continue

            # Ambil pertanyaan publik untuk misi yang terpilih
            self.log(f"🚀 Fetching questions for Mission {idx+1}...", Fore.CYAN)
            try:
                questions_response = requests.get(f"{self.BASE_URL}mission/{mission_id}/questions/public", headers=headers)
                questions_response.raise_for_status()
                mission_questions = self.decode_response(questions_response)
                self.log(f"✅ Questions for Mission {idx+1} retrieved successfully", Fore.GREEN)
            except Exception as e:
                self.log(f"❌ Failed to fetch questions for Mission {idx+1}: {e}", Fore.RED)
                continue

            # Urutkan pertanyaan berdasarkan properti 'position'
            mission_questions_sorted = sorted(mission_questions, key=lambda q: q.get("position", 0))
            if len(mission_questions_sorted) != len(answer_positions):
                self.log(f"❌ Number of answers does not match number of questions for Mission {idx+1}. Skipping.", Fore.RED)
                continue

            # Mapping jawaban ke option ID berdasarkan posisi jawaban
            questions_payload = []
            skip_mission = False
            for q_idx, question in enumerate(mission_questions_sorted):
                question_id = question.get("id")
                desired_position = answer_positions[q_idx]
                picked_answer_id = None
                for ans in question.get("answers", []):
                    if ans.get("position") == desired_position:
                        picked_answer_id = ans.get("id")
                        break
                if picked_answer_id is None:
                    self.log(f"❌ Could not find answer option at position {desired_position} for question {question_id} in Mission {idx+1}. Skipping mission.", Fore.RED)
                    skip_mission = True
                    break
                questions_payload.append({
                    "questionId": question_id,
                    "pickedAnswersIds": [picked_answer_id]
                })
                self.log(f"📋 For Question {question.get('position', q_idx+1)}: selected answer option at position {desired_position} (ID: {picked_answer_id})", Fore.CYAN)

            if skip_mission:
                continue

            # Buat payload akhir untuk misi
            payload = {
                "missionId": mission_id,
                "questions": questions_payload
            }
            self.log(f"🚀 Sending answers for Mission {idx+1}...", Fore.CYAN)
            try:
                response = requests.put(f"{self.BASE_URL}users/missions/provide-answers", headers=headers, json=payload)
                response.raise_for_status()
                self.log(f"✅ Answers for Mission {idx+1} submitted successfully!", Fore.GREEN)
            except Exception as e:
                self.log(f"❌ Failed to submit answers for Mission {idx+1}: {e}", Fore.RED)
                try:
                    self.log(f"📄 Response content: {response.text}", Fore.RED)
                except Exception:
                    pass
                continue

    def lootbox(self) -> None:
        # Header dengan authorization yang benar
        headers = {**self.HEADERS, "authorization": f"Bearer {self.token}"}

        # Ambil daftar loot box yang belum dibuka
        self.log("🚀 Fetching loot boxes...", Fore.CYAN)
        try:
            loot_response = requests.get(f"{self.BASE_URL}loot-boxes/user?from=0&size=25&status=notOpened", headers=headers)
            loot_response.raise_for_status()
            loot_data = self.decode_response(loot_response)
            loot_boxes = loot_data.get("data", [])
            self.log(f"✅ Found {len(loot_boxes)} loot box(es)", Fore.GREEN)
        except Exception as e:
            self.log(f"❌ Failed to fetch loot boxes: {e}", Fore.RED)
            return

        if not loot_boxes:
            self.log("ℹ️ No loot boxes found to open.", Fore.YELLOW)
            return

        # Proses setiap loot box
        for lb in loot_boxes:
            lootbox_id = lb.get("id")
            self.log(f"📦 Processing Loot Box ID: {lootbox_id}", Fore.CYAN)

            # Ambil detail loot box
            try:
                detail_response = requests.get(f"{self.BASE_URL}loot-boxes/user/{lootbox_id}", headers=headers)
                detail_response.raise_for_status()
                detail_data = self.decode_response(detail_response)
                self.log(f"📄 Loot Box Detail: Status - {detail_data.get('status', 'N/A')}", Fore.CYAN)
            except Exception as e:
                self.log(f"❌ Failed to fetch detail for Loot Box {lootbox_id}: {e}", Fore.RED)
                continue

            # Buka loot box dengan PUT request (tanpa payload)
            self.log(f"🔓 Opening Loot Box {lootbox_id}...", Fore.CYAN)
            try:
                open_response = requests.put(f"{self.BASE_URL}loot-boxes/user/{lootbox_id}/open", headers=headers)
                open_response.raise_for_status()
                open_data = self.decode_response(open_response)
                self.log(f"✅ Loot Box {lootbox_id} opened successfully!", Fore.GREEN)
                self.log(f"💰 Points Reward: {open_data.get('pointsReward', 'N/A')}", Fore.CYAN)
                # Jika terdapat raffle tickets, tampilkan juga
                raffles = open_data.get("rafflesTickets", [])
                if raffles:
                    self.log(f"🎟️ Raffle Tickets: {len(raffles)} ticket(s) received.", Fore.CYAN)
            except Exception as e:
                self.log(f"❌ Failed to open Loot Box {lootbox_id}: {e}", Fore.RED)
                continue

    def load_proxies(self, filename="proxy.txt"):
        """
        Reads proxies from a file and returns them as a list.

        Args:
            filename (str): The path to the proxy file.

        Returns:
            list: A list of proxy addresses.
        """
        try:
            with open(filename, "r", encoding="utf-8") as file:
                proxies = [line.strip() for line in file if line.strip()]
            if not proxies:
                raise ValueError("Proxy file is empty.")
            return proxies
        except Exception as e:
            self.log(f"❌ Failed to load proxies: {e}", Fore.RED)
            return []

    def set_proxy_session(self, proxies: list) -> requests.Session:
        """
        Creates a requests session with a working proxy from the given list.

        If a chosen proxy fails the connectivity test, it will try another proxy
        until a working one is found. If no proxies work or the list is empty, it
        will return a session with a direct connection.

        Args:
            proxies (list): A list of proxy addresses (e.g., "http://proxy_address:port").

        Returns:
            requests.Session: A session object configured with a working proxy,
                            or a direct connection if none are available.
        """
        # If no proxies are provided, use a direct connection.
        if not proxies:
            self.log("⚠️ No proxies available. Using direct connection.", Fore.YELLOW)
            self.proxy_session = requests.Session()
            return self.proxy_session

        # Copy the list so that we can modify it without affecting the original.
        available_proxies = proxies.copy()

        while available_proxies:
            proxy_url = random.choice(available_proxies)
            self.proxy_session = requests.Session()
            self.proxy_session.proxies = {"http": proxy_url, "https": proxy_url}

            try:
                test_url = "https://httpbin.org/ip"
                response = self.proxy_session.get(test_url, timeout=5)
                response.raise_for_status()
                origin_ip = response.json().get("origin", "Unknown IP")
                self.log(
                    f"✅ Using Proxy: {proxy_url} | Your IP: {origin_ip}", Fore.GREEN
                )
                return self.proxy_session
            except requests.RequestException as e:
                self.log(f"❌ Proxy failed: {proxy_url} | Error: {e}", Fore.RED)
                # Remove the failed proxy and try again.
                available_proxies.remove(proxy_url)

        # If none of the proxies worked, use a direct connection.
        self.log("⚠️ All proxies failed. Using direct connection.", Fore.YELLOW)
        self.proxy_session = requests.Session()
        return self.proxy_session

    def override_requests(self):
        import random

        """Override requests functions globally when proxy is enabled."""
        if self.config.get("proxy", False):
            self.log("[CONFIG] 🛡️ Proxy: ✅ Enabled", Fore.YELLOW)
            proxies = self.load_proxies()
            self.set_proxy_session(proxies)

            # Override request methods
            requests.get = self.proxy_session.get
            requests.post = self.proxy_session.post
            requests.put = self.proxy_session.put
            requests.delete = self.proxy_session.delete
        else:
            self.log("[CONFIG] proxy: ❌ Disabled", Fore.RED)
            # Restore original functions if proxy is disabled
            requests.get = self._original_requests["get"]
            requests.post = self._original_requests["post"]
            requests.put = self._original_requests["put"]
            requests.delete = self._original_requests["delete"]


async def process_account(account, original_index, account_label, spac, config):
    # Set a random fake User-Agent for this account
    ua = UserAgent()
    spac.HEADERS["User-Agent"] = ua.random

    display_account = account[:10] + "..." if len(account) > 10 else account
    spac.log(f"👤 Processing {account_label}: {display_account}", Fore.YELLOW)

    # Override proxy if enabled
    if config.get("proxy", False):
        spac.override_requests()
    else:
        spac.log("[CONFIG] Proxy: ❌ Disabled", Fore.RED)

    # Login (blocking call executed in a thread) using the account's index
    await asyncio.to_thread(spac.login, original_index)

    spac.log("🛠️ Starting task execution...", Fore.CYAN)
    tasks_config = {
        "mission": "auto mission solve",
        "lootbox": "auto open lootbox",
    }

    for task_key, task_name in tasks_config.items():
        task_status = config.get(task_key, False)
        color = Fore.YELLOW if task_status else Fore.RED
        spac.log(
            f"[CONFIG] {task_name}: {'✅ Enabled' if task_status else '❌ Disabled'}",
            color,
        )
        if task_status:
            spac.log(f"🔄 Executing {task_name}...", Fore.CYAN)
            await asyncio.to_thread(getattr(spac, task_key))

    delay_switch = config.get("delay_account_switch", 10)
    spac.log(
        f"➡️ Finished processing {account_label}. Waiting {Fore.WHITE}{delay_switch}{Fore.CYAN} seconds before next account.",
        Fore.CYAN,
    )
    await asyncio.sleep(delay_switch)


async def worker(worker_id, spac, config, queue):
    """
    Each worker takes one account from the queue and processes it sequentially.
    A worker will not take a new account until the current one is finished.
    """
    while True:
        try:
            original_index, account = queue.get_nowait()
        except asyncio.QueueEmpty:
            break
        account_label = f"Worker-{worker_id} Account-{original_index+1}"
        await process_account(account, original_index, account_label, spac, config)
        queue.task_done()
    spac.log(
        f"Worker-{worker_id} finished processing all assigned accounts.", Fore.CYAN
    )


async def main():
    spac = spacerace()  # Initialize your spacerace instance
    config = spac.load_config()
    all_accounts = spac.query_list
    num_workers = config.get("thread", 1)  # Number of concurrent workers (threads)

    spac.log(
        "🎉 [LIVEXORDS] === Welcome to Spacerace Automation === [LIVEXORDS]",
        Fore.YELLOW,
    )
    spac.log(f"📂 Loaded {len(all_accounts)} accounts from query list.", Fore.YELLOW)

    if config.get("proxy", False):
        proxies = spac.load_proxies()

    while True:
        # Create a new asyncio Queue and add all accounts (with their original index)
        queue = asyncio.Queue()
        for idx, account in enumerate(all_accounts):
            queue.put_nowait((idx, account))

        # Create worker tasks according to the number of threads specified
        workers = [
            asyncio.create_task(worker(i + 1, spac, config, queue))
            for i in range(num_workers)
        ]

        # Wait until all accounts in the queue are processed
        await queue.join()

        # Cancel workers to avoid overlapping in the next loop
        for w in workers:
            w.cancel()

        spac.log("🔁 All accounts processed. Restarting loop.", Fore.CYAN)
        delay_loop = config.get("delay_loop", 30)
        spac.log(
            f"⏳ Sleeping for {Fore.WHITE}{delay_loop}{Fore.CYAN} seconds before restarting.",
            Fore.CYAN,
        )
        await asyncio.sleep(delay_loop)


if __name__ == "__main__":
    asyncio.run(main())
