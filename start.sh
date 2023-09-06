if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Jkdeveloper01/TOM-2BOT.git /TOM-2BOT
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /TOM-2BOT
fi
cd /TOM-2BOT
pip3 install -U -r requirements.txt
echo "Starting...."
python3 bot.py
