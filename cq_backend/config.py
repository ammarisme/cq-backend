import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="cq_backend",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="cq_backend_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from cq_backend.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export cq_backend_KEY=value
export cq_backend_KEY="@int 42"
export cq_backend_KEY="@jinja {{ this.db.uri }}"
export cq_backend_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
cq_backend_ENV=production cq_backend run
```

Read more on https://dynaconf.com
"""
