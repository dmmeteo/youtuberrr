# Youtuberrr

A simple web application for downloading YouTube videos and playlists.

## About The Project

Youtuberrr is a lightweight web service designed for conveniently downloading content from YouTube. You can paste a link to a single video or an entire playlist, select your desired options, and get the files.

## Key Features

- Download single videos.
- Download entire playlists.
- Simple and clean web interface.
- Option to choose format and quality (in development).

## Tech Stack

- **Backend:**
  - **[Litestar](https://litestar.dev/)**: A modern and fast web framework for Python.
  - **[yt-dlp](https://github.com/yt-dlp/yt-dlp)**: A powerful command-line utility for downloading videos, which is the core of our application.

- **Frontend:**
  - **[HTMX](https://htmx.org/)**: Allows creating dynamic interfaces without writing complex JavaScript.
  - **[Tailwind CSS](https://tailwindcss.com/)**: A utility-first CSS framework for rapidly building modern designs.

## Getting Started

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd youtuberrr
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    litestar run
    ```