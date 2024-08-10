from suno import SongsGen
from api_keys import SongsGen_


def generate_song(promp):
    i = SongsGen(SongsGen_)
    print(i.get_limit_left())
    i.save_songs(prompt=promp, output_dir='./output')

