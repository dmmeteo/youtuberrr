# Gemini Context: Youtuberrr Project

These are my notes for working on the project.

## Project Goal

Create a web application for downloading YouTube videos and playlists. The project name is `youtuberrr`.

## Key Technologies

- **Backend Core**: `yt-dlp`. This is the primary tool for downloading. My task is to call it from Python (likely via `subprocess`) with the necessary arguments.
- **Backend Framework**: `Litestar`. I will use it to create the web server, routes, and handle requests. It will serve as a wrapper for `yt-dlp`.
- **Frontend**:
  - `HTMX`: For creating a dynamic interface without page reloads. I need to generate HTML responses with the appropriate `hx-*` attributes.
  - `Tailwind CSS`: For styling. I will add Tailwind classes directly into the HTML templates.

## Project Structure

```
youtuberrr/
├── app/
│   ├── __init__.py
│   ├── main.py             # App entry point: creates and configures the Litestar app
│   ├── routers/
│   │   ├── __init__.py
│   │   └── web.py          # Handles user-facing web routes (e.g., serving the form)
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── download.py     # Pydantic models for request data (e.g., URL)
│   ├── services/
│   │   ├── __init__.py
│   │   └── downloader.py   # Business logic for calling yt-dlp
│   ├── static/
│   │   └── css/
│   │       └── style.css   # Compiled Tailwind CSS will go here
│   └── templates/
│       ├── base.html       # Base template with head, body, CSS/JS links
│       └── index.html      # Main page content, extends base.html
├── .gitignore
├── pyproject.toml          # Project definition and dependencies for uv
├── package.json            # For managing frontend dependencies (Tailwind, HTMX)
└── tailwind.config.js
```

## Architecture

1.  **Interface**: Litestar serves the main page with an HTML form.
2.  **Form**: Includes a field for the URL (video/playlist) and download settings.
3.  **Interaction**: The form sends a request (e.g., `hx-post`) to a Litestar endpoint.
4.  **Processing**: The Litestar endpoint handler will:
    - Validate the URL.
    - Formulate the `yt-dlp` command based on the form data.
    - Run `yt-dlp` in a separate process.
5.  **Response**: Litestar returns an HTML fragment that HTMX will insert into the page to show the status (e.g., "Download started..." or "Error").

## Action Plan

1.  Set up the basic Litestar project structure.
2.  Create the main HTML template with the form.
3.  Integrate Tailwind CSS for basic styling.
4.  Create an endpoint in Litestar that accepts a POST request from the form.
5.  Implement the logic for calling `yt-dlp`.

## Future Improvements

*   **Cleanup Task:** Implement a background task (e.g., cron job) to periodically delete files from the `downloads` directory to save server space.
