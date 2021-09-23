echo "Cloning Repo...."
git clone https://github.com/ZauteKm/YT-PlayList-DL-Bot.git /YT-PlayList-DL-Bot
cd /YT-PlayList-DL-Bot
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
