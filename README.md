# Coding Challenge Setup

## Forking the repository

More information on how to fork a repository can be found [here](https://docs.github.com/en/get-started/quickstart/fork-a-repo)

**NOTE**: forking the repository will show up publicly on your GitHub profile.
If you don't want to see [How to mirror the repository](#priv) section

### <a name="priv"></a>How to mirror the repository

GitHub does not allow a forked repository to be private. Therefore, a private
repository
needs to be created. Hence

- [create an empty private repository](https://docs.github.com/en/get-started/quickstart/create-a-repo)
- bare clone the public repository and mirror push it to the private repository
```
git clone --bare <link to the public repository>
cd <public_repository.git>
git push --mirror <link to the private repository>
```
- clean up
```
rm -rf <public_repository.git>
```

**NOTE**: make sure if you created a private repository please add [theodorosg](https://github.com/theodorosg) as a collaborator.

## Preconditions

### docker & docker-compose

- Linux: [how to install docker](https://docs.docker.com/engine/install/ubuntu/)
  , [how to install docker-compose](https://docs.docker.com/compose/install/#install-compose-on-linux-systems)
- Mac: [how to install](https://docs.docker.com/desktop/mac/install/)
- Windows: [how to install](https://docs.docker.com/desktop/windows/install/)

### make

- Linux: `sudo apt-get install make`
- Mac: `brew install make`
- Windows: [make setup for Windows](https://www.pascallandau.com/blog/structuring-the-docker-setup-for-php-projects/#install-make-on-windows-mingw)

## How to setup the environment

Corresponding docker environment has been created and can be setup via the
following
`make` commands

```
- make docker-build-from-scratch
- make docker-up
- make pip-install
```

and verify via `docker ps` that the container is running

```
$ docker ps
CONTAINER ID   IMAGE              COMMAND                  CREATED          STATUS          PORTS     NAMES
0d8281610db0   docker_workspace   "/usr/bin/docker-ent…"   18 seconds ago   Up 16 seconds             docker_workspace_1
```

## Verify the setup is working

In order to verify that the setup is working as expected run the `make verify`
target.
The output should look like the following:

```
 $ make verify-setup
============================= test session starts ==============================
platform linux -- Python 3.9.13, pytest-7.1.2, pluggy-1.0.0
rootdir: /usr/src/app
collected 3 items

test/test_main.py ...                                                    [100%]

============================== 3 passed in 0.01s ===============================
```

## Task

After the coding challenge is does please

- add a new commit
- push it to your repository
- send us a link to your repository
