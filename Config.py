import os
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()
env_path = Path('.') / 'vars.env'
load_dotenv(dotenv_path=env_path)

fontConfig = ['Montserrat', 16]
backgroundColour = '#80c1ff'
darkBlue = '#1da1f2'
height = 600
width = 700



