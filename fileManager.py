import pickle

# Name of the default file that contain the back-up
FILE = 'data.file'

def save(data, filename=FILE):
	""" Save the data object in filename """
	with open(filename, 'wb') as output_data:
		pickle.dump(data, output_data, pickle.HIGHEST_PROTOCOL)

def load(filename):
	""" Return the data object saved in filename """
	with open(filename, 'rb') as input_data:
		return pickle.load(input_data)
