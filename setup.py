from setuptools import setup, find_packages

setup(
    name="cybertemp",                   
    version="0.0.9",                           
    packages=find_packages(),               
    install_requires=["logmagix", "requests"],           
    author="Sexfrance",                     
    author_email="bwuuuuu@gmail.com",   
    description="A Python wrapper for the CyberTemp temporary email service API",   
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sexfrance/cybertemp-wrapper",  
    classifiers=[                          
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Communications :: Email",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="email, temporary-email, disposable-email, api-wrapper, cybertemp",
    python_requires=">=3.8",
    project_urls={
        "Documentation": "https://cybertemp.xyz/api-docs",
        "Source": "https://github.com/sexfrance/cybertemp-wrapper",
        "Issues": "https://github.com/sexfrance/cybertemp-wrapper/issues",
    },
)
