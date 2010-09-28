from setuptools import setup, find_packages

setup(
		name="indygo",
		version="1.0",
		author="Conrad Indiono",
		description="A complete Django environment ready for deployment",
		packages=find_packages(),
		install_requires=["PasteScript"],
		zip_safe=False,
		package_data={'':['*.*']},
		include_package_data=True,
		entry_points = {
			'paste.paster_create_template':
				['indygo = indygo:IndyGoTemplate'],
			'console_scripts':
				#['rst2pdf = project_a.tools.pdfgen [PDF]',
				#'rst2html = project_a.tools.htmlgen'],
				[]
		},
		eager_resources = ["indygo/template/media/site/css/ie.css"]
)
