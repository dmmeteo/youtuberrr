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
    git clone https://github.com/dmmeteo/youtuberrr.git
    cd youtuberrr
    ```

3.  **Install dependencies:**
    ```bash
    make install
    ```

4.  **Run the application:**
    ```bash
    make run
    ```

## Running with Docker

You can also run the application using Docker. This is the recommended method for production or if you prefer not to manage Python dependencies locally.

### Option 1: Using Docker

This method uses the official pre-built image from Docker Hub.

1.  **Pull the image:**
    ```bash
    docker pull dmmeteo/youtuberrr:main
    ```

2.  **Run the container:**
    This command starts the application and maps port `8000` on your host to the container. It also creates a `downloads` directory in your current working directory and mounts it to the container to store the downloaded videos.
    ```bash
    docker run -d -p 8000:8000 -v "$(pwd)/downloads:/app/downloads" --name youtuberrr dmmeteo/youtuberrr:main
    ```

3.  Open your browser and navigate to `http://localhost:8000`.

### Option 2: Using Docker Compose

This method builds the image locally and runs it using the configuration in the `compose.yaml` file.

1.  **Build and run the container:**
    ```bash
    docker compose up --build -d
    ```

2.  Open your browser and navigate to `http://localhost:8000`.

To stop the container, run:
```bash
docker compose down
```