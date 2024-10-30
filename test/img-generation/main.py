import requests
import random
import os
from uuid import uuid4
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "src"))
)

from utils import *
from config import *


def get_verbose():
    return True


def get_image_model():
    # "v1" , "v2" , "v2-beta" , "v3" (DALL-E) , "lexica" , "prodia", "simurg", "animefy", "raava", "shonin"
    # v2 em manutenção
    # v3 (DALL-E) gerou as imagens mais bonitas!
    return "v3"


def get_image_style():
    return "Highly detailed style with a focus on realism. Dont generate any living creatures, humans, aliens, spaceships."


def get_prompt():
    prompts = [
        "A breathtaking cosmic landscape illustrating the enigmatic nature of dark matter, with swirling galaxies and shimmering stars, emphasizing the mysteries of dark matterr: recent discoveries and their implications for our understanding of the universe.",
        "An awe-inspiring visualization of dark matter's gravitational effects on a distant galaxy, showcasing the intricate dance of celestial bodies and the profound implications for our understanding of the universe.",
        "A dramatic depiction of scientists in a high-tech laboratory, passionately discussing the latest findings on dark matter, highlighting the excitement and urgency of their research in exploring the mysteries of dark matter: recent discoveries and their implications for our understanding of the universe.",
        "An ethereal representation of dark matter as a vast, invisible web connecting galaxies, illustrating the unseen forces that shape our universe and the recent discoveries that challenge our understanding of dark matter.",
        "A captivating image of a cosmic collision, where dark matter plays a crucial role, revealing the dynamic interactions between galaxies and the implications for our understanding of the universe.",
        "A stunning visualization of a dark matter halo surrounding a galaxy, with vibrant colors and intricate patterns, symbolizing the hidden structures that influence the cosmos and the recent discoveries related to dark matter.",
        "An imaginative portrayal of a futuristic observatory peering into the depths of space, searching for clues about dark matter, reflecting the relentless pursuit of knowledge in exploring the mysteries of dark matter: recent discoveries and their implications for our understanding of the universe.",
        "A mesmerizing cosmic scene featuring dark matter's influence on the cosmic microwave background radiation, illustrating the profound implications of recent discoveries for our understanding of the universe.",
        "An artistic interpretation of dark matter as a mysterious force, with swirling colors and abstract shapes, representing the unknown aspects of dark matter: recent discoveries and their implications for our understanding of the universe.",
        "A thought-provoking image of a black hole surrounded by dark matter, capturing the tension between known and unknown in the universe and the implications of recent discoveries.",
        "A vivid representation of a galaxy cluster, showcasing the gravitational lensing effects of dark matter, emphasizing the beauty and complexity of the universe and the recent discoveries related to dark matter.",
        "An inspiring scene of a diverse group of scientists collaborating on dark matter research, symbolizing the global effort to unravel the mysteries of dark matter: recent discoveries and their implications for our understanding of the universe.",
        "A striking visualization of dark matter's role in the formation of large-scale structures in the universe, illustrating the intricate web of galaxies and the implications of recent discoveries.",
        "A dramatic cosmic event, such as a supernova, with dark matter subtly influencing the outcome, highlighting the interconnectedness of phenomena in exploring the mysteries of dark matter: recent discoveries and their implications for our understanding of the universe.",
        "An imaginative depiction of a time traveler witnessing the birth of the universe, with dark matter as a key player in the cosmic drama, reflecting on the implications of recent discoveries.",
        "A captivating image of a cosmic void, illustrating the absence of visible matter yet filled with dark matter, symbolizing the hidden aspects of the universe and the recent discoveries that challenge our understanding.",
        "A dynamic representation of a particle collider experiment, where scientists are probing the nature of dark matter, showcasing the cutting-edge technology and excitement in exploring the mysteries of dark matter: recent discoveries and their implications for our understanding of the universe.",
        "An enchanting visualization of dark matter interacting with visible matter in a vibrant galaxy, highlighting the delicate balance and the implications of recent discoveries for our understanding of the universe.",
        "A thought-provoking image of a cosmic map, with dark matter highlighted as a crucial component, illustrating the vastness of the universe and the recent discoveries that reshape our understanding.",
        "A stunning portrayal of a nebula, with dark matter subtly influencing its formation, capturing the beauty and complexity of cosmic phenomena in exploring the mysteries of dark matter: recent discoveries and their implications for our understanding of the universe.",
        "An evocative scene of a scientist gazing at the night sky, contemplating the mysteries of dark matter and the implications of recent discoveries for our understanding of the universe.",
        "A vibrant cosmic tapestry depicting the interplay between dark matter and dark energy, illustrating the fundamental forces that shape our universe and the implications of recent discoveries.",
        "A dramatic image of a galaxy being distorted by dark matter's gravitational pull, showcasing the unseen forces at work in exploring the mysteries of dark matter: recent discoveries and their implications for our understanding of the universe.",
        "An imaginative representation of a futuristic spacecraft exploring dark matter regions in space, symbolizing humanity's quest for knowledge and the implications of recent discoveries.",
        "A captivating visualization of dark matter's role in cosmic evolution, with galaxies forming and interacting under its influence, highlighting the profound implications for our understanding of the universe.",
        "A striking image of a cosmic web, with dark matter filaments connecting clusters of galaxies, illustrating the large-scale structure of the universe and the recent discoveries that enhance our understanding.",
        "An inspiring scene of a public lecture on dark matter, with an enthusiastic audience engaged in the mysteries of dark matter: recent discoveries and their implications for our understanding of the universe.",
        "A mesmerizing depiction of a starry night sky, with dark matter subtly woven into the fabric of the cosmos, inviting viewers to ponder the mysteries and recent discoveries that shape our understanding of the universe.",
    ]

    return random.choice(prompts)


url = f"https://hercai.onrender.com/{get_image_model()}/text2image?prompt={get_image_style()},{get_prompt()}"

r = requests.get(url)
parsed = r.json()
image_url = parsed["url"]

if get_verbose():
    info(f" => Generated Image: {image_url}")

os.makedirs(os.path.join(ROOT_DIR, "img-generation", "output", get_image_model()), exist_ok=True)

image_path = os.path.join(
    ROOT_DIR, "img-generation", "output", get_image_model(), str(uuid4()) + ".png"
)

with open(image_path, "wb") as image_file:
    # Write bytes to file
    image_r = requests.get(image_url)

    image_file.write(image_r.content)

if get_verbose():
    info(f' => Wrote Image to "{image_path}"\n')
