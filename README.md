# Everything's Okay

<p align="center">
  <em>A Flask app just to show that everything's okay when you access a URL</em>
</p>
<p align="center">
  <a href="https://github.com/mauprogramador/everythings-okay/releases/tag/v1.0.0" target="_blank" rel="external" title="App Version">
    <img src="https://img.shields.io/github/v/tag/mauprogramador/everythings-okay?logo=github&label=App Version&color=E9711C" alt="App Version">
  </a>
  <a href="https://www.python.org/" target="_blank" rel="external" title="Python3 Version">
    <img src="https://img.shields.io/badge/Python-v3.11-3776AB?logo=python&logoColor=FFF" alt="Python3 Version">
  </a>
</p>

---

Federal Institute of Mato Grosso do Sul - <a href="https://www.ifms.edu.br/campi/campus-tres-lagoas" target="_blank" rel="external" title="IFMS - Campus Três Lagoas">IFMS - Campus Três Lagoas</a><br/>
Technology in Systems Analysis and Development - <a href="https://www.ifms.edu.br/campi/campus-tres-lagoas/cursos/graduacao/analise-e-desenvolvimento-de-sistemas" target="_blank" rel="external" title="TADS">TADS</a><br/>

**Web App**: <a href="http://0.0.0.0:2004/" target="_blank" rel="external" title="Web API">http://0.0.0.0:2004/</a>

---

## Configuration

The **App** will run, by default, with the following options:

| **Parameter**  | **Description**                                                                                 | **Default** |
| -------------- | ----------------------------------------------------------------------------------------------- | ----------- |
| `debug`        | Enable the debug mode                                                                           | `false`     |
| `host`         | Sets the hostname to listen on. <br>Setting `0.0.0.0` make the application externally available | `0.0.0.0`   |
| `port`         | Sets the web server port on which the application will run                                      | `8000`      |

You can also create a `.env` file to configure the port on which the application will run:

```dotenv
PORT=2004
```

## Run locally with Pip

You will need <a href="https://www.python.org/downloads/release/python-3117/" target="_blank" rel="external" title="Python3.11">Python3 `v3.11`</a> with <a href="https://pip.pypa.io/en/stable/installation/" target="_blank" rel="external" title="Pip">Pip</a> and <a href="https://docs.python.org/3/library/venv.html" target="_blank" rel="external" title="Pip">Venv</a> installed to run the **Flask** application.

```bash
# Setup Venv and Install dependencies
make setup

# Activate Venv
source .venv/bin/activate

# Run the App locally
(.venv) make run
```

---

This project is licensed under the terms of the [MIT license](./LICENSE)
