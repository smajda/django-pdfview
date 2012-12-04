from setuptools import setup

setup(
    name="django-pdfview",
    author="Jon Smajda",
    author_email="jon@smajda.com",
    description="A PDFView mixin for Django views using xhtml2pdf",
    version="0.1",
    packages=['pdfview'],
    install_requires=[
        "django >= 1.4",
        "xhtml2pdf",
    ],
)
