from __future__ import division
import time
import serial
import Adafruit_PCA9685
import pygame
from pygame.locals import *


# Initialize the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

servo_min = 150  # Min pulse length out of 4096
servo_max = 250  # Max pulse length out of 4096


def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    pulse_length //= 4096     # 12 bits of resolution
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Serial port configuration
serial_port = '/dev/ttyAMA0'
baud_rate = 115200

ser = serial.Serial(serial_port, baud_rate)
print('Serial port initialized successfully.')

# Initialize Pygame
pygame.init()

# Set the path to the music folder
music_folder = '/home/bait0ng/Music'


# Function to play MP3 file
def play_music(file_name):
    sound = pygame.mixer.Sound(file_name)
    sound.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)




mp3_file = 'startup.wav'  # Replace with your actual MP3 file
play_music(f"{music_folder}/{mp3_file}")

pwm.set_pwm(0, 0, servo_min)
pwm.set_pwm(1, 0, servo_min)
pwm.set_pwm(2, 0, servo_min)
pwm.set_pwm(3, 0, servo_min)
pwm.set_pwm(4, 0, servo_min)
pwm.set_pwm(5, 0, servo_min)
pwm.set_pwm(10, 0, servo_min)
pwm.set_pwm(11, 0, servo_min)
pwm.set_pwm(12, 0, servo_min)
pwm.set_pwm(13, 0, servo_min)
pwm.set_pwm(14, 0, servo_min)
pwm.set_pwm(15, 0, servo_min)

