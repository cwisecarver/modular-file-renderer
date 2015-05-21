import pytest

from mfr.extensions.audio import AudioRenderer


@pytest.fixture
def url():
    return 'test.mp3'


@pytest.fixture
def file_path():
    return {}


@pytest.fixture
def assets_url():
    return {}


@pytest.fixture
def extension():
    return {}


@pytest.fixture
def provider(url, file_path, assets_url, extension):
    return AudioRenderer(url, file_path, assets_url, extension)

class TestAudio:

    def test_render_audio(self, provider):
        html = provider.render()