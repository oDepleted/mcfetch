import pytest

from mcfetch import FetchPlayer, FetchPlayer2
from requests_cache import CachedSession


class BaseTestFetchPlayer:
    def setup_method(self):
        self.existing_player: FetchPlayer = \
            self.get_existing_player_instance()

        self.non_existing_player: FetchPlayer = \
            self.get_non_existing_player_instance()


    def test_fetch_player_init(self):
        assert self.existing_player

    @pytest.mark.asyncio
    async def test_fetch_player_uuid_by_existing_player(self):
        assert self.existing_player.uuid is not None

    @pytest.mark.asyncio
    async def test_fetch_player_name_by_existing_player(self):
        assert self.existing_player.name is not None

    @pytest.mark.asyncio
    async def test_fetch_player_name_by_non_existing_player(self):
        assert self.non_existing_player.name is None

    @pytest.mark.asyncio
    async def test_fetch_player_skin_url_by_existing_player(self):
        assert self.existing_player.skin_url is not None

    @pytest.mark.asyncio
    async def test_fetch_player_skin_url_by_non_existing_player(self):
        assert self.non_existing_player.skin_url is None

    @pytest.mark.asyncio
    async def test_fetch_player_skin_texture_by_existing_player(self):
        assert self.existing_player.skin_texture is not None

    @pytest.mark.asyncio
    async def test_fetch_player_skin_texture_by_non_existing_player(self):
        assert self.non_existing_player.skin_texture is None



class TestFetchPlayerByName(BaseTestFetchPlayer):
    def get_existing_player_instance(self):
        return FetchPlayer(name='Notch')

    def get_non_existing_player_instance(self):
        return FetchPlayer(name='Bitch')


class TestFetchPlayerByUUID(BaseTestFetchPlayer):
    def get_existing_player_instance(self):
        return FetchPlayer(uuid='069a79f444e94726a5befca90e38aaf5')

    def get_non_existing_player_instance(self):
        return FetchPlayer(uuid='abcdefghijklmnopqrstuvwxyz')



session = CachedSession(cache_name='.cache/test', expire_after=60)

class TestFetchPlayerByNameWithCaching(BaseTestFetchPlayer):
    def get_existing_player_instance(self):
        return FetchPlayer(name='Notch', requests_obj=session)

    def get_non_existing_player_instance(self):
        return FetchPlayer(name='Bitch', requests_obj=session)


class TestFetchPlayerByUUIDWithCaching(BaseTestFetchPlayer):
    def get_existing_player_instance(self):
        return FetchPlayer(
            uuid='069a79f444e94726a5befca90e38aaf5', requests_obj=session)

    def get_non_existing_player_instance(self):
        return FetchPlayer(
            uuid='abcdefghijklmnopqrstuvwxyz', requests_obj=session)


class TestFetchPlayerDynamicallyByNameWithCaching(BaseTestFetchPlayer):
    def get_existing_player_instance(self):
        return FetchPlayer2(
            'Notch', requests_obj=session)

    def get_non_existing_player_instance(self):
        return FetchPlayer2(
            'Bitch', requests_obj=session)


class TestFetchPlayerDynamicallyByUUIDWithCaching(BaseTestFetchPlayer):
    def get_existing_player_instance(self):
        return FetchPlayer2(
            '069a79f444e94726a5befca90e38aaf5', requests_obj=session)

    def get_non_existing_player_instance(self):
        return FetchPlayer2(
            'abcdefghijklmnopqrstuvwxyz', requests_obj=session)