try:
    print('Moving servo on channel 0, press Ctrl-C to quit...')
    while True:
   
        if ser.in_waiting > 0:
            try:
                # Read the data from the serial port
                data = ser.readline().decode('utf-8', errors='replace').rstrip()
                print(data)
                if data == "T1":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T1.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")
                    
                elif data == "T2":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T2.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T3":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_max)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_max)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T3.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T4":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T4.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T5":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_max)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_max)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_max)

                    mp3_file = 'T5.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T6":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_max)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_max)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_max)

                    mp3_file = 'T6.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T7":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T7.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T8":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T8.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T9":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T9.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T10":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T10.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T11":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T11.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T12":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_max)
                    pwm.set_pwm(13, 0, servo_max)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_max)

                    mp3_file = 'T12.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T13":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_max)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_max)
                    pwm.set_pwm(13, 0, servo_max)
                    pwm.set_pwm(14, 0, servo_max)
                    pwm.set_pwm(15, 0, servo_max)

                    mp3_file = 'T13.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "14":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_max)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_max)
                    pwm.set_pwm(14, 0, servo_max)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T14.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T15":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_max)
                    pwm.set_pwm(11, 0, servo_max)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_max)
                    pwm.set_pwm(15, 0, servo_max)

                    mp3_file = 'T15.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T16":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_max)
                    pwm.set_pwm(12, 0, servo_max)
                    pwm.set_pwm(13, 0, servo_max)
                    pwm.set_pwm(14, 0, servo_max)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T16.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T17":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_max)
                    pwm.set_pwm(12, 0, servo_max)
                    pwm.set_pwm(13, 0, servo_max)
                    pwm.set_pwm(14, 0, servo_max)
                    pwm.set_pwm(15, 0, servo_max)

                    mp3_file = 'T17.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T18":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_max)
                    pwm.set_pwm(12, 0, servo_max)
                    pwm.set_pwm(13, 0, servo_max)
                    pwm.set_pwm(14, 0, servo_max)
                    pwm.set_pwm(15, 0, servo_max)

                    mp3_file = 'T18.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T19":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_max)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_max)
                    pwm.set_pwm(13, 0, servo_max)
                    pwm.set_pwm(14, 0, servo_max)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T19.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T20":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T20.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T21":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T21.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T22":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T22.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T23":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T23.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T24":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_max)
                    pwm.set_pwm(12, 0, servo_max)
                    pwm.set_pwm(13, 0, servo_max)
                    pwm.set_pwm(14, 0, servo_max)
                    pwm.set_pwm(15, 0, servo_max)

                    mp3_file = 'T24.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T25":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T25.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T26":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T26.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T27":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T27.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T28":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T28.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T29":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T29.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T30":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T30.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T31":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T31.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T32":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_max)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_max)
                    pwm.set_pwm(14, 0, servo_max)
                    pwm.set_pwm(15, 0, servo_max)

                    mp3_file = 'T32.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T33":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T33.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T34":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T34.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T35":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T35.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T36":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T36.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T37":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T37.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T38":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_max)
                    pwm.set_pwm(12, 0, servo_max)
                    pwm.set_pwm(13, 0, servo_max)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T38.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T39":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_max)
                    pwm.set_pwm(12, 0, servo_max)
                    pwm.set_pwm(13, 0, servo_max)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T39.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T40":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T40.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T41":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T41.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T42":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_max)
                    pwm.set_pwm(11, 0, servo_max)
                    pwm.set_pwm(12, 0, servo_max)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T42.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T43":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T43.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "T44":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T44.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "EN1":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'A.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "EN2":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'B.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "EN3":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'C.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "EN4":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'D.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "EN5":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'E.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "EN6":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'F.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "EN7":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'G.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "EN8":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'H.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "EN9":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'I.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "EN10":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'J.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "EN11":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'K.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "EN12":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'L.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "EN13":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'M.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "EN14":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'N.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "EN15":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'O.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "EN16":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'P.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "EN17":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'Q.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "EN18":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'R.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "EN19":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "EN20":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'T.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "EN21":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'U.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "22EN":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'V.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "EN23":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'W.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "EN24":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'X.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "EN25":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'Y.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "EN26":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'Z.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "N0":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_max)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_max)
                    pwm.set_pwm(14, 0, servo_max)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'N0.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "N1":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_max)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'N1.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "N2":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_max)
                    pwm.set_pwm(11, 0, servo_max)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'N2.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "N3":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_max)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_max)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'N3.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "N4":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_max)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_max)
                    pwm.set_pwm(13, 0, servo_max)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'N4.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "N5":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_max)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_max)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'N5.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "N6":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_max)
                    pwm.set_pwm(11, 0, servo_max)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_max)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'N6.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "N7":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_max)
                    pwm.set_pwm(11, 0, servo_max)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_max)
                    pwm.set_pwm(14, 0, servo_max)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'N7.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "N8":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_max)
                    pwm.set_pwm(11, 0, servo_max)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_max)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'N8.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "N9":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_max)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_max)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'N9.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S1":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S1.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S2":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S2.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S3":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S3.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S4":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S4.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S5":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S5.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S6":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S6.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S7":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S7.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S8":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S8.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S9":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_max)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S9.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S10":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S10.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S11":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_max)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S11.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S12":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S12.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S13":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_max)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S13.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S14":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S14.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S15":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_max)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S15.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S16":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S16.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S17":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_max)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S17.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S18":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S18.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S19":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_max)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S19.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S20":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S20.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S21":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_max)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S21.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S22":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S22.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S23":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_max)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S23.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S24":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S24.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S25":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S25.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S26":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S26.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S27":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_max)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S27.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S28":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S28.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S29":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_max)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S29.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S30":
                    pwm.set_pwm(0, 0, servo_max)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_max)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S30.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S31":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S31.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S32":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S32.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S33":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S33.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S34":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S34.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S35":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_max)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S35.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S36":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_max)
                    pwm.set_pwm(5, 0, servo_max)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S36.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S37":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_max)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S37.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                elif data == "S38":
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_max)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)

                    mp3_file = 'S38.wav'  # Replace with your actual MP3 file
                    play_music(f"{music_folder}/{mp3_file}")

                else:
                    pwm.set_pwm(0, 0, servo_min)
                    pwm.set_pwm(1, 0, servo_min)
                    pwm.set_pwm(2, 0, servo_min)
                    pwm.set_pwm(3, 0, servo_min)
                    pwm.set_pwm(4, 0, servo_min)
                    pwm.set_pwm(5, 0, servo_min)
                    pwm.set_pwm(10, 0, servo_min)
                    pwm.set_pwm(11, 0, servo_min)
                    pwm.set_pwm(12, 0, servo_min)
                    pwm.set_pwm(13, 0, servo_min)
                    pwm.set_pwm(14, 0, servo_min)
                    pwm.set_pwm(15, 0, servo_min)
                    
            except UnicodeDecodeError as e:
                print(f"Error decoding data: {e}")

except KeyboardInterrupt:
    print("\nTerminated by user.")

finally:
    # Close the serial port
    ser.close()
    print("Serial port closed.")