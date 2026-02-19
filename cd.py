import cloudinary
import cloudinary.uploader
import cloudinary.api
from dotenv import load_dotenv
import os
load_dotenv()


cloudinary.config(
    cloud_name='dtefc9vkq',
    api_key='724627291312128',
    api_secret='4Ss2oD4GIkdGAGJ7ZZDszlsY6Y4'
)

response = cloudinary.uploader.upload(
    r"C:\Users\ARYAN\OneDrive\画像\Screenshots\Screenshot 2026-02-13 002912.png",
)

print(response["secure_url"])

