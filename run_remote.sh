HOST=pi@raspberrypi.local
PROJECT=${PWD##*/}

ssh $HOST -t mkdir -p  Desktop/$PROJECT
scp -r $PWD/*.* $HOST:Desktop/$PROJECT
ssh $HOST -t python Desktop/$PROJECT/app.py
