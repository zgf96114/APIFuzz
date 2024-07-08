from setuptools import setup,find_packages

setup(name='ApiFuzz',
      version='1.0.0',
      description='API fuzzing test framework',
      author='Gazhou',
      author_email='gaofeng.zhou2@harman.com',
      license='GPL v3.0',
      #packages=['ApiFuzz'],
      project_urls={
      'Documentation': 'https://packaging.python.org/',
      'Source': 'https://github.com/',
      },
      install_requires=[
            "frida",
            "frida-tools"
      ],
      packages=find_packages(),
      package_data={'': ['*.*']},
      include_package_data=True,
      python_requires=">=3.8.0"
      )