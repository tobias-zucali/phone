HOST=pi@raspberrypi.local
PROJECT=${PWD##*/}

# make sure folder is available
ssh $HOST -t mkdir -p  Desktop/$PROJECT

# copy files
scp -r $PWD/*.* $HOST:Desktop/$PROJECT
scp -r $PWD/* $HOST:Desktop/$PROJECT

# make sure soundcard is available
ssh $HOST -t jack_control start

# start
ssh $HOST -t python Desktop/$PROJECT/app.py
