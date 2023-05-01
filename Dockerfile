FROM python:3.11

ADD application.py .

COPY EcommerceApp.py .
COPY Catalog.py .
COPY Product.py .
COPY Constants.py .
COPY Order.py .
CMD ["python", "./application.py"]