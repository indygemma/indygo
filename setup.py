from setuptools import setup, find_packages

setup(
		name="indygo",
		version="1.0",
		author="Conrad Indiono",
		description="A complete Django environment ready for deployment",
		packages=find_packages(),
		install_requires=["PasteScript"],
		zip_safe=False,
		package_data={
			'indygo.template':[
				"compass/src/*",
				"media/site/css/*",
				"media/site/img/*",
				"media/site/js/*",
				"templates/site/*",
				"fixtures/development/*",
				"fixtures/production/*",
			]
		},
		include_package_data=True,
		entry_points = {
			'paste.paster_create_template':
				['indygo = indygo:IndyGoTemplate'],
			'console_scripts':
				['indygo = indygo.cmd:call_paster']
		},
)
