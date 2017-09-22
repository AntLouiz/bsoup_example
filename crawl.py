import json
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag as bs4_Tag
from pprint import pprint
from settings import HEADER
from utils import (
	get_next_page,
	get_recipe_details,
	get_search_url,
	serialize_recipe,
	save_recipes,
)

# recipe = str(input("Insira o nome de uma receita: "))
recipe = 'empadao'
recipes_json = {}

search_page = get_search_url(recipe)

page = requests.get(search_page, headers=HEADER)

base_soup = BeautifulSoup(page.text, 'html.parser')

recipe_page_soup = base_soup
# while True:
if recipe_page_soup:
	recipe_page_soup = get_next_page(recipe_page_soup)

	if not recipe_page_soup:
		# break
		pass

	recipes_box_soup = recipe_page_soup.find('div', attrs={'class':'listing box'})

	for recipe_soup in recipes_box.find_all(attrs={'class':'box-hover'}):

		if recipe_soup:
			data = serialize_recipe(recipe_soup)
			recipes_json[data['title']] = data

	save_recipes(recipes_json)