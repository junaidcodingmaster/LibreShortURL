# LibreShortURL

**LibreShortURL** is a minimalistic, privacy-friendly, and lightweight URL shortener.

It’s a web application that includes both a frontend website and a backend API server to shorten URLs. Open-source, developer-friendly, and simple to host — built using **Flask** and **Python**.

## ✨ Features

- Lightweight & Minimalist
- Simple to Use
- Fully Self-Hostable
- No Analytics
- No Trackers
- Easy-to-Use APIs
- 🔒 Self-Destructing URLs [*coming soon*]
- 🔑 Password-Protected URLs [*coming soon*]

## 🔌 APIs

- `POST /api/gen-url`  
  Generate a shortened URL from an original URL.

- `POST /api/check-name-availability`  
  Check if a custom short name is valid and available.

For detailed API docs, see [`docs/apis.md`](docs/apis.md)

## ⚙️ Configuration

Create a `.env` file or `config.env` with these values:

```env
SERVER_DOMAIN=yourdomain.com     # without http(s)
SERVER_HOST=0.0.0.0              # use 0.0.0.0 for public server
SERVER_PORT=5000                 # use 80 for HTTP servers
REQ_LIMIT_PER_DAY=50             # limit requests per IP per day
```


You can change these values depending on your server specs and traffic.

More in [`docs/config.md`](docs/config.md)

## 🚀 Installation
Clone Repo:
```
git clone https://github.com/junaidcodingmaster/LibreShortURL
cd LibreShortURL
```

Automatic:

```bash
chmod +x ./run.sh
./run.sh
```

Manual:

```bash
pip install -r requirements.txt
python3 ./setup.py
flask run --host "0.0.0.0" --port 80
```

## 🧩 Use Cases

- Host your own URL shortening service
- Run a local development tool for quick URL shortening
- Learn how URL shorteners work internally
- Build your own business on top of this base

## 👨‍💻 Developer Notes

> "Use it for any project — just stay curious, my friends!"
> — _Made by Junaid_

---

### 🔍 Highlights of Changes:
- Fixed typos like `friednly`, `lightweigth`, `manimual`, etc.
- Improved sentence clarity ("An application that..." → "It’s a web application that...")
- Used standard markdown formatting for better readability
- Preserved your tone and made it feel polished but still personal

## License
- This project is under MIT License

---
**Made By [Junaid](https://abujuni.dev)**