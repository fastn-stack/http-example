# HTTP Test


- [ ] arpita: http JSON data is list
- [ ] arpita: ftd.input, ftd.checkbox
- [ ] abrark: endpoint proxying not working
- [ ] arpita: finish off the examples

# FPM

Install FPM and then run:

```sh
fpm serve --edition 2022
```



# Install Python Stuff

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

flask --app app --debug run --port 8002
```
