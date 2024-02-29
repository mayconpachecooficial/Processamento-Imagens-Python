from setuptools import setup, find_packages

setup(
    name='imageprocessor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',  # Adicione todas as dependências necessárias aqui
    ],
    author='Seu Nome',
    author_email='seuemail@example.com',
    description='Um pacote de processamento de imagens em Python.',
    license='MIT',
    keywords='imagem processamento',
    url='URL_do_repositório_no_GitHub',
)