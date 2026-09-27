from pathlib import Path
import subprocess

import imageio_ffmpeg
import pytest
from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import sync_playwright
from pytest_html import extras

from config import BASE_URL


def convert_video_to_mp4(video_path):
    video_path = Path(video_path)
    mp4_path = video_path.with_suffix(".mp4")
    ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()

    subprocess.run(
        [
            ffmpeg_path,
            "-y",
            "-i",
            str(video_path),
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            str(mp4_path),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    if video_path.exists():
        video_path.unlink()

    if mp4_path.exists():
        return mp4_path

    return video_path


@pytest.fixture
def page(request):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        videos_dir = Path("videos")
        videos_dir.mkdir(exist_ok=True)
        context = browser.new_context(
            ignore_https_errors=True,
            record_video_dir=str(videos_dir),
        )
        page = context.new_page()
        page.goto(BASE_URL)
        page.wait_for_load_state("load")

        request.node.video_path = None

        try:
            yield page
        finally:
            try:
                recorded_video = page.video
                context.close()
                if recorded_video:
                    video_path = Path(recorded_video.path())
                    request.node.video_path = convert_video_to_mp4(video_path)
            except Exception:
                request.node.video_path = None
            finally:
                browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    extra = list(getattr(report, "extras", []))

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page and not page.is_closed():
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)

            file_name = screenshots_dir / f"{item.name}.png"

            try:
                page.screenshot(path=str(file_name))
            except PlaywrightError:
                pass
            else:
                extra.append(extras.image(str(file_name)))

    if report.when == "teardown":
        video_path = getattr(item, "video_path", None)
        if video_path and Path(video_path).is_file():
            extra.append(
                extras.video(
                    str(video_path),
                    name=f"{item.name} execution",
                    mime_type="video/mp4",
                    extension="mp4",
                )
            )

    report.extras = extra