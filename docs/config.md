# LibreShortURL Configuration Guide

The application uses a `.env`-style configuration file named `config.env` to manage runtime settings.

---

## Location

Place your `config.env` file in the root directory of your project:

```
LibreShortURL/
└── config.env
```

---

## Configuration Options

### 🔹 `SERVER_DOMAIN`

- **Type:** `string`
- **Description:** Your domain name used for generating shortened URLs.
- **Example:**

  ```env
  SERVER_DOMAIN=short.yourdomain.com
  ```

- **Note:** **Do not include `http://` or `https://`** – it's added automatically.

---

### 🔹 `SERVER_HOST`

- **Type:** `string`

- **Default:** `localhost`

- **Description:** The host address where the Flask server will bind.

- **Example:**

  ```env
  SERVER_HOST=0.0.0.0
  ```

- **Tip:** Use `0.0.0.0` to expose on all interfaces (for deployment).

---

### 🔹 `SERVER_PORT`

- **Type:** `int`
- **Default:** `5000`
- **Description:** The port on which to run the server.
- **Example:**

  ```env
  SERVER_PORT=80
  ```

---

### 🔹 `REQ_LIMIT_PER_DAY`

- **Type:** `int`
- **Default:** `50`
- **Description:** Maximum number of API calls allowed per user (IP) per day.
- **Example:**

  ```env
  REQ_LIMIT_PER_DAY=100
  ```

---

## 🧪 Experimental / Upcoming Fields

These fields are for **future support** and may be ignored for now:

---

### 🔹 `CUSTOM_DB`

- **Type:** `bool` (`true` or `false`)
- **Default:** `false`
- **Description:** Enable custom database path support.

---

### 🔹 `CUSTOM_URL_BLACKLIST_DB`

- **Type:** `bool`
- **Default:** `false`
- **Description:** Enable custom URL blacklist path support.

---

### 🔹 `DB_PATH`

- **Type:** `string`
- **Description:** Custom path to the SQLite database file.
- **Only used if:** `CUSTOM_DB=true`

---

### 🔹 `URL_BLACKLIST_PATH`

- **Type:** `string`
- **Description:** Custom path to the URL blacklist file.
- **Only used if:** `CUSTOM_URL_BLACKLIST_DB=true`

---

## Example `config.env`

```env
SERVER_DOMAIN=short.example.com
SERVER_HOST=0.0.0.0
SERVER_PORT=80

REQ_LIMIT_PER_DAY=100

CUSTOM_DB=false
CUSTOM_URL_BLACKLIST_DB=false
DB_PATH=""
URL_BLACKLIST_PATH=""
```

**Note**:
- If the `config.env` is not create before running the `setup.py` or `run.sh` , it will be auto-generated on default values.