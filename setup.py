from setuptools import setup

setup(
    name="python_studies",
    description="Projeto para estudos com Python 💙🤖",
    install_requires=[
        "parsel==1.6.0",
        "requests==2.24.0",
        "pymongo==3.11.0",
        "python-decouple==3.3",
        "rich==12.5.1"
    ],
    # setup_requires=["pytest-runner"],
    # tests_require=["pytest"],
    # entry_points={
    #     "console_scripts": [
    #         "tech-news-collector=tech_news.menu:collector_menu",
    #         "tech-news-analyzer=tech_news.menu:analyzer_menu",
    #     ],
    # },
)
