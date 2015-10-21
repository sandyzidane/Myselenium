def create_new_dir():
	input_file_name = 
	new_dir_name = 'e:\python\selenium\%s' %(file_name)

	if not os.path.exists(new_dir_name):
		os.makedirs(new_dir_name)

def set_up():
	driver = webdriver.Firefox()

def brower_open_final_url():
	driver.get(final_test_url)

def take_a_good_photo():
	dirver.get_screenshot_as_file(saved_file)
	shutil.move(saved_file, new_dir_name)