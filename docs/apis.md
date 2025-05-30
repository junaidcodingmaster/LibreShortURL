# LibreShortURL API Documentation

LibreShortURL provides a lightweight and privacy-friendly way to generate and manage shortened URLs. Below is the detailed API reference.

---

## Base URL

```plaintext
https://<your-domain>/
```

> ⚠️ Replace `<your-domain>` with your server domain as configured in `config.env`.

---

## `POST /api/gen-url`

### ➤ Description

Generates a shortened URL for a given original URL.

### 🔸 Request Headers

```http
Content-Type: application/json
```

### 🔸 Request Body

```json
{
  "url": "https://example.com",
  "name": "mycustomalias" // Optional. Auto-generated if not provided.
}
```

- `url` _(required)_: Original URL to shorten.
- `name` _(optional)_: Custom alias (max 18 chars). If omitted, a random name is generated.

### 🔸 Response

**Success (200)**

```json
{
  "message": "URL successfully Created and hosted.",
  "url": "https://yourdomain/mycustomalias"
}
```

**Error (400/401/500)**

```json
{ "message": "URL is missing!" }
{ "message": "Too Long" }
{ "message": "NOT ALLOWED" }
{ "message": "mycustomalias - Already exists!" }
```

### 🔒 Rate Limiting

Default: `50 requests per day` _(configurable in `config.env`)_

---

## `POST /api/check-name-availability`

### ➤ Description

Checks if a custom short name (alias) is available.

### 🔸 Request Headers

```http
Content-Type: application/json
```

### 🔸 Request Body

```json
{ "name": "mycustomalias" }
```

### 🔸 Response

**Available:**

```json
{ "message": "mycustomalias - Available!" }
```

**Unavailable:**

```json
{ "message": "mycustomalias - Already exists!" }
```

**Blacklist or Error:**

```json
{ "message": "NOT ALLOWED" }
{ "message": "Too Long" }
```

---

## 🔗 `GET /<name>`

### ➤ Description

Redirects to the original URL for the given short name.

### 🔸 Example

```http
GET /mycustomalias
```

### 🔸 Response

- **308 Redirect** to the original URL if found.
- **404 Not Found** if alias doesn't exist.
- **Blacklist Safety Check:** If the destination URL is blacklisted or unreachable, a custom error page is shown.

---

## 🗂 Other Routes

- `/` – Serves the main frontend HTML interface (`index.html`)
- `/index.js`, `/styles.css` – Static frontend assets from the `templates/` directory

---

## File Structure (Simplified)

```
LibreShortURL/
├── app.py
├── config.env
├── db/
├── docs/
├── templates/
├── sql_db.py
├── setup.py
├── run.sh
├── venv/
├── WORDS_NOVA/
└── README.md
```

---

## 🛡 Blacklist Handling

Blocked or suspicious short names are rejected based on terms in:

```bash
./db/blacklist-urls.txt
```

---

## Notes

- All names must be **< 18 characters**
- Short name must **not** match any blacklisted word
- URL status is validated before redirecting
- Add server Domain with `http://` or `https://` 