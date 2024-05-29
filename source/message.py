import wave
from audio import Audio
from character import Character

class Message:

    # maps each letter to its active segments of a virtual 14-segment display
    letters = {
        "A": "11101111000000",
        "B": "11110001010010",
        "C": "10011100000000",
        "D": "11110000010010",
        "E": "10011110000000",
        "F": "10001110000000",
        "G": "10111101000000",
        "H": "01101111000000",
        "I": "10010000010010",
        "J": "01111000000000",
        "K": "00001110001001",
        "L": "00011100000000",
        "M": "01101100101000",
        "N": "01101100100001",
        "O": "11111100000000",
        "P": "11001111000000",
        "Q": "11111100000001",
        "R": "11001111000001",
        "S": "10110111000000",
        "T": "10000000010010",
        "U": "01111100000000",
        "V": "00001100001100",
        "W": "01101100000101",
        "X": "00000000101101",
        "Y": "01110111000000",
        "Z": "10010000001100"
    }

    def __init__(self, message_text):
        self.message_text = message_text


    def __render_message(self, audio_channels, char_duration):
        self.char_audio_samples = {}

        for character in set(self.message_text):
            wav_character = Character(self.letters.get(character))
            self.char_audio_samples[character] = wav_character.render_char(audio_channels, char_duration)
            del wav_character


    def encrypt(self, carrier_audio_path, output_path, char_duration=1):
        with wave.open(carrier_audio_path, 'rb') as f:
            audio_channels = f.getparams().nchannels

        self.__render_message(audio_channels, char_duration)

        message_samples = []
        for char in self.message_text:
            message_samples.append(self.char_audio_samples[char])

        message_audio = Audio(message_samples)
        message_audio.overlay_wavs("song.wav", output_path)
