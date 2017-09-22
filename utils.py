from settings import START_URL

def get_search_url(recipe):
	search_page = '/busca.php?q='

	return "{0}{1}{2}".format(START_URL, search_page, recipe.lower())

def get_next_page(page_soup):
	next_button_soup = page_soup.find('a', attrs={'class':'next'})

	if next_button_soup:
		url = "{0}/{1}".format(START_URL, next_button_soup['href'])
		page = requests.get(url, headers=HEADER)
		next_page_soup = BeautifulSoup(page.text, 'html.parser')

		return next_page_soup

	return False

def get_recipe_details(recipe):
	raise NotImplementedError

def serialize_recipe(recipe_soup):
	data = {
		'url': None,
		'title': None,
		'likes': None,
		'rating': None,
		'author': None,
		'image_url': None
	}

	if isinstance(recipe_soup, bs4_Tag):
		# print(recipe_soup.a['href'])
		# print(recipe_soup.a.span.img['src'])
		# print(recipe_soup.a.div.h2.text)
		# print(
		# 	recipe_soup.find( attrs={'class': 'ratingbox current'}).text
		# )
		# print(
		# 	recipe_soup.find(attrs={'class': 'author'}).span.text
		# )
		# print(
		# 	recipe_soup.find(attrs={'class': 'like recipe_soup-info'}).text
		# )
		# print(
		# 	recipe_soup.find(attrs={'class': 'photo'})['src']
		# )

		data['url'] = "{0}{1}".format(START_URL, recipe_soup.a['href'])
		data['title'] = recipe_soup.a.div.h2.text
		data['likes'] = recipe_soup.find(attrs={'class': 'like recipe-info'}).text
		data['rating'] = recipe_soup.find( attrs={'class': 'ratingbox current'}).text
		data['author'] = recipe_soup.find(attrs={'class': 'author'}).span.text
		data['image_url'] = recipe_soup.find(attrs={'class': 'photo'})['src']

		return data

def save_recipes(data):
	with open('recipes.json', 'w') as file:
		json.dump(data, file, indent=4)