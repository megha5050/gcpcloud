FROM tiangolo/uwsgi-nginx-flask

# Create app directory

 
WORKDIR /usr/src/megha 

COPY serviceapp2.py . 
EXPOSE 4444

 
RUN pip install requests


 
CMD [ "python", "serviceapp2.py" ]

