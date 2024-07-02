step:
1. git clone https://github.com/QuinStore/ubot-gayontwann
- username : QuinStore 
- pass : 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

1. sudo apt update && sudo apt upgrade -y - (awal deploy aja)
2. sudo apt install python3.10-venv ffmpeg -y - (awal deploy aja)
3. cd ubot-gayontwann
4. screen -S ubot-gayontwann
5. python3 -m venv wannfyy - (awal deploy aja)
6. source wannfyy/bin/activate
7. pip install --no-cache-dir -r requirements.txt - (awal deploy aja)
8. cp sample.env .env (awal deploy aja)
9. nano .env (isi varsnya, ctrl + s buat save, ctrl + x buat exit nano)
10. bash start
