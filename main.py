import sys
import urllib.request
import urllib.error
import json

if len(sys.argv) > 1 and sys.argv[1]:
    username = sys.argv[1]
    url = f"https://api.github.com/users/{username}/events"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read())
    except urllib.error.HTTPError as error:
        if error.code == 404:
            print(f"No se encontró el usuario de GitHub '{username}'.", file=sys.stderr)
        else:
            print(f"Error de la API de GitHub (HTTP {error.code}).", file=sys.stderr)
        sys.exit(1)
    except (urllib.error.URLError, TimeoutError) as error:
        print(f"No se pudo conectar con la API de GitHub: {error.reason if isinstance(error, urllib.error.URLError) else 'tiempo de espera agotado'}.", file=sys.stderr)
        sys.exit(1)

    for event in data:
        event_type = event.get("type")
        repo = event.get("repo", {}).get("name", "unknown repository")
        payload = event.get("payload", {})

        if event_type == "PushEvent":
            commits = payload.get("size", 0)
            message = f"Pushed {commits} commits to {repo}"
        elif event_type == "IssuesEvent":
            if payload.get("action") == "opened":
                message = f"Opened a new issue in {repo}"
            else:
                message = f"Updated an issue in {repo}"
        elif event_type == "WatchEvent":
            message = f"Starred {repo}"
        else:
            message = f"{event_type} in {repo}"

        print(f"- {message}")