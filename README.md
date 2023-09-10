# Docker

Прежде чем вы сможете установить Docker Engine, вы должны сначала убедиться, что все конфликтующие пакеты удалены.
## 1. Запустите следующую команду, чтобы удалить все конфликтующие пакеты:

    $ for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done



## 2. Обновите и установите дополнительные пакеты:
    sudo apt-get update
    sudo apt-get install ca-certificates curl gnupg

## 3. Обмен клюами с репозиториями:

    sudo install -m 0755 -d /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    sudo chmod a+r /etc/apt/keyrings/docker.gpg

## 4. Команда для настройки репозитория:

    echo \
      "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
      "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
      sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update

## 5. Обновите список репозиториев:

    sudo apt-get update


