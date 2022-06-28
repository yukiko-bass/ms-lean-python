# ms-lean-python

# env

- Windows 11 WSL2 on Ubuntu

# install

- 3.8.10(2022/06/28時点) のインストール
```bash
$ sudo apt-get update
$ sudo apt-get install python3.10
$ python3 --version
Python 3.8.10
```

- 3.10 のインストール

[UbuntuにPython 3.10をインストールする方法](https://codechacha.com/ja/python-install-python-3-10/)

```
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt install python3.10
$ python3.10 --version
Python 3.10.5
```

- 3.10 のpipが古いのでアップデートする
[Pip is not working for Python 3.10 on Ubuntu](https://stackoverflow.com/questions/69503329/pip-is-not-working-for-python-3-10-on-ubuntu)

```
$ curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10
```

- source からインストール

[Ubuntu環境のPython](https://www.python.jp/install/ubuntu/index.html)


# VSCode の拡張機能

- [Python 拡張機能のインストール](https://docs.microsoft.com/ja-jp/learn/modules/python-install-vscode/5-exercise-install-python-extension?pivots=linux)

- [2021年Python開発リンター導入のベストプラクティス](https://zenn.dev/yhay81/articles/yhay81-202102-pythonlint)

  - black のインストール
  ```
  $ /bin/python3.10 -m pip install -U black
  ```
  - Flake8 のインストール
  ```
  $ /bin/python3.10 -m pip install -U flake8
  ```

## error解消

- ModuleNotFoundError: No module named 'distutils.util'

```
# 3.8
$ sudo apt-get install python3-distutils
# 2.10
$ sudo apt-get install python3.10-distutils
```