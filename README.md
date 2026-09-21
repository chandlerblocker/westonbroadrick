# Weston Broadrick Studio — website

Replaces the Squarespace site at westonbroadrick.com. Plain HTML, hosted free on GitHub Pages.

## What's here
| Path | What it is |
|---|---|
| `index.html`, `projects/…`, `contact/` | The pages. Addresses match the old Squarespace site so existing links still work. |
| `_src/build.py` | Writes every page. **Edit copy, projects, and photo order here**, then run `python3 _src/build.py`. |
| `css/site.css` | The look: colors and fonts at the top. |
| `js/site.js` | Header scroll, phone menu, fade-ins, photo viewer. |
| `images/` | Web-sized photos (`-sm` = phone size). `images/original/` = full-res Squarespace downloads, kept locally only (not uploaded). |
| `CNAME` | Tells GitHub which domain this site answers to. |

## Adding a project
1. Drop photos into `images/` (JPEG, ~2000px on the long side).
2. Add them to `images.json` (width/height) and an entry to `PROJECTS` in `_src/build.py`.
3. Run `python3 _src/build.py`, then commit and push.

## Going live (one time)
1. **GitHub:** create an empty repo (no README), then push this folder to it.
2. **Repo → Settings → Pages:** Source = *Deploy from a branch*, branch `main`, folder `/ (root)`. Custom domain = `www.westonbroadrick.com`.
3. **Squarespace → Domains → westonbroadrick.com → DNS:**
   - Delete the Squarespace Defaults preset records (the four `198.x` A records and `www → ext-sq.squarespace.com`).
   - Add four **A** records, host `@`: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - Add **CNAME**, host `www` → `<github-username>.github.io`
   - **Do not touch** the Google MX records (`aspmx.l.google.com` …) or the `google-site-verification` TXT records. They run Weston's email.
4. Wait for DNS (minutes to a few hours), then tick **Enforce HTTPS** in Settings → Pages.
5. Only after the new site is confirmed live: cancel the Squarespace **website** plan. Keep the **domain** registration and its auto-renew. The domain is billed separately and must not lapse.
