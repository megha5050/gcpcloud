FROM tiangolo/uwsgi-nginx-flask

# Create app directory

 
WORKDIR /usr/src/megha 

COPY serviceapp1.py . 
EXPOSE 4444

 
RUN pip install requests

 
CMD [ "python", "serviceapp1.py" ]

