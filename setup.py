from setuptools import setup, find_packages 

with open('README.md', 'r') as f:
	long_description = f.read()

setup(
	name ='asyncimg', 
	version ='1.0.1', 
	author ='Shahriyar Alam', 
	author_email ='mdshahriyaralam552@gmail.com', 
	url ='https://github.com/shahprog/cmdline', 
	description ='An async image manipulation lib. Can be used for discord.', 
	long_description = long_description, 
	long_description_content_type ="text/markdown", 
	license ='MIT', 
	packages = find_packages(), 
	classifiers =( 
		"Programming Language :: Python :: 3", 
		"License :: OSI Approved :: MIT License", 
		"Operating System :: OS Independent",
	), 
	keywords ='Pillow addon, pillow lib, discord image lib, discord image commands, discord image manipulation', 
	install_requires = ['Pillow==8.0.2',],
	zip_safe = False
) 
