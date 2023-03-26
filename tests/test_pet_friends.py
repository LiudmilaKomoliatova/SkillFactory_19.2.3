import os
from api import PetFriends
from settings import *


pf = PetFriends(base_url)


def test_get_api_key_valid_user(email=valid_email, password=valid_password):
	status, result = pf.get_api_key(email, password)
	assert status == 200
	assert 'key' in result


def test_get_pets_with_valid_user(pets_filter=''):
	_, auth_key = pf.get_api_key(valid_email, valid_password)
	status, result = pf.get_pets(auth_key, pets_filter)
	assert status == 200
	assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data(name='Zevs', animal_type='Cat', age='12', pet_photo='images\cat0.jpg'):
	_, auth_key = pf.get_api_key(valid_email, valid_password)
	pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
	status, result = pf.post_pets(auth_key, name, animal_type, age, pet_photo)
	assert status == 200
	assert result['name'] == name


def test_put_pets_with_valid_data(name='Super Zevs', animal_type='Super cotiara', age=100500):
	_, auth_key = pf.get_api_key(valid_email, valid_password)
	_, my_pets = pf.get_pets(auth_key, "my_pets")

	if len(my_pets['pets']) > 0:
		status, result = pf.put_pets(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
		assert status == 200
		assert result['name'] == name
	else:
		raise Exception("There is no my pets")
