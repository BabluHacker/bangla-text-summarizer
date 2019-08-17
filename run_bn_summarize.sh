#!/bin/bash
# My first script

echo "starting summarizer...."

source venv/bin/activate

PATH=$PATH:/home/ubuntu/technocratsProjects/bangla-text-summarizer/venv/bin/python:/home/ubuntu/technocratsProjects/bangla-text-summarizer/ven$
export PATH
#gunicorn -w 14 -b 127.0.0.1:3000 app:app --timeout 300 --log-file logs --daemon
gunicorn -b 127.0.0.1:5000 app:app --timeout 300
echo "stopping summarizer"