Installation
pip install promptpay

# or
git clone https://github.com/karndiy/pypromtpay
cd promptpay
python setup.py install
Usage
Library
from promptpay import qrcode

# generate a payload
id_or_phone_number = "0892343728"
payload = qrcode.generate_payload(id_or_phone_number)
payload_with_amount = qrcode.generate_payload(id_or_phone_number, 1.23)

# export to PIL image
img = qrcode.to_image(payload)

# export to file
qrcode.to_file(payload, "./qrcode-0892343728.png")
qrcode.to_file(payload_with_amount, "/Users/joe/Downloads/qrcode-0892343728.png") 
CLI
python -m promptpay qrcode --id="0892343728"
python -m promptpay qrcode --id="0892343728" --file="./qrcode-cli.png"
python -m promptpay qrcode --id="0892343728" --show=true
python -m promptpay qrcode \
  --id="0892343728" \
  --amount=2.34 \
  --file="/Users/joe/Downloads/qrcode-cli-with-amount.png"
Development
# Conda env
conda create --name promptpay3.10 python=3.10.4
conda activate promptpay3.10
conda create --name promptpay3.7 python=3.7.13
conda activate promptpay3.7
conda remove --name promptpay3.10 --all

# others
pip install -r requirements.txt
pip install -r requirements-dev.txt
python -m flake8 --ignore=E501 promptpay tests
python -m pytest tests --cov=./ --cov-report=xml
pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U
python -m pip list --format=freeze > requirements-tmp.txt
pip install libscrc==
pip install Pillow==
pip install promptpay
pip install promptpay==1.1.7
pip install .
pip install --force-reinstall promptpay